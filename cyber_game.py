import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Code Catcher: The Investigation", page_icon="🕵️‍♂️", layout="centered")

# التنسيق البصري المتقدم
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00FF41; border: 1px solid #00FF41; }
    .stButton > button { width: 100%; border-radius: 10px; background-color: transparent; color: #00FF41; border: 2px solid #00FF41; font-weight: bold; }
    .stButton > button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 20px #00FF41; }
    .story-box { padding: 20px; border: 1px solid #00FF41; border-radius: 10px; background-color: #0d0d0d; color: #00FF41; line-height: 1.6; }
    h1, h2, h3 { color: #00FF41 !important; text-align: center; }
    .terminal-text { font-family: 'Courier New', Courier, monospace; color: #00FF41; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة
if 'game_step' not in st.session_state:
    st.session_state.game_step = "welcome"
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""

# --- 1. شاشة الترحيب ---
if st.session_state.game_step == "welcome":
    st.markdown("<h1>🕵️‍♂️ أهلاً بك في عالم كود-قاتشر</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>من هُنا تبدأ رحلتك في عالم الأمن السيبراني</p>", unsafe_allow_html=True)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=300)
    
    player_n = st.text_input("أدخل اسمك أيها المحقق الرقمي:", placeholder="اكتب اسمك هنا...")
    if st.button("🚀 ابدأ الآن"):
        if player_n:
            st.session_state.player_name = player_n
            st.session_state.game_step = "story"
            st.rerun()
        else:
            st.warning("يرجى إدخال اسمك لبدء المهمة!")

# --- 2. القصة والتحقيق ---
elif st.session_state.game_step == "story":
    st.subheader("🚨 بلاغ عاجل: اختراق السيرفر المركزي")
    st.markdown(f"""
    <div class="story-box">
    المحقق <b>{st.session_state.player_name}</b>، استيقظنا اليوم على كارثة! 
    جميع درجات الطلاب في المدرسة تم تشفيرها وتحولت إلى رموز غريبة. 
    ترك المخترق رسالة غامضة تقول: "لن تستطيعوا الوصول لبياناتكم إلا إذا عرفتم من أنا!".<br><br>
    <b>الأدلة المتوفرة:</b><br>
    1. تم الدخول للنظام الساعة 3 فجراً من جهاز خارجي.<br>
    2. البصمة الرقمية تشير إلى شخص استخدم "كلمة مرور" ضعيفة جداً لأحد المعلمين.<br>
    3. وجدنا ملفاً مخفياً باسم "The_Shadow".
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🔍 من تعتقد أنه وراء الاختراق؟")
    suspect = st.selectbox("اختر المتهم الرئيسي:", ["طالب عبقري يريد تغيير درجاته", "مخترق خارجي (هاكر) يبحث عن فدية", "فيروس عشوائي بسبب رابط إعلاني"])
    
    if st.button("تأكيد المشتبه به"):
        st.session_state.suspect = suspect
        st.session_state.game_step = "solve"
        st.rerun()

# --- 3. المعالجة (الأسئلة التقنية) ---
elif st.session_state.game_step == "solve":
    st.header("🛠️ مرحلة التطهير والمعالجة")
    st.write(f"لقد عرفنا أن الجاني هو **{st.session_state.suspect}**. الآن يجب عليك معالجة النظام يا {st.session_state.player_name}!")
    
    st.write("---")
    st.write("**السؤال 1: الهاكر دخل عبر كلمة مرور المعلم. كيف نحمي الحساب الآن؟**")
    q1 = st.radio("اختر الحل:", ["تغيير كلمة المرور لـ (Jouri@2025#)", "حذف حساب المعلم", "إطفاء السيرفر"])
    
    st.write("**السؤال 2: وجدنا رابطاً خبيثاً هو سبب دخول الفيروس. ما هو الرابط الأخطر؟**")
    q2 = st.radio("اختر الرابط:", ["https://moe.gov.sa", "http://win-iphone-free.biz/login", "https://google.com"])
    
    if st.button("🛡️ تنفيذ أوامر التطهير"):
        if q1 == "تغيير كلمة المرور لـ (Jouri@2025#)" and q2 == "http://win-iphone-free.biz/login":
            st.session_state.game_step = "advice"
        else:
            st.error("فشلت المعالجة! بعض الثغرات لا تزال مفتوحة. حاول مرة أخرى.")
        st.rerun()

# --- 4. نصائح المحقق والتقييم ---
elif st.session_state.game_step == "advice":
    st.balloons()
    st.title("✅ تم استعادة النظام!")
    st.success(f"كفو يا {st.session_state.player_name}! لقد أنقذت المدرسة.")
    
    st.write("---")
    st.subheader("✍️ اكتب نصيحتك الأخيرة لزملائك لحمايتهم مستقبلاً:")
    user_advice = st.text_area("نصيحة المحقق:", placeholder="مثلاً: لا تفتحوا الروابط المجهولة...")
    
    if st.button("إرسال التقرير النهائي"):
        st.write("### 💻 تقييم نظام كود-قاتشر لنصيحتك:")
        if len(user_advice) > 10:
            st.info(f"نصيحتك ممتازة يا {st.session_state.player_name}! نظامنا يضيف عليها: 'تأكد دائماً من تفعيل التحقق الثنائي'.")
            st.markdown("### التقييم النهائي: محقق سيبراني من الدرجة الأولى 🎖️")
        else:
            st.warning("نصيحة قصيرة جداً، لكنها بداية جيدة!")
        
        st.markdown(f"<div style='text-align:center; color:#00FF41;'>المطورة المبدعة للمشروع: الجوري ✨</div>", unsafe_allow_html=True)
        if st.button("إعادة المهمة 🔄"):
            st.session_state.clear()
            st.rerun()
