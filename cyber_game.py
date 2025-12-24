import streamlit as st
import time

# إعدادات الشاشة الكاملة
st.set_page_config(page_title="CODE CATCHER: ULTIMATE", page_icon="☣️", layout="wide")

# هندسة الواجهة (CSS) - ستايل الاستخبارات الرقمية
st.markdown("""
    <style>
    .stApp { background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZ3bmZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKSjPqcKGRZaO3u/giphy.gif'); background-size: cover; }
    h1, h2, h3, p, label { color: #00FF41 !important; text-shadow: 0 0 10px #00FF41; font-family: 'Share Tech Mono', monospace; text-align: right; }
    .stButton > button { width: 100%; border: 2px solid #00FF41; background-color: rgba(0,255,65,0.1); color: #00FF41; font-size: 20px; font-weight: bold; transition: 0.5s; height: 60px; }
    .stButton > button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 30px #00FF41; transform: scale(1.02); }
    .terminal-box { border: 2px solid #00FF41; padding: 30px; background-color: rgba(0,0,0,0.8); border-radius: 5px; direction: rtl; }
    .glitch { color: white; animation: glitch 1s linear infinite; }
    @keyframes glitch { 2% { text-shadow: 2px 0 red, -2px 0 blue; } }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة
if 'mode' not in st.session_state: st.session_state.mode = "auth"

# --- 1. مرحلة التصريح (الدخول) ---
if st.session_state.mode == "auth":
    st.markdown("<h1 class='glitch' style='text-align: center;'>☣️ نظام كود-قاتشر: البروتوكول الأخير</h1>", unsafe_allow_html=True)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=500)
    
    # محاكاة تشغيل الموسيقى (رابط بديل ومباشر)
    st.markdown("### 🎵 اضغطي تشغيل لتفعيل موسيقى القضاء")
    st.video("https://www.youtube.com/watch?v=mt-C3C78_wE") # موسيقى قوية من يوتيوب تفتح كخلفية
    
    user_id = st.text_input("إدخال رمز التعريف (اسمك):", placeholder="الجوري...")
    if st.button("تأكيد الهوية وتفعيل النظام 🔓"):
        if user_id:
            st.session_state.user_id = user_id
            st.session_state.mode = "briefing"
            st.rerun()

# --- 2. الفصل الأول: القصة الطويلة (الخطر المحدق) ---
elif st.session_state.mode == "briefing":
    st.markdown(f"<h2>🕵️‍♂️ ملف القضية المفتوحة: العملية (صفر)</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="terminal-box">
    المحققة <b>{st.session_state.user_id}</b>، مرحباً بكِ في المركز الوطني للعمليات السيبرانية. <br><br>
    لقد حدث ما كنا نخشاه.. في منتصف الليل، تم اختراق نظام "المنصة التعليمية الوطنية". 
    الهاكر ليس شخصاً عادياً، إنه يستخدم تقنيات <b>Quantum Hacking</b>. <br><br>
    <b>تفاصيل الجريمة:</b><br>
    1. تم تشفير ملفات درجات مليون طالب وطالبة.<br>
    2. النظام الآن يرسل رسائل وهمية لجميع أولياء الأمور تطلب مبالغ مالية.<br>
    3. الهاكر زرع "دودة رقمية" (Worm) تنتشر في أجهزة المعلمات الآن!<br><br>
    لقد تتبعنا الإشارة، الهاكر يختبئ خلف 7 خوادم وهمية، وقد ترك رسالة مشفرة تقول: 
    "إذا أردتم مفتاح فك التشفير، عليكم هزيمتي في قاعة القضاء الرقمي، لديكم 5 دقائق قبل مسح السيرفر بالكامل".<br><br>
    <b>هل أنتِ مستعدة للمخاطرة بسمعتكِ المهنية لإنقاذ مستقبل الطلاب؟</b>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("بدء عملية الهجوم المضاد 🔥"):
        st.session_state.mode = "interrogation"
        st.rerun()

# --- 3. الفصل الثاني: التحقيق والأسئلة ---
elif st.session_state.mode == "interrogation":
    st.markdown("<h3>⚡ المعركة السيبرانية: الجوري vs الظل الأسود</h3>", unsafe_allow_html=True)
    cols = st.columns([1, 1])
    
    with cols[0]:
        st.markdown("<p style='color:red !important;'>🚨 حالة النظام: تحت الهجوم</p>", unsafe_allow_html=True)
        st.write("---")
        q1 = st.radio("🛡️ التحدي 1: الهاكر أرسل ملف باسم (grades_update.exe). ما هو قرارك؟", ["فتحه لفحص الدرجات", "حذفه فوراً وعمل Scan للشبكة", "إرساله لصديقتي"])
        q2 = st.radio("🛡️ التحدي 2: اكتشفنا أن الهاكر استخدم 'هجمة الرجل في المنتصف' (MITM). كيف نمنعه؟", ["استخدام VPN وتشفير SSL", "إغلاق الشاشة", "تغيير لغة الحاسب"])
    
    with cols[1]:
        st.write("---")
        q3 = st.radio("🛡️ التحدي 3: أي من الروابط التالية هو 'رابط ملغم' زرعه الهاكر؟", ["https://saudi-edu.gov.sa", "http://login-school-verify.xyz/auth", "https://microsoft.com"])
        q4 = st.radio("🛡️ التحدي 4: ما هي أقوى وسيلة لحماية حساب المديرة من الاختراق المستقبلي؟", ["كلمة مرور من 4 أرقام", "مفتاح أمان فيزيائي (Yubikey)", "عدم استخدام الكمبيوتر"])

    if st.button("⚖️ إصدار الحكم التقني"):
        if q1 == "حذفه فوراً وعمل Scan للشبكة" and q2 == "استخدام VPN وتشفير SSL" and q3 == "http://login-school-verify.xyz/auth" and q4 == "مفتاح أمان فيزيائي (Yubikey)":
            st.session_state.mode = "victory"
        else:
            st.error("❌ خطأ! الهاكر اخترق جدار حماية إضافي. ركزي يا جوري!")
        st.rerun()

# --- 4. الفصل الأخير: النصر والتقييم ---
elif st.session_state.mode == "victory":
    st.balloons()
    st.markdown("<h1>🏆 تم استعادة السيطرة: نصر الجوري الأسطوري</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="terminal-box" style="border-color: gold;">
    لقد سقط (الظل الأسود)! تم فك التشفير في الثانية الأخيرة. <br>
    المحقق <b>{st.session_state.user_id}</b>، لقد أثبتِّ أنكِ درع الوطن الرقمي. 
    الطلاب والمعلمون مدينون لكِ بهذا النصر.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📝 كتابة ميثاق الأمان الرقمي:")
    advice = st.text_area("بصفتكِ الخبيرة الأولى، وضعي نصيحتكِ للتاريخ:")
    
    if st.button("ختم الملف برتبة (خبير أمني) 🎖️"):
        st.info("جاري تحليل بلاغكِ النهائي...")
        time.sleep(2)
        st.success("تم اعتماد النصيحة! تقييمك: 10/10 - عبقرية أمنية.")
        st.markdown(f"<h3 style='text-align:center;'>إعداد المبدعة: الجوري ✨</h3>", unsafe_allow_html=True)
        if st.button("محاكاة هجوم جديد 🔄"):
            st.session_state.clear()
            st.rerun()
