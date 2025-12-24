import streamlit as st
import time

# إعدادات واجهة المستقبل
st.set_page_config(page_title="CODE-CATCHER AI", page_icon="⚡", layout="wide")

# تصميم الواجهة (نظام تشغيل سيبراني)
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #00FF41; }
    .status-bar { padding: 10px; background: #111; border: 1px solid #00FF41; border-radius: 5px; text-align: center; font-family: monospace; }
    .terminal-card { background: rgba(0, 255, 65, 0.05); border-right: 5px solid #00FF41; padding: 20px; margin: 10px 0; font-family: 'Courier New', monospace; }
    .stButton > button { background: black; color: #00FF41; border: 1px solid #00FF41; border-radius: 0px; font-weight: bold; height: 3em; transition: 0.5s; }
    .stButton > button:hover { background: #00FF41; color: black; box-shadow: 0 0 20px #00FF41; }
    .blink { animation: blinker 1s linear infinite; color: #FF0000; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة النظام
if 'system_status' not in st.session_state: st.session_state.system_status = "locked"
if 'threat_level' not in st.session_state: st.session_state.threat_level = 50

# --- 1. واجهة الدخول الأمنية ---
if st.session_state.system_status == "locked":
    st.markdown("<h1 style='text-align: center; letter-spacing: 5px;'>SYSTEM INITIALIZATION</h1>", unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", use_container_width=True)
        st.markdown("<p class='blink' style='text-align: center;'>⚠️ تنبيه: محاولة اختراق نشطة مكتشفة</p>", unsafe_allow_html=True)
        
        # تفعيل الصوت (موسيقى القضاء)
        st.write("🎵 **تفعيل بروتوكول الصوت (القضاء):**")
        st.audio("https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Yargi+Main+Theme&filename=mt/mtyzodm3nzm2mtyzody5_vj_2bl_2bjv_2bq2u.mp3")
        
        user = st.text_input("إدخال بصمة المحقق (الاسم):")
        if st.button("تأكيد الدخول السريع ⚡"):
            if user:
                st.session_state.user = user
                st.session_state.system_status = "story_mode"
                st.rerun()

# --- 2. القصة: سيناريو ساعة الصفر ---
elif st.session_state.system_status == "story_mode":
    st.markdown(f"<h3>📂 التقرير السري: عملية الظل العكسي</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='terminal-card'>
    المحقق <b>{st.session_state.user}</b>، نحن لا نواجه هاكر عادي.. نحن نواجه "ذكاء اصطناعي متمرد"! <br><br>
    لقد تم اختراق نظام التحكم في الإضاءة والشبكة داخل المدرسة. الكاميرات تم توجيهها نحو الحائط، 
    وتم قفل الأبواب الذكية على المعلمات بالداخل! <br><br>
    الهاكر أرسل شيفرة ثنائية (Binary) تقول: "المدرسة ستظل مظلمة حتى يتم تسليم شيفرة فك التشفير الرئيسية". <br>
    الخطر الآن ليس فقط الدرجات، بل أمن كل شخص داخل المبنى.<br><br>
    <b>مهمتك:</b> اختراق "سيرفر الهاكر" نفسه وتعطيل القنبلة الرقمية قبل انفجار جدار الحماية الأخير.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("بدء عملية الاقتحام الرقمي 🔓"):
        st.session_state.system_status = "mission_control"
        st.rerun()

# --- 3. المهمة: لوحة التحكم التفاعلية ---
elif st.session_state.system_status == "mission_control":
    st.markdown(f"<h2>🛠️ غرفة العمليات السيبرانية - القائد {st.session_state.user}</h2>", unsafe_allow_html=True)
    
    # عداد الخطر
    st.write(f"مستوى التهديد الحالي: {st.session_state.threat_level}%")
    st.progress(st.session_state.threat_level)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='terminal-card'><b>[الثغرة 1]</b><br>تلقيتِ إشارة من جهاز المعلمة 'هند'. الجهاز يرسل بيانات لموقع مجهول.</div>", unsafe_allow_html=True)
        choice1 = st.selectbox("الإجراء:", ["تنسيق القرص الصلب", "تفعيل نظام IPS لعزل الاتصال", "تجاهل الإشارة"])
        
        st.markdown("<div class='terminal-card'><b>[الثغرة 2]</b><br>الهاكر يحاول الدخول عبر منفذ (Port 8080).</div>", unsafe_allow_html=True)
        choice2 = st.selectbox("الإجراء:", ["إغلاق المنافذ غير المستخدمة", "تغيير كلمة مرور الواي فاي", "فتح جميع المنافذ للفخ"])

    with col2:
        st.markdown("<div class='terminal-card'><b>[الثغرة 3]</b><br>وجدتِ رسالة مشفرة: '74-68-65-20-63-6f-64-65'.</div>", unsafe_allow_html=True)
        choice3 = st.selectbox("تحليل الشيفرة:", ["هجوم تخميني", "تشفير Hexadecimal", "رقم جوال الهاكر"])

        st.markdown("<div class='terminal-card'><b>[الثغرة 4]</b><br>الهاكر يهدد بنشر صور الطلاب.</div>", unsafe_allow_html=True)
        choice4 = st.selectbox("رد الفعل:", ["التفاوض مع الهاكر", "تفعيل بروتوكول الحماية القصوى (Encryption)", "إغلاق الكهرباء"])

    if st.button("🚀 إرسال حزمة الإصلاح النهائية"):
        # منطق النجاح (إجابات تقنية دقيقة)
        score = 0
        if choice1 == "تفعيل نظام IPS لعزل الاتصال": score += 25
        if choice2 == "إغلاق المنافذ غير المستخدمة": score += 25
        if choice3 == "تشفير Hexadecimal": score += 25
        if choice4 == "تفعيل بروتوكول الحماية القصوى (Encryption)": score += 25
        
        st.session_state.threat_level = 100 - score
        if score >= 75:
            st.session_state.system_status = "success"
        else:
            st.error("❌ فشل البروتوكول! مستوى التهديد ارتفع. حاول مجدداً قبل فوات الأوان.")
        st.rerun()

# --- 4. النجاح والتقييم الذكي ---
elif st.session_state.system_status == "success":
    st.balloons()
    st.markdown("<h1 style='color: gold !important; text-align: center;'>🏆 MISSION ACCOMPLISHED</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='terminal-card'>تم القضاء على التهديد بنجاح. المحققة {st.session_state.user}، لقد أنقذتِ المدرسة من كارثة حقيقية. تم القبض على الهاكر وتأمين السيرفرات.</div>", unsafe_allow_html=True)
    
    st.write("---")
    advice = st.text_area("✍️ بصفتكِ خبيرة AI، اكتبي نصيحة للمستقبل:")
    if st.button("إغلاق القضية 📝"):
        st.success("تم تحليل نصيحتكِ وحفظها في قاعدة بيانات الأمن الوطني.")
        st.markdown(f"<h3 style='text-align:center;'>تمت البرمجة بواسطة AI للجوري ✨</h3>", unsafe_allow_html=True)
        if st.button("بدء محاكاة جديدة"):
            st.session_state.clear()
            st.rerun()
