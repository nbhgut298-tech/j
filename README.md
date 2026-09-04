# ShaHm Music

بوت تيليغرام لتشغيل الموسيقى في المحادثات الصوتية.

## الإعداد

1. انسخ `sample.env` إلى ملف باسم `.env`.
2. أضف القيم المطلوبة: `API_ID` و`API_HASH` و`BOT_TOKEN` و`MONGO_DB_URI` و`LOGGER_ID` و`OWNER_ID` و`STRING_SESSION`.
3. ثبّت FFmpeg ثم ثبّت حزم بايثون:

   ```bash
   pip install -r requirements.txt
   ```

4. شغّل البوت:

   ```bash
   python3 -m ZelzalMusic
   ```

## مشكلة YouTube على VPS

إذا ظهر الخطأ `Sign in to confirm you’re not a bot`، صدّر كوكيز YouTube بصيغة
**Netscape cookies.txt** من متصفح فيه حساب YouTube مسجّل الدخول، وضعه في المجلد
الرئيسي للمشروع بجانب ملف `start`، ثم أضف هذا السطر إلى `.env`:

```env
YTDLP_COOKIES_FILE=cookies.txt
YTDLP_PLAYER_CLIENT=default,web_embedded
```

أعد تشغيل البوت بعد ذلك. لا ترفع ملف الكوكيز إلى Git أو ترسله في القنوات؛ فهو
يعطي صلاحية جلسة حسابك. عند توقفه لاحقاً صدّر ملفاً جديداً، وحدّث `yt-dlp` عبر
`pip install -U yt-dlp` داخل بيئة المشروع.

ثبّت المتطلبات بعد تحديث المشروع كي يُثبّت مكوّن JavaScript المطلوب من yt-dlp:

```bash
python -m pip install -r requirements.txt
```

عند استخدام Docker، اربط الملف كـ read-only وأشر إلى مساره داخل الحاوية:

```bash
docker run --env-file .env -e YTDLP_COOKIES_FILE=/run/secrets/youtube-cookies.txt \
  -v /opt/zelzal/cookies.txt:/run/secrets/youtube-cookies.txt:ro your-image
```

لا تضع مفاتيح API أو رموز البوت أو رابط MongoDB داخل `config.py` أو في مستودع عام.
