#▒▒▒# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .tele_https://t.me/y_o_v▒▒▒▒

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZelzalMusic import app
from ZelzalMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي </b>\n<b>» استخـدم الازرار بالاسفـل\n» لـ تصفـح اوامـر سورس  </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر الجروبات •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القناة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[  
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبـاً بك عـزيـزي المطـور </b>\n\n<b>» استخـدم الازرار بالاسفـل \n» لـ تصفـح اوامـر سورس  </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• التحـديث •", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "• الـرفــع •", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "• الـحظــر •", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "• الاشعــارات & المسـاعــد •", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
★¦ تاك لعمل تاك للكروب
★¦ الرابط لجلب رابط الكروب
★¦ همسه برد ع شخص
★¦ رفع مشرف مع منع تصفية
★¦ كشف المجموعه لعرض معلومات المجموعه
★¦ تثبيت برد ع رساله يثبت رساله بلكروب
★¦ غادر يغادر بوت تلقائي من كروب بواسطه مطور بوت
★¦ يوت او تنزيل+اسم اغنيه لتنزيل الاغنيه
★¦ حجره للعب حجره ورا مقص
★¦ ابراج لتحليل برجك
★¦ اكبتلي + اكتب اي شيئ ليكتبلك عبر ذكاء الاصتناعي
★¦ قولي + اكتب اي شيئ يقولها بمقطع صوتي عبر ذكاء الاصتناعي
★¦ المطور لعرض معلومات المطور
★¦ تلجراف + برد ع صوره 
★¦ نسبه الرجوله لعرض معلومات رجولتك
★¦ لعبه انصحني
★¦ كتابات
★¦ اوقات الصلاه
★¦ تفعيل /تعطيل الادعيه ينشر ادعيه تلقائي بلكروب
★¦ افلام لعرض افلام تقدر تشاهد
★¦ لعبه الاحرف ب امر /احرف
★¦ فتح الكول لفتح الكول ب الكروب
★¦ مين في الكول لعرض من متواجدين ب الكول
★¦ اعلان البوت / لعمل اعلان للبوت
★¦ لو خيروك /خيروك
★¦اسال / س/ سوال
★¦ ص /صراحه
★¦ تشغيل + اسم الاغنيه

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر الادمــن :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / انهاء / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / كملي
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>

رفع ادمن/تنزيل ادمن
<b>- لـ رفـع/تنزيـل ادمـن فـي البـوت</b>

الادمنيه
<b>- لـ عـرض قائمـة ادمنيـة البـوت</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل مباشـر</b>
<b>- ارسـل (/channelplay او ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الاوامــر بالاسفـل لـ التشغيـل</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
<b>- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة</b>

فيديو + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

ايقاف / انهاء / اسكت / كافي
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

وقف / توقف
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف
<b>- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تقديم + عـدد الثـوانـي
<b>- لـ تقديـم الاغنيـه لـ الامـام</b>
رجوع + عـدد الثـوانـي
<b>- لـ إرجـاع الاغنيـه لـ الخـلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجلات
<b>- لـ جلب سجـلات البـوت 📋</b>

تحديث
<b>- لـ تحديـث البــوت</b>

اعاده تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي ميـوزك البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

بلوك/الغاء بلوك/المبلكين
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت</b>

احظره عام/الغاء حظره عام
<b>- لـ حظـر/الغـاء حظـر شخـص من استخـدام ميـوزك البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة/سماح
<b>- لـ حظـر/الغـاء حظـر مجموعـة من استخـدام ميـوزك البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمــة اوامــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة اوامــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل اشعـارات مجموعـة سجـل البــوت</b>

المغادره التلقائيه تفعيل/تعطيل
<b>- لـ تفعيـل/تعطيـل المغـادره التلقائيـه لـ الحسـاب المسـاعـد مـن المجمـوعـات عنـد عـدم استـخـدام الميـوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )
