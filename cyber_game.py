import streamlit as st
import time

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Cyber Mission: Jouri", page_icon="💻", layout="centered")

# التنسيق المتقدم (CSS) لإبهار اللجنة
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stButton > button { 
        width: 100%; border-radius: 5px; height: 3em; 
        background-color: transparent; color: #00FF41; 
        border: 1px solid #00FF41; font-family: 'Courier New', Courier, monospace;
    }
    .stButton > button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 15px #00FF41; }
    h1, h2, h3, p { color: #00FF41 !important; font-family: 'Courier New', Courier, monospace; }
    .stRadio > label { color: #00FF41 !important; font-size: 18px !important; }
    .warning { color: #FF0000; font-weight: bold; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة والقصة
if 'cyber_step' not in st.session_state:
    st.session_state.cyber_step = "intro"
if 'shield_power' not in st.session_state:
    st.session_state.shield_power = 100

# --- 1. القصة (المقدمة) ---
if st.session_state.cyber_step == "intro":
    st.markdown("<h1 style='text-align: center;'>💻 نظام الاختراق المتقدم</h1>", unsafe_allow_html=True)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=350)
    st.markdown("<p class='warning' style='text-align: center;'>⚠️ تحذير: تم اكتشاف فيروس يحاول سرقة ملفات المدرسة!</p>", unsafe_allow_html=True)
    st.write("---")
    st.write("المهمة: صد الهجمات السيبرانية وإعادة تأمين السيرفر الرئيسي.")
    st.write(f"المحققة المسؤولة: **الجوري**")
    
    if st.button("بدء عملية التطهير 🛡️"):
        st.session_state.cyber_step = "mission_1"
        st.rerun()

# --- 2. المهمة الأولى: الهندسة الاجتماعية ---
elif st.session_state.cyber_step == "mission_1":
    st.subheader("📡 المرحلة 1: هجوم انتحال الشخصية")
    st.info("تلقى أحد المعلمين رسالة بريد تقول: 'حدث خطأ في راتبك، ادخل بياناتك هنا'.")
    choice = st.radio("كيف تتصرفين يا جوري؟", 
                      ["تجاهل الرسالة وإبلاغ تقنية المعلومات", "الضغط على الرابط للتأكد", "إرسال البيانات بسرعة"])
    
    if st.button("تأمين الثغرة ⚔️"):
        if choice == "تجاهل الرسالة وإبلاغ تقنية المعلومات":
            st.success("تم صد الهجوم! أنتِ ذكية جداً.")
            time.sleep(1)
            st.session_state.cyber_step = "mission_2"
        else:
            st.error("خطأ! الفيروس بدأ بالتسلل..")
            st.session_state.shield_power -= 30
            st.session_state.cyber_step = "mission_2"
        st.rerun()

# --- 3. المهمة الثانية: كلمات المرور ---
elif st.session_state.cyber_step == "mission_2":
    st.subheader("🔐 المرحلة 2: محاولة كسر التشفير")
    st.write(f"قوة الدرع الحالي: {st.session_state.shield_power}%")
    st.write("الهاكر يحاول تخمين كلمة مرور مدير المدرسة.")
    choice = st.radio("أي وسيلة حماية ستفعلينها الآن؟", 
                      ["استخدام كلمة مرور سهلة", "تفعيل التحقق بخطوتين (MFA)", "تغيير اسم المستخدم فقط"])
    
    if st.button("تشفير البيانات 🔒"):
        if choice == "تفعيل التحقق بخطوتين (MFA)":
            st.success("تم عزل الهاكر بنجاح!")
            time.sleep(1)
            st.session_state.cyber_step = "final_boss"
        else:
            st.error("الهاكر اقترب من الملفات!")
            st.session_state.shield_power -= 40
            st.session_state.cyber_step = "final_boss"
        st.rerun()

# --- 4. المواجهة النهائية ---
elif st.session_state.cyber_step == "final_boss":
    st.subheader("👾 المواجهة النهائية: الفيروس العملاق")
    st.write("الفيروس يحاول الآن مسح قاعدة بيانات الغياب والدرجات!")
    choice = st.radio("ما هو الإجراء الأمني الأخير؟", 
                      ["فصل الجهاز عن الإنترنت وعمل نسخة احتياطية", "إطفاء الشاشة", "البكاء بجانب الحاسب"])
    
    if st.button("إنهاء التهديد 🔥"):
        if choice == "فصل الجهاز عن الإنترنت وعمل نسخة احتياطية":
            st.session_state.cyber_step = "victory"
        else:
            st.session_state.cyber_step = "game_over"
        st.rerun()

# --- شاشة النصر ---
elif st.session_state.cyber_step == "victory":
    st.balloons()
    st.title("🏆 تم إنقاذ المدرسة!")
    st.success(f"بفضل المحققة **الجوري**، النظام الآن آمن بنسبة 100%.")
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055687.png", width=200)
    if st.button("إعادة المهمة"):
        st.session_state.clear()
        st.rerun()

# --- شاشة الخسارة ---
elif st.session_state.cyber_step == "game_over":
    st.title("💀 تم اختراق النظام!")
    st.error("للأسف، الفيروس سيطر على الحاسب.")
    if st.button("محاولة الإنقاذ مرة أخرى"):
        st.session_state.clear()
        st.rerun()
