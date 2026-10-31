---
name: uzbek-new-latin-alphabet
description: Convert, proofread, and explain Uzbek text under the 2026 Latin alphabet reform (Oʻ→Ö, Gʻ→Ğ, Sh→Ş, Ch→Ç; "ng" no longer a separate letter). Use this whenever the user gives Uzbek text in old Latin (o', g', sh, ch, ʻ) or Cyrillic (ў, ғ, ш, ч) and wants it converted, fixed, or checked in the new alphabet; when they paste Uzbek text containing Ö Ğ Ş Ç and ask to proofread it; or when they ask about "yangi alifbo", "yangi lotin alifbosi", "yangi o'zbek alifbosi", the 28-letter alphabet, or how the reform changes spelling. Trigger even if the user never names the alphabet explicitly, e.g. "bu matnni yangi imloga o'tkazib ber" or "convert this Uzbek text to the new script".
---

# Uzbek new Latin alphabet (2026 reform)

This skill covers four jobs: converting old Latin to the new alphabet, converting Cyrillic to the new alphabet, proofreading text already written in the new alphabet, and explaining the reform.

## Status of the reform

The law was signed on 21 October 2026 and the revised alphabet takes effect on 22 April 2027. Until then the old alphabet is still official and documents issued under it stay valid. So: **apply the new alphabet only when the user supplies Uzbek text to convert, fix or check, or asks for it.** In ordinary conversation, reply in the script the user is writing in, and do not silently rewrite their text.

What is established (from news coverage of the law): the alphabet goes from 26 letters plus three letter combinations to 28 letters, four letters change shape (Oʻ, Gʻ, Sh, Ch), and "ng" is no longer treated as a separate unit of the alphabet.

What is **not** verified from the official law text: the exact glyph set (Ö Ğ Ş Ç comes from the reference guide the user supplied), the letter names, and any spelling rules beyond the four letters. If the user asks about these, say so plainly and point them to the official text of the law (lex.uz) instead of presenting the guide's details as settled. Never invent school or publishing timelines.

## The four letter changes

| Old Latin | New | Cyrillic |
|---|---|---|
| Oʻ oʻ | Ö ö | Ў ў |
| Gʻ gʻ | Ğ ğ | Ғ ғ |
| Sh sh | Ş ş | Ш ш |
| Ch ch | Ç ç | Ч ч |

Everything else (q, x, h, j, y, etc.) is unchanged. "ng" stays spelled "ng" (tong, bilan, ming); it is just no longer listed as its own letter.

Use precomposed Unicode characters (Ö U+00D6, Ğ U+011E, Ş U+015E, Ç U+00C7 and lowercase), never a base letter plus combining mark, and never output Oʻ/Gʻ unless the user asks for a comparison with the old spelling.

The tutuq (hard sign / glottal stop) stays and is written as ’ (U+2019): ma’no, e’lon, san’at, s’yezd. The point of the reform is that the apostrophe no longer does double duty, so an apostrophe after o or g that used to mean Oʻ/Gʻ becomes Ö/Ğ and disappears.

## Converting old Latin text

For anything longer than a sentence or two, run the bundled script and then review its output, because it handles the mechanical rules reliably and consistently:

```bash
python scripts/convert.py input.txt --report          # or:  echo "text" | python scripts/convert.py - --report
python scripts/convert.py input.txt --keep Chrome,Shell --report   # leave named words untouched
```

For short snippets you can convert by hand using the same rules. Either way, the rules are:

1. **Apostrophe after o/g means Oʻ/Gʻ.** o'/oʻ/o‘/o’/o` → ö, g'/gʻ/g‘/g’/g` → ğ (and capitals). People type these with many different characters; treat them all alike. Includes word-final cases: tog' → toğ, bog' → boğ.
2. **Any other apostrophe is a tutuq** and is normalised to ’ : ma'no → ma’no.
3. **sh → ş, ch → ç**, with case following the first letter (Sh → Ş, SH → Ş). Convert inside words and names: Shavkat → Şavkat, qo'shiq → qöşiq, ko'cha → köça.
4. **Leave non-Uzbek text alone.** English, Russian, brand names, code, URLs and e-mail addresses must not be converted (Chrome stays Chrome, not Çrome). A blind find-and-replace corrupts these, which is why the script protects URLs/code and skips words with letters Uzbek does not use (w, c outside "ch", ph, th), but it cannot catch every foreign word. Read the result and pass `--keep` for anything it missed.
5. **Check ambiguities by reading, not by pattern.** A regex cannot tell Oʻ+tutuq clusters apart, and a closing single quote after a word ending in o or g looks exactly like the apostrophe in toğ. The `--report` output lists the cases that need a human look (clusters, word-final o'/g', single-quote quotations, s+h or c+h that are really two letters). Resolve them from context and mention any you were unsure about.

## Converting Cyrillic text

The script converts Cyrillic and Latin in the same pass (mixed text is fine). The mapping:

- Unchanged-style letters: а a, б b, в v, г g, д d, ж j, з z, и i, й y, к k, л l, м m, н n, о o, п p, р r, с s, т t, у u, ф f, х x, қ q, ҳ h, э e.
- The four reform letters: ў ö, ғ ğ, ш ş, ч ç.
- **е** → *ye* at the start of a word or after a vowel or ъ (елкан → yelkan, съезд → s’yezd); → *e* after a consonant (беш → beş).
- **ё** → yo, **ю** → yu, **я** → ya (тайёр → tayyor).
- **ц** → *s* at the start of a word (цирк → sirk), *ts* between vowels or at the end (федерация → federatsiya).
- **ъ** → ’ (tutuq).
- нг → ng.

Things the user's guide does not cover, handled by carrying over the existing orthography: ц after a consonant → s (функция → funksiya), ь is dropped, щ → şç. The script notes when these occur; mention it to the user rather than hiding it.

## Proofreading text already in the new alphabet

Check for, and fix:

- Leftover old forms in Uzbek words: oʻ/gʻ/o'/g', sh, ch that should be ö, ğ, ş, ç.
- Over-conversion: ş/ç inside English or other non-Uzbek words, "ng" wrongly altered, or a genuine tutuq turned into ö/ğ.
- Wrong or invented characters (ü, ı, ñ, ŝ, decomposed accents), or the wrong apostrophe (straight ' or ʻ where ’ belongs).
- Mixed scripts within one word (a Cyrillic letter inside a Latin word).
- Capitalisation of Ö Ğ Ş Ç (Şavkat, ÖZBEKISTON).

Do not "fix" ordinary spelling or grammar the user did not ask about; if you notice something, mention it in one line after the corrected text.

## Explaining the reform

Answer from the "Status of the reform" section above, keep it short, and be explicit about what is confirmed and what is not. Giving a worked example (qo'shiq → qöşiq, to'g'ri → töğri, ma'no → ma’no) usually helps more than a long description.

## Output format

Give the converted or corrected text first, exactly as it should be pasted, with the original paragraph and line structure preserved. Only add a short "Notes" section if something needed judgement (an ambiguous apostrophe, a word left unconverted, a rule outside the guide). Write notes in the language the user used. For proofreading, add a compact list of what you changed. Do not add a lecture on the reform unless asked.

## Gotchas learned from the source guide

The reference guide this skill was built from contains a few slips; do not reproduce them:

- Its example output shows "tögʻrisidagi" with the old ʻ; the correct form is **töğrisidagi**.
- It writes the sample word as "qoşik"; the correct conversion of qo'shiq is **qöşiq**.
- Its Cyrillic examples "Besh", "Eshik", "Yaxshi" are in the *old* spelling; in the new alphabet they are **Beş, Eşik, Yaxşi**.
- Its rule 2 on the tutuq is garbled (it lists g’azal as a tutuq example); the tutuq is only for hard-sign positions such as ma’no, e’lon, s’yezd.
