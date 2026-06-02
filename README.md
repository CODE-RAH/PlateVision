<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=240&color=0:16a34a,100:0f172a&text=PlateVision&fontColor=ffffff&fontSize=60&fontAlignY=40&desc=Iranian%20License%20Plate%20Detector%20%7C%20CODE%20RAH&descAlignY=63&animation=twinkling" width="100%" />

# 🚗 سیستم هوشمند تشخیص پلاک خودروهای ایرانی

### توسعه داده شده توسط تیم تخصصی CODE RAH 💻

</div>

---

# 🛑 بیانیه کپی‌رایت و مالکیت معنوی (مهم)

> ⚠️ **تذکر جدی برای همکاران و اساتید:**  
> این کد برای اولین بار در سطح اینترنت منتشر می‌شود و توسط **امیرفرخانی موسس آکادمی آنلاین کدراه** پیاده‌سازی و کدنویسی شده است.  
> هرگونه استفاده، برداشته شدن سورس‌کد، تولید محتوای ویدیویی مشابه در سطح وب و آموزش آن **منحصراً مشروط به ذکر منبع و نام CODE RAH** است.  
> در غیر این صورت هیچ‌گونه رضایتی وجود نداشته و عواقب آن متوجه فرد خاطی خواهد بود.

---

# 📝 درباره پروژه

**PlateVision** یک سیستم بینایی ماشین برای تشخیص پلاک خودروهای ایرانی است که با Python و OpenCV پیاده‌سازی شده.

این سیستم هم روی فایل ویدیویی و هم روی دوربین زنده کار می‌کند و با الگوریتم‌های پردازش تصویر پیشرفته، پلاک‌های ایرانی را با دقت بالا شناسایی می‌کند.

---

# ⚡ ویژگی‌های فنی

- **بهبود تصویر با CLAHE**  افزایش کنتراست در فضای رنگی LAB برای تشخیص دقیق‌تر در نور ضعیف.

- **فیلتر Bilateral**  
  حذف نویز بدون از بین بردن لبه‌های حروف پلاک.

- **تشخیص هوشمند کانتور**  
  فیلتر بر اساس نسبت ابعاد `(2.5 - 4.5)` و مساحت نسبی پلاک ایرانی.

- **اعتبارسنجی کاراکتر**  
  بررسی وجود حداقل ۳ کاراکتر معتبر در ناحیه پلاک.

- **پردازش بلادرنگ**  
  پشتیبانی از ویدیو و دوربین با نمایش زنده نتیجه.

---

# 🚀 راهنمای نصب و راه‌اندازی

## 📥 مرحله اول: دانلود پروژه

روی دکمه سبز **Code** کلیک کرده و **Download ZIP** را انتخاب کنید، سپس از حالت فشرده خارج نمایید.

---

## 🧩 مرحله دوم: نصب Python

اگر Python روی سیستم ندارید، آخرین نسخه را دانلود و نصب کنید.  
هنگام نصب حتماً گزینه زیر را فعال کنید:
```text
Add Python to PATH
```

## 📦 مرحله سوم: نصب پکیج‌ها

bash
pip install opencv-python numpy imutils

---

## ▶️ مرحله چهارم: اجرا

فایل ویدیویی خود را با نام `vf.mp4` کنار `main.py` قرار دهید، سپس:

bash
python main.py

برای خروج از برنامه کلید `Q` را فشار دهید.

---

# 📂 ساختار پروژه


PlateVision/
├── main.py
└── vf.mp4

---

# 🧠 نحوه کار الگوریتم


ورودی ویدیو/دوربین
↓
بهبود تصویر (CLAHE + Saturation)
↓
تشخیص لبه (Bilateral Filter + Canny)
↓
یافتن کانتورهای چهارضلعی
↓
فیلتر نسبت ابعاد و مساحت
↓
اعتبارسنجی کاراکترهای پلاک
↓
نمایش کادر سبز روی پلاک

---

# 🛠️ پارامترهای قابل تنظیم

| پارامتر | مقدار پیش‌فرض | توضیح |
|--------|---------------|-------|
| `min_plate_aspect` | 2.5 | حداقل نسبت طول به عرض پلاک |
| `max_plate_aspect` | 4.5 | حداکثر نسبت طول به عرض پلاک |
| `clahe_clip` | 2.5 | شدت بهبود کنتراست |
| `edge_thresh1` | 30 | آستانه پایین Canny |
| `edge_thresh2` | 120 | آستانه بالای Canny |

---

# ⚡ فناوری‌های استفاده‌شده

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![imutils](https://img.shields.io/badge/imutils-ComputerVision-16a34a?style=for-the-badge)

</div>

---

# 🧠 درباره تیم CODE RAH

تیم **CODE RAH** یک گروه تخصصی در حوزه‌های پیشرفته فناوری است:

- 🤖 هوش مصنوعی و بینایی ماشین — `OpenCV` `YOLO` `ML`
- 💻 برنامه‌نویسی — `Python` `C#` `Java` `JavaScript`
- 🔒 امنیت سایبری — `Ethical Hacking` `Kali Linux`
- ⚙️ اینترنت اشیاء — `Arduino` `Raspberry Pi`

---

<div align="center">

# 💻 CODE RAH

### کدنویسی فقط نوشتن برنامه نیست؛ ساختن آینده است.

⭐ اگر از این پروژه خوشتان آمد، ستاره فراموش نشه ⭐

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0f172a,100:16a34a&section=footer" width="100%" />
`
