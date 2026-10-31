#!/usr/bin/env python3
"""Convert Uzbek text (old Latin and/or Cyrillic) to the new 2026 Latin alphabet.

Handles the mechanical part so the model can spend its attention on judgement
calls (ambiguous apostrophes, non-Uzbek words, quotations). Always review the
output and the --report notes before handing text back to the user.

Usage:
    python convert.py input.txt                 # converted text to stdout
    python convert.py input.txt -o out.txt      # write to a file
    echo "O'zbek" | python convert.py -         # read stdin
    python convert.py input.txt --keep Chrome,Shell --report
"""
import argparse
import re
import sys
import unicodedata

TUTUQ = "\u2019"            # U+2019: the apostrophe that stays in the new alphabet
MARK = "\uE000"             # private-use placeholder for "some apostrophe"
APOS = "'\u2019\u2018\u02bb\u02bc`\u00b4\u2032"   # everything people type as an apostrophe

# Protected spans are never touched: code fences, inline code, URLs, e-mail addresses.
PROTECT_RE = re.compile(
    r"(```.*?```|(?<![A-Za-z])`[^`\n]+`(?![A-Za-z])|https?://\S+|www\.\S+|[\w.+-]+@[\w-]+\.[\w.-]+)", re.S
)
CYR_RE = re.compile(r"[\u0400-\u04FF]+")
# A Latin word: letters, apostrophes between letters, optionally a trailing apostrophe
# (tog', bog'). Backtick-like marks only count between letters so code spans survive.
LAT_WORD_RE = re.compile(
    r"[A-Za-z]+(?:[" + re.escape(APOS) + r"]+[A-Za-z]+)*(?:[" + re.escape("'\u2019\u2018\u02bb\u02bc") + r"]+)?"
)
# Letters Uzbek Latin does not use: a word like "Windows" or "check" is not Uzbek.
FOREIGN_RE = re.compile(r"[wW]|[cC](?![hH])|[pP][hH]|[tT][hH]")

CYR_MAP = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ё": "yo", "ж": "j", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
    "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "x", "ч": "\u00e7",
    "ш": "\u015f", "щ": "\u015f\u00e7", "ъ": TUTUQ, "ы": "i", "ь": "", "э": "e",
    "ю": "yu", "я": "ya", "ў": "\u00f6", "қ": "q", "ғ": "\u011f", "ҳ": "h",
}
CYR_VOWELS = set("аеёиоуўэюяы")
YE_TRIGGERS = CYR_VOWELS | set("ъь")   # е after these -> "ye" (съезд -> s'yezd)


def cyr_word(w, flags):
    out, n = [], len(w)
    all_upper = n > 1 and w.isupper()
    for i, ch in enumerate(w):
        low, up = ch.lower(), ch.isupper()
        prev = w[i - 1].lower() if i else ""
        if low == "е":
            s = "ye" if (i == 0 or prev in YE_TRIGGERS) else "e"
        elif low == "ц":
            # guide: between vowels / word end -> ts, word start -> s.
            # After a consonant -> s (carried over from the existing orthography).
            s = "ts" if (prev in CYR_VOWELS or (i == n - 1 and i > 0)) else "s"
            if i > 0 and i < n - 1 and prev not in CYR_VOWELS:
                flags["notes"].add(f"ц after a consonant rendered as 's' in '{w}' (not covered by the guide)")
        elif low in CYR_MAP:
            s = CYR_MAP[low]
            if low == "щ":
                flags["notes"].add(f"щ rendered as 'şç' in '{w}' (not covered by the guide, please verify)")
        else:
            s = ch
            up = False
        if up and s:
            if len(s) > 1 and s != TUTUQ:
                nxt_upper = i + 1 < n and w[i + 1].isupper()
                s = s.upper() if (all_upper or nxt_upper) else s[0].upper() + s[1:]
            else:
                s = s.upper()
        out.append(s)
    return "".join(out)


def latin_word(w, flags):
    if FOREIGN_RE.search(w):
        flags["skipped"].add(w)           # looks non-Uzbek, leave as is
        return w
    t = re.sub("[" + re.escape(APOS) + "]", MARK, w)
    if MARK * 2 in t:
        flags["notes"].add(f"apostrophe cluster in '{w}': check which mark is Oʻ/Gʻ and which is the tutuq")
    # o' / g' -> Ö / Ğ  (an apostrophe after o or g is Oʻ / Gʻ, not a tutuq)
    t = re.sub("([OoGg])" + MARK,
               lambda m: {"O": "\u00d6", "o": "\u00f6", "G": "\u011e", "g": "\u011f"}[m.group(1)], t)
    # any apostrophe left is a tutuq (ma'no, e'lon, san'at)
    t = t.replace(MARK, TUTUQ)
    # digraphs; the first letter decides the case (Sh -> Ş, SH -> Ş, sh -> ş)
    t = re.sub(r"[Ss][Hh]", lambda m: "\u015e" if m.group(0)[0].isupper() else "\u015f", t)
    t = re.sub(r"[Cc][Hh]", lambda m: "\u00c7" if m.group(0)[0].isupper() else "\u00e7", t)
    if re.search(r"[OoGg][" + re.escape("'\u2019\u2018\u02bb\u02bc") + r"]$", w):
        flags["final"].add(w)
    return t


def convert_latin(seg, keep, flags):
    if keep:
        parts = re.split(r"\b(" + "|".join(re.escape(k) for k in keep) + r")\b", seg)
        return "".join(p if i % 2 else convert_latin(p, None, flags) for i, p in enumerate(parts))
    if re.search(r"(?<![A-Za-z0-9])['\u2018][A-Za-z]", seg):
        flags["quotes"] = True
    return LAT_WORD_RE.sub(lambda m: latin_word(m.group(0), flags), seg)


def convert_text(text, keep=None):
    flags = {"skipped": set(), "final": set(), "notes": set(), "quotes": False}
    out = []
    for i, piece in enumerate(PROTECT_RE.split(text)):
        if i % 2:                      # protected span
            out.append(piece)
            continue
        pos = 0
        for m in CYR_RE.finditer(piece):
            out.append(convert_latin(piece[pos:m.start()], keep, flags))
            out.append(cyr_word(m.group(0), flags))
            pos = m.end()
        out.append(convert_latin(piece[pos:], keep, flags))
    return unicodedata.normalize("NFC", "".join(out)), flags


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="file to convert, or - for stdin")
    ap.add_argument("-o", "--output", help="write result here instead of stdout")
    ap.add_argument("--keep", default="", help="comma-separated words to leave untouched (brand names, English words)")
    ap.add_argument("--report", action="store_true", help="print review notes to stderr")
    a = ap.parse_args()
    text = sys.stdin.read() if a.input == "-" else open(a.input, encoding="utf-8").read()
    keep = [k.strip() for k in a.keep.split(",") if k.strip()]
    result, flags = convert_text(text, keep)
    if a.output:
        open(a.output, "w", encoding="utf-8").write(result)
    else:
        sys.stdout.write(result)
    if a.report:
        e = sys.stderr.write
        if flags["skipped"]:
            e("Left unchanged (look non-Uzbek): " + ", ".join(sorted(flags["skipped"])) + "\n")
        if flags["final"]:
            e("Word-final o'/g' converted (check none is a closing quote): " + ", ".join(sorted(flags["final"])) + "\n")
        if flags["quotes"]:
            e("Text uses single-quote quotation marks: check word-final conversions near them.\n")
        for n in sorted(flags["notes"]):
            e("Note: " + n + "\n")


if __name__ == "__main__":
    main()
