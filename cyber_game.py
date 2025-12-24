import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Code-Catcher Game", page_icon="🛡️", layout="centered")

# تنسيق الواجهة (ألوان الأمن السيبراني: أسود وأخضر فسفوري)
st.markdown("""
    <style>
    .stButton > button { 
        width: 100%; border-radius: 15px; height: 3.5em; 
        background-color: #00FF41; color: black; font-weight: bold; 
        border: 2px solid #003B00; 
    }
    .stButton > button:hover { background-color: #003B00; color: #00FF41; }
    body { background-color: #0D0208; }
    .stRadio > label { font-size: 20px !important; font-weight: bold; color: #00FF41; }
    h1, h2, h3 { color: #00FF41 !important; text-align: center; }
    .footer-text { position: fixed; bottom: 10px; width: 100%; text-align: center; color: #00FF41; font-weight: bold; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة
if 'cyber_stage' not in st.session_state:
    st.session_state.cyber_stage = "start"
if 'cyber_score' not in st.session_state:
    st.session_state.cyber_score = 0
if 'current_virus' not in st.session_state:
    st.session_state.current_virus = 0

# قاعدة بيانات هجمات الفيروسات (الوحوش)
attacks = [
    {
        "type": "الروابط المشبوهة 🔗",
        "q": "وصلتك رسالة: 'مبروك ربحت آيفون! اضغط هنا: http://apple-gift-win.xyz'. هل هذا الرابط:",
        "options": ["رابط آمن ورسمي", "رابط تصيد احتيالي (Phishing)", "رابط تحديث للجهاز"],
        "a": "رابط تصيد احتيالي (Phishing)"
    },
    {
        "type": "كلمات المرور 🔑",
        "q": "أي من كلمات المرور التالية تعتبر الأقوى والأكثر أماناً؟",
        "options": ["12345678", "Admin2024", "J@o0u#R_9!z"],
        "a": "J@o0u#R_9!z"
    },
    {
        "type": "الهندسة الاجتماعية 👤",
        "q": "اتصل بك شخص يدعي أنه موظف بنك وطلب رمز التفعيل المرسل لجوالك. ماذا تفعل؟",
        "options": ["أعطيه الرمز بسرعة", "أغلق الخط فوراً", "أطلب منه الانتظار"],
        "a": "أغلق الخط فوراً"
    },
    {
        "type": "تأمين الحسابات 📱",
        "q": "ما هي أفضل وسيلة لحماية حساباتك من الاختراق حتى لو سُرقت كلمة المرور؟",
        "options": ["تغيير اسم المستخدم", "تفعيل التحقق الثنائي (2FA)", "مسح التطبيق"],
        "a": "تفعيل التحقق الثنائي (2FA)"
    },
    {
        "type": "البرمجيات الخبيثة 👾",
        "q": "وجدت فلاش ميموري (USB) مجهول في المدرسة. التصرف الصحيح هو:",
        "options": ["تجربته على جهازي", "تسليمه للمعلمة دون فتحه", "مسح محتواه واستخدامه"],
        "a": "تسليمه للمعلمة دون فتحه"
    }
]

# --- شاشة البداية ---
if st.session_state.cyber_stage == "start":
    st.title("👾 لعبة كود-قاتشر (🛡️ Code-Catcher)")
    # الصورة التي طلبتِها (المحارب بالسيفين)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=350)
    st.subheader("وحوش الفايروسات تهاجم بياناتك! هل تستطيعين صدها؟")
    if st.button("🛡️ ابدأ حماية نظامك الآن"):
        st.session_state.cyber_stage = "battle"
        st.rerun()
    # اسمك في الأسفل
    st.markdown(f'<div class="footer-text">تطوير خبيرة الأمن السيبراني: الجوري 🛡️</div>', unsafe_allow_html=True)

# --- شاشة المعركة (الأسئلة) ---
elif st.session_state.cyber_stage == "battle":
    idx = st.session_state.current_virus
    attack = attacks[idx]
    
    st.header(f"👾 هجوم {attack['type']}")
    st.write(f"**تحدي الحماية رقم {idx + 1}**")
    
    choice = st.radio(attack['q'], attack['options'], key=f"q_{idx}")
    
    if st.button("إطلاق جدار الحماية 🔥"):
        if choice == attack['a']:
            st.session_state.cyber_score += 1
            st.toast("تم صد الهجوم بنجاح! ✅")
        else:
            st.toast("اختراق! الوحش تجاوز دفاعك ❌")
            
        if idx < len(attacks) - 1:
            st.session_state.current_virus += 1
        else:
            st.session_state.cyber_stage = "result"
        st.rerun()

# --- شاشة التحليل النهائي ---
elif st.session_state.cyber_stage == "result":
    st.title("📊 تقرير الفحص الأمني")
    score = st.session_state.cyber_score
    
    if score >= 4:
        st.balloons()
        st.success(f"النتيجة: {score} من 5")
        st.header("🏆 الرتبة: خبير أمني محترف")
        st.write("أنتِ تملكين وعياً سيبرانياً ممتازاً وقادرة على حماية بياناتك.")
    else:
        st.error(f"النتيجة: {score} من 5")
        st.header("⚠️ الرتبة: مستخدم معرض للخطر")
        st.write("بياناتك في خطر! تحتاجين لتعلم مهارات الدفاع الرقمي.")

    st.write("---")
    st.subheader("💡 نصائح كود-قاتشر للأمان:")
    st.info("1. لا تضغطي على أي رابط مشبوه.")
    st.info("2. استخدمي كلمات مرور معقدة (رموز + أرقام + حروف).")
    st.info("3. فعلي التحقق بخطوتين في كل حساباتك.")
    
    if st.button("🔄 إعادة تأمين النظام"):
        st.session_state.cyber_stage = "start"
        st.session_state.cyber_score = 0
        st.session_state.current_virus = 0
        st.rerun()
