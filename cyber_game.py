import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Code Catcher: The Investigation", page_icon="🕵️‍♂️", layout="centered")

# التنسيق البصري (أسود وأخضر هاكرز)
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #00FF41 !important; font-family: 'Courier New', monospace; }
    .stButton > button { width: 100%; background-color: transparent; color: #00FF41; border: 2px solid #00FF41; border-radius: 10px; font-weight: bold; }
    .stButton > button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 20px #00FF41; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00FF41; border: 1px solid #00FF41; }
    .story-box { padding: 15px; border: 1px solid #00FF41; border-radius: 10px; background-color: #0d0d0d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة مراحل اللعبة
if 'step' not in st.session_state:
    st.session_state.step = "welcome"

# --- المرحلة 1: الترحيب والاسم ---
if st.session_state.step == "welcome":
    st.markdown("<h1>🕵️‍♂️ أهلاً بك في عالم كود-قاتشر</h1>", unsafe_allow_html=True)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=300)
    st.write("من هُنا تبدأ رحلتك في عالم الأمن السيبراني..")
    
    p_name = st.text_input("أدخل اسمك أيها المحقق الرقمي:", key="name_input")
    if st.button("🚀 ابدأ الآن"):
        if p_name:
            st.session_state.p_name = p_name
            st.session_state.step = "story"
            st.rerun()
        else:
            st.error("لازم تكتب اسمك عشان نبدأ المهمة!")

# --- المرحلة 2: القصة والتحقيق ---
elif st.session_state.step == "story":
    st.markdown(f"<h3>🚨 بلاغ اختراق عاجل يا {st.session_state.p_name}!</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="story-box">
    لقد تم اختراق نظام المدرسة الساعة 3 فجراً! الدرجات مشفرة، والهاكر ترك رسالة غامضة باسم <b>(The Shadow)</b>. 
    الدلائل تقول أن الهاكر استخدم "رابط تصيد" أرسله لأحد المعلمين.<br><br>
    <b>مهمتك الآن:</b> معرفة من الفاعل وتطهير النظام!
    </div>
    """, unsafe_allow_html=True)
    
    suspect = st.selectbox("من تعتقد أنه المخترق؟", ["طالب عبقري يريد تعديل درجاته", "هاكر مجهول يطلب فدية", "فيروس عشوائي"])
    if st.button("تأكيد المتهم 🔍"):
        st.session_state.suspect = suspect
        st.session_state.step = "solve"
        st.rerun()

# --- المرحلة 3: الأسئلة والمعالجة ---
elif st.session_state.step == "solve":
    st.markdown("<h3>🛠️ مرحلة المعالجة الفنية</h3>", unsafe_allow_html=True)
    st.write(f"المتهم هو {st.session_state.suspect}. لنبدأ بإغلاق الثغرات:")
    
    q1 = st.radio("1. الهاكر استخدم كلمة مرور ضعيفة، ما هي الأقوى؟", ["Jouri123", "J@o#u$R%i_2025", "12345678"])
    q2 = st.radio("2. ما هو الرابط الذي تسبب في الاختراق؟", ["google.com", "moe.gov.sa", "free-games-hack.xyz"])
    
    if st.button("تطهير النظام 🔥"):
        if q1 == "J@o#u$R%i_2025" and q2 == "free-games-hack.xyz":
            st.success("تم التطهير بنجاح! أنت محقق أسطوري.")
            st.session_state.step = "advice"
        else:
            st.error("للأسف، النظام لا يزال مخترقاً! حاول مرة أخرى.")
        st.rerun()

# --- المرحلة 4: النصيحة والتقييم ---
elif st.session_state.step == "advice":
    st.balloons()
    st.markdown("<h1>🏆 تم إنقاذ النظام!</h1>", unsafe_allow_html=True)
    st.write(f"كفو يا {st.session_state.p_name}! المدرسة فخورة بك.")
    
    st.write("---")
    st.write("بصفتك محققاً، اكتب نصيحة للأمان السيبراني لزملائك:")
    advice = st.text_area("نصيحة المحقق:", placeholder="اكتب نصيحتك هنا...")
    
    if st.button("إرسال التقرير النهائي"):
        st.write("### 💻 تقييم المحققة الجوري لنصيحتك:")
        if len(advice) > 10:
            st.success("تقييم ممتاز! نصيحة احترافية ومفيدة جداً.")
        else:
            st.warning("نصيحة جيدة، لكن يفضل أن تكون أكثر تفصيلاً.")
        
        st.markdown("<br><hr><center>تطوير المبدعة: الجوري ✨</center>", unsafe_allow_html=True)
        if st.button("إعادة المهمة 🔄"):
            st.session_state.step = "welcome"
            st.rerun()
