# Uzbek New Latin Alphabet

Uzbek tilidagi matnlarni 2026-yilgi yangi lotin alifbosiga o'giruvchi, tekshirish va to'g'rilash uchun mo'ljallangan loyiha. Loyiha asosan quyidagi vazifalarni bajaradi:

- eski lotin yozuvi yoki kirill yozuvidagi matnni yangi lotin alifbosiga o'tkazadi;
- mavjud yangi lotin alifbosidagi matnlarni tekshiradi va xatolarni tuzatadi;
- alifbo islohotining asosiy qoidalarini tushuntiradi;
- GitHub Copilot yoki boshqa AI-yordamchilar uchun maxsus `skill` fayl sifatida ishlatiladi.

Reponing maqsadi oddiy foydalanuvchilar va AI tizimlari uchun uzbek tilida aniq, standartlashtirilgan va izchil yozuvni ta'minlashdir.

## Loyiha haqida

Bu repoda yangi lotin alifbosining asosiy qoidalari, o'zgartirish qoidalari va avtomatik konvertatsiya mexanizmi jamlangan.

Asosiy reform qoidalari:

- `Oʻ` / `oʻ` → `Ö` / `ö`
- `Gʻ` / `gʻ` → `Ğ` / `ğ`
- `Sh` / `sh` → `Ş` / `ş`
- `Ch` / `ch` → `Ç` / `ç`
- `ng` alohida harf emas, lekin yozuvda saqlanadi
- ajratish belgisi (tutuq) `’` shaklida ishlatiladi

Boshqa so'zlar, jumla va kirill yozuvidagi belgilar ham avtomatik ravishda yangi lotin yozuviga moslashtiriladi, ammo foydalanuvchi tomonidan tekshirish va ba'zi holatlarni ko'zdan kechirish tavsiya etiladi.

## Loyiha maqsadi

Bu loyiha quyidagi muammolarni hal qiladi:

1. eski lotin yozuvi yoki kirill yozuvidagi matnni yangi standartga o'tkazish;
2. alifbo islohotiga oid aniq qoidalarni jamlash;
3. AI model uchun ko'rsatmalarni va konvertatsiya regullarini standartlashtirish;
4. bir xil yozuv qoidalari bilan ishlaydigan vazifalarni avtomatlashtirish.

Bu yondashuv nafaqat odamlar uchun, balki AI modellari, kod yozuvchilar va matn ishlovchilar uchun ham foydali bo'ladi.

## Repodagi fayllar

Repo tarkibi quyidagicha:

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
└── README.md
```

### 1) `AI_New_Uzbek_Alphabet_Guide.md`

Bu fayl loyiha uchun asosiy ma'lumotnoma bo'lib, alifbo reformi haqida batafsil tushuntirishlar, qoidalar, misollar va transformatsiya usullarini o'z ichiga oladi.

Nima uchun kerak:

- qoidalarni hujjatlashtirish;
- transformatsiya mezonlarini aniq yozish;
- AI uchun mos keluvchi saboqlar, misollar va noto'g'ri talablarga qarshi yo'l-yo'riq ko'rsatish.

### 2) `uzbek-new-latin-alphabet.skill`

Bu fayl GitHub Copilot yoki AI skill mexanizmi uchun tayyorlangan maxsus konfiguratsiya fayli hisoblanadi. U modelga "bu vazifa nima bo'lyaptimi" va "qanday ishlash kerak" degan ko'rsatmalarni beradi.

Nima uchun kerak:

- AI agent yoki Copilotga ma'lum vazifa bilan ishlashni o'rgatish;
- matnni konvertatsiya qilish, tekshirish va tahrirlashni avtomatlashtirish;
- turli savollarga standart javoblarni berishga yordam berish.

### 3) `uzbek-new-latin-alphabet/SKILL.md`

Bu faylning maqsadi skillning ichki texnik qo'llanmasi bo'lib, quyidagi ko'rsatmalarni o'z ichiga oladi:

- alifbo reformi statusi;
- eski lotin → yangi lotin konvertatsiya qoidalari;
- kirill → yangi lotin konvertatsiya qoidalari;
- matnni tekshirish va to'g'rilash usullari;
- qiyinchiliklar, gotcha/ogohlantirishlar.

Nima uchun kerak:

- bunday AI skillni aniq va izchil ishlatish;
- xatolarga yo'l qo'ymaslik;
- konvertatsiya natijalarini yana qayta tekshirishda yordam berish.

### 4) `uzbek-new-latin-alphabet/scripts/convert.py`

Bu Python skripti amaliy konvertatsiya mexanizmi hisoblanadi. U matnni old lotin va kirill yozuvidan yangi lotin yozuviga aylantiradi.

Nima uchun kerak:

- katta hajmdagi matnlarni avtomatik o'zgartirish;
- qoidalarni dastur orqali izchil qo'llash;
- ishlov berishdan oldin yotgan xatoliklarni aniqlashga yordam berish.

Skript qaysi funktsiyalarni bajaradi:

- matnni old lotin va kirilldan yangi alifboga moslashtirish;
- `Sh`, `Ch`, `O'`, `G'` va boshqa belgilarni standartlashtirish;
- qoldiq oldiy forma va xatoliklarni report qilish;
- `--report` parametridan foydalangan holda ko'rsatmalarni chiqarmoq;
- `--keep` orqali ayrim so'zlarni qo'lda saqlab qolish.

### 5) `uzbek-new-latin-alphabet.zip`

Bu arxiv repodagi skill yoki loyiha paketining yig'ilgan versiyasidir. U ko'pincha boshqa muhitlarga yoki platformalarga yuklash uchun tayyorlangan paket sifatida ishlatiladi.

Nima uchun kerak:

- tezkor tarqatish;
- boshqa muhitga oson ko'chirish;
- ishlatish uchun tayyorlangan paket.

### 6) `LICENSE`

Loyiha litsenziyasi. Bu fayl qaysi huquqlar va shartlar asosida foydalanish mumkinligini belgilaydi.

Nima uchun kerak:

- huquqiy tozalangan foydalanish;
- kodni qayta ishlatishdagi cheklovlarni aniq ko'rsatish;
- mualliflik huquqlarini saqlash.

## O'rnatish (Installation)

### Talablar

- Python 3.8+
- terminal/CLI
- UTF-8 kodirovkali matn fayllari

### Klon qilish

```bash
git clone https://github.com/SolijonSolayev/uzbek-new-latin-alphabet.git
cd uzbek-new-latin-alphabet
```

### Kerakli paketlar

Bu loyiha qo'shimcha paketlardan foydalanmaydi. Faqat Python standart kutubxonalari yetarli.

```bash
python --version
```

## Ishlatish (Usage)

### 1. Matn faylidan o'qib konvertatsiya qilish

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt
```

### 2. Konsoldan kirish berish

```bash
echo "O'zbek tili yangi alifboga o'tmoqda." | python uzbek-new-latin-alphabet/scripts/convert.py -
```

### 3. Natija haqida ma'lumot bilan chiqish

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt --report
```

Bu holatda skript quyidagilarni ham chiqaradi:

- qaysi so'zlar non-Uzbek deb qabul qilingan;
- qaysi so'zlar tekshirishga muhtoj;
- qaysi xatolar yoki noaniq holatlar mavjud.

### 4. Ayrim so'zlarni saqlab qolish

Agar biror brend, inglizcha so'z yoki maxsus nomlarni o'zgartirmaslik kerak bo'lsa:

```bash
python uzbek-new-latin-alphabet/scripts/convert.py input.txt --keep Chrome,Shell --report
```

## Misollar

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

Qo'lda yoki dastur orqali:

```text
Şavkat Mirziyoyev özbek tilining yangi alifbati haqida gapirdi.
```

### Apostrof qoidalari

- `ma'no` → `ma’no`
- `e'lon` → `e’lon`
- `qo'shiq` → `qöşiq`
- `to'g'ri` → `töğri`

## Qoidalar va muhim eslatmalar

Loyiha ishlash prinsiplari quyidagilarni nazarda tutadi:

1. `O'`, `G'`, `Sh`, `Ch` kabi oldiy yozuvlar yangi alifboga moslashtiriladi.
2. Tutuq belgisi `’` bilan yoziladi; oddiy `'` bu yerda xilma-xil yozuvlar uchun ishlatilmaydi.
3. `ng` alohida harf emas, lekin so'zlarning ichida saqlanadi.
4. Inglizcha so'zlar, URL manzillar, elektron pochta manzillari, kodlar yoki brend nomlari avtomatik o'zgartirilmaydi.
5. Matnni yakuniy tarzda qabul qilishdan oldin qo'lda tekshirish tavsiya etiladi, chunki ba'zi so'zlar kontekstga qarab noaniq bo'lishi mumkin.

## Nega bu loyiha kerak?

Ushbu loyiha quyidagi sabablar uchun muhim:

- uzbek alifbosining islohotini standartlashtirish;
- AI va matn konvertatsiyasi uchun qo'llanmalarni birlashtirish;
- matnlar bilan ishlaydigan tizimlar uchun qoidalarni izchillik bilan ta'minlash;
- turli platformalarda bir xil yozuv holatini qo'llab-quvvatlash.

Bu sohadagi muhimlik shundaki, yozuv standartlari faqat imlo masalasi emas, balki tilning rasmiy qabul qilinishidagi me'yor va kelib chiqish nuqtasi hamdir.

## Foydalanishda ehtiyot bo'lish kerak

Har bir avtomatik konvertatsiya natijasi to'liq mukammal bo'lavermaydi. Ba'zi so'zlar aniq kontekstga bog'liq bo'ladi. Shuning uchun:

- oddiy matnlarni avtomatik konvertatsiya qilish mumkin;
- uzun va rasmiy matnlarni tekshirish va to'g'rilash lozim;
- so'zning mazmuni, umumiy qiyofasi va yozilish tarixi yuqoriroq ahamiyatga ega.

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

Bu loyiha faqat bir skript emas; u Uzbek tilidagi yozuv islohotini standartlashtirishga intilayotgan texnik va lingvistik platformadir.

Uning asosiy qiymati shundaki:

- matnlarni avtomatik o'zgartiradi;
- yangi alifbo qoidalarini saqlaydi;
- foydalanuvchi va AI o'rtasida aniq muomala yaratadi;
- kelajakdagi uzbek tilidagi texnik mahsulotlar uchun asos bo'ladi.

Agar siz repoga birinchi marta qarasangiz, avval `AI_New_Uzbek_Alphabet_Guide.md` va `uzbek-new-latin-alphabet/SKILL.md` fayllarini o'qib chiqish tavsiya etiladi. Keyin esa `convert.py` skriptini ishlatib, amaliy natijalarni ko'rishingiz mumkin.

---

Created for the Uzbek New Latin Alphabet conversion project.
