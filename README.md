# Uzbek New Latin Alphabet

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-success" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" />
  <img alt="UTF-8" src="https://img.shields.io/badge/Encoding-UTF--8-1f6feb" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
  <img alt="Open Source" src="https://img.shields.io/badge/Open%20Source-Yes-181717?logo=github" />
  <img alt="AI Ready" src="https://img.shields.io/badge/AI%20Ready-GitHub%20Copilot-6F42C1" />
  <img alt="Language Standard" src="https://img.shields.io/badge/Language%20standard-Uzbek%20Latin-0A84FF" />
</p>

<p align="center">
  <a href="#bu-nima">Bu nima?</a> ·
  <a href="#demo">Demo</a> ·
  <a href="#features">Xususiyatlar</a> ·
  <a href="#why-this-project">Nega bu loyiha?</a> ·
  <a href="#usage">Ishlatish</a> ·
  <a href="#roadmap">Yo'l xaritasi</a>
</p>

<p align="center">
  <img width="820" alt="Uzbek new Latin alphabet overview" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80" />
</p>

> [!IMPORTANT]
> Bu loyiha uzbek tilidagi matnlarni 2026-yilgi yangi lotin alifbosiga o'girish, tekshirish va standartlashtirish uchun mo'ljallangan. Ochiq manbali, AI-ga tayyor va til standartlari uchun qulay yondashuvni taqdim etadi.

## Bu nima?

Uzbek New Latin Alphabet — bu uzbek tilidagi matnlarni yangi lotin alifbosiga avtomatik tarzda o'zgartirish, tekshirish va standartlashtirish uchun yaratilgan loyiha. Loyiha eski lotin yozuvi, kirill yozuvi va zamonaviy matnlar o'rtasidagi moslikni saqlashga yordam beradi.

Asosiy maqsadlar:

- eski lotin yoki kirill yozuvidagi matnlarni yangi lotin alifbosiga o'tkazish;
- mavjud yozuvdagi xatolarni aniqlash va tuzatish;
- alifbo islohotining asosiy qoidalarini standart tarzda hujjatlashtirish;
- GitHub Copilot, AI-agentlar va boshqa dasturiy tizimlar uchun yaxshi ishlaydigan yozuv ko'rsatmalarini yaratish.

Bu loyiha nafaqat matn konvertatsiyasi uchun, balki Uzbek tilining yozuv standartlarini modernizatsiya qilish, AI uchun ishga tushadigan qo'llanmalar yaratish va texnik hujjatlarda bir xil imlo qoidalarini saqlash uchun ham muhimdir.

## Demo

### Tez demo

```text
Kiruvchi:   O'zbekiston Respublikasi Prezidenti Shavkat Mirziyoyev yangi alifbo to'g'risidagi qonunni imzoladi.
Chiqarish:  Özbekiston Respublikasi Prezidenti Şavkat Mirziyoyev yangi alifbo töğrisidagi qonunni imzoladi.
```

```text
Kiruvchi:   Шавкат Мирзиёев ўзбек тилининг янги алфавити ҳақида гапирди.
Chiqarish:  Şavkat Mirziyoyev özbek tilining yangi alfaviti haqida gapirdi.
```

### Asosiy qoidalar

- `Oʻ` / `oʻ` → `Ö` / `ö`
- `Gʻ` / `gʻ` → `Ğ` / `ğ`
- `Sh` / `sh` → `Ş` / `ş`
- `Ch` / `ch` → `Ç` / `ç`
- `ng` alohida harf emas, lekin yozuvda saqlanadi
- ajratish belgisi (tutuq) `’` shaklida ishlatiladi

## Features

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>🔄 Konvertatsiya</strong><br />Eski lotin va kirill yozuvini yangi alifboga o'zgartiradi.</td>
      <td align="center"><strong>✅ Tekshirish</strong><br />Yozuvdagi xatolar, noaniq holatlar va standart bo'lmagan shakllarni aniqlaydi.</td>
      <td align="center"><strong>📘 Standart qoidalar</strong><br />Alifbo islohoti qoidalarini izchil va aniq tarzda tushuntiradi.</td>
      <td align="center"><strong>🤖 AI tayyor</strong><br />GitHub Copilot va AI-agentlar uchun qulay formatda ishlaydi.</td>
    </tr>
  </table>
</div>

### Loyiha nima qiladi?

- eski lotin va kirill yozuvidagi matnlarni yangi lotin alifbosiga o'tkazadi;
- yangi lotin yozuvidagi textlarni tekshiradi va xatolarni tuzatadi;
- alifbo reformining qoidalarini standartlashtiradi;
- qoidalarini AI, dasturiy modullar va matn ishlovchi tizimlar uchun qulay tarzda taqdim etadi;
- bir xil yozuv tizimi bo'yicha me'yor va amaliy misollarni ta'minlaydi.

## Why this project?

Bu loyiha quyidagi muammolarni hal qiladi:

1. eski lotin yozuvi yoki kirill yozuvidagi matnlarni yangi standartga o'tkazish;
2. alifbo islohotiga oid aniq qoidalarni jamlash;
3. AI model uchun ko'rsatmalarni va konvertatsiya regullarini standartlashtirish;
4. bir xil yozuv qoidalari bilan ishlaydigan vazifalarni avtomatlashtirish.

Ushbu yondashuv nafaqat oddiy foydalanuvchilar uchun, balki AI modellari, developerlar, matn muharrirlari, tarjimonlar, davlat va rasmiy hujjatlar bilan ishlaydigan tashkilotlar uchun ham foydali bo'ladi.

Asosiy afzalliklari:

- Uzbek alifbosining islohotini standartlashtirish;
- AI va matn konvertatsiyasi uchun qo'llanmalarni birlashtirish;
- matnlar bilan ishlaydigan tizimlar uchun qoidalarni izchillik bilan ta'minlash;
- turli platformalarda bir xil yozuv holatini qo'llab-quvvatlash.

## Usage

### 1) Matn faylidan o'qib konvertatsiya qilish

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt
```

### 2) Konsoldan kirish berish

```bash
echo "O'zbek tili yangi alifboga o'tmoqda." | python uzbek-new-latin-alphabet/scripts/convert.py -
```

### 3) Natija haqida ko'proq ma'lumot bilan chiqish

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt --report
```

### 4) Ayrim so'zlarni saqlab qolish

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt --keep Chrome,Shell --report
```

## Quick examples

### Old lotin yozuvidan yangi lotin yozuviga

Kiruvchi matn:

```text
O'zbekiston Respublikasi Prezidenti Shavkat Mirziyoyev yangi alifbo to'g'risidagi qonunni imzoladi.
```

Chiqarish:

```text
Özbekiston Respublikasi Prezidenti Şavkat Mirziyoyev yangi alifbo töğrisidagi qonunni imzoladi.
```

### Kirill yozuvidan yangi lotin yozuviga

Kiruvchi matn:

```text
Шавкат Мирзиёев ўзбек тилининг янги алфавити ҳақида гапирди.
```

Chiqarish:

```text
Şavkat Mirziyoyev özbek tilining yangi alfaviti haqida gapirdi.
```

### Apostrof qoidalari

- `ma'no` → `ma’no`
- `e'lon` → `e’lon`
- `qo'shiq` → `qöşiq`
- `to'g'ri` → `töğri`

## Project structure

```text
uzbek-new-latin-alphabet/
├── AI_New_Uzbek_Alphabet_Guide.md
├── LICENSE
├── uzbek-new-latin-alphabet.skill
├── uzbek-new-latin-alphabet.zip
├── uzbek-new-latin-alphabet/
│   ├── SKILL.md
│   └── scripts/
│       └── convert.py
├── README.md
└── .github/
```

### Repozitoriyning asosiy fayllari

- `AI_New_Uzbek_Alphabet_Guide.md` — loyiha haqida batafsil qo'llanma.
- `uzbek-new-latin-alphabet.skill` — GitHub Copilot / AI skill konfiguratsiyasi.
- `uzbek-new-latin-alphabet/SKILL.md` — texnik va amaliy ko'rsatmalar.
- `uzbek-new-latin-alphabet/scripts/convert.py` — asosiy konvertatsiya skripti.
- `README.md` — loyiha haqida qisqacha, chiroyli va SEOga mos keluvchi tavsif.

## Roadmap

```text
[✅] Yangi lotin alifbosiga avtomatik konvertatsiya
[✅] Kirill va eski lotin yozuvini tanib olish
[✅] Tekshiruv va xatolarni aniqlash
[✅] GitHub Copilot / AI skill formatiga moslash
[🚀] Kengaytirilgan qoidalar bazasi
[🚀] Ko'proq testlar va hujjatlar
[🚀] CLI va web-interfeys uchun qo'shimcha modullar
[🚀] Harflar va imlo nazorati uchun avtomatlashtirilgan tekshiruv
```

## O'rnatish

### Talablar

- Python 3.8+
- terminal / CLI
- UTF-8 kodirovkali matn fayllari

### Klon qilish

```bash
git clone https://github.com/SolijonSolayev/uzbek-new-latin-alphabet.git
cd uzbek-new-latin-alphabet
```

### Kerakli paketlar

Bu loyiha qo'shimcha paketlardan foydalanmaydi. Faqat Python standart kutubxonasi yetarli.

```bash
python --version
```

## Qoidalar va muhim eslatmalar

Loyiha ishlash prinsiplari quyidagilarni nazarda tutadi:

1. `O'`, `G'`, `Sh`, `Ch` kabi oldiy yozuvlar yangi alifboga moslashtiriladi.
2. Tutuq belgisi `’` bilan yoziladi; oddiy `'` bu yerda xilma-xil yozuvlar uchun ishlatilmaydi.
3. `ng` alohida harf emas, lekin so'zlarning ichida saqlanadi.
4. Inglizcha so'zlar, URL manzillar, elektron pochta manzillari, kodlar yoki brend nomlari avtomatik o'zgartirilmaydi.
5. Matnni yakuniy tarzda qabul qilishdan oldin qo'lda tekshirish tavsiya etiladi, chunki ba'zi so'zlar kontekstga qarab noaniq bo'lishi mumkin.

## Hissa qo'shish

Agar loyiha rivojlanishiga hissa qo'shmoqchi bo'lsangiz:

1. fork qiling;
2. o'zingizning branch'ini yarating;
3. o'zgarishlarni kiritib, test qiling;
4. pull request yuboring.

Hissa qo'shishdan avval qoidalarni diqqat bilan o'rganib chiqing va konvertatsiya natijalarini tekshirishni unutmang.

## Litsenziya

Bu loyiha MIT yoki mos keluvchi ochiq litsenziya asosida tarqatilgan bo'lishi mumkin. Batafsil ma'lumot uchun `LICENSE` faylini o'qib chiqing.

## Xulosa

Uzbek New Latin Alphabet loyiha sifatida oddiy konvertatsiya skripti emas, balki Uzbek tilining yozuv standartlarini modernizatsiyalashga qaratilgan open-source va AI-ga tayyor texnik platformadir. Bu loyiha yangi lotin alifbosini, imlo qoidalarini, konvertatsiya usullarini va AI uchun qulay ko'rsatmalarni bir joyga jamlaydi.

Natijada:

- matnlarni avtomatik o'zgartirish imkoniyati paydo bo'ladi;
- yangi alifbo qoidalari standartlashtiriladi;
- foydalanuvchi va AI tizimi o'rtasida aniq muomala yaratiladi;
- kelajakdagi uzbek tilidagi texnik, ilmiy va axborot mahsulotlari uchun asos bo'ladi.

Agar siz repoga birinchi marta qarasangiz, avval `AI_New_Uzbek_Alphabet_Guide.md` va `uzbek-new-latin-alphabet/SKILL.md` fayllarini o'qib chiqishni tavsiya qilamiz. Keyin esa `convert.py` skriptini ishlatishni boshlashingiz mumkin.

---

<p align="center">
  <img alt="Built with GitHub" src="https://img.shields.io/badge/Built%20with-GitHub-181717?logo=github" />
  <img alt="Markdown" src="https://img.shields.io/badge/Docs-Markdown-000000?logo=markdown" />
  <img alt="Python" src="https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white" />
</p>
