import streamlit as st
import time
import random

# إعدادات الشاشة الكاملة
st.set_page_config(page_title="CODE BREAKER: CYBER HEIST", page_icon="⛔", layout="wide")

# CSS المتقدم: خلفية هكر متحركة، تأثيرات Glitch، خطوط تيرمينال
st.markdown(
    """
    <style>
    /* خلفية الماتريكس المتحركة */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.95), rgba(0,0,0,0.95)), url('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjV6aTFtZTRtZmNzbW5mdjFkY2N6d3B4cDhqZ2Z5ZnU4OWJ2OWwyaSZlcD12MV9pbnRlcm5uYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKSjPqcKGRZaO3u/giphy.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    /* الألوان والخطوط */
    h1, h2, h3, p, label, .stMarkdown { color: #00FF41 !important; font-family: 'Share Tech Mono', monospace; text-shadow: 0 0 8px rgba(0,255,65,0.7); }
    /* زر التفاعل */
    .stButton > button { 
        width: 100%; border: 2px solid #00FF41; background-color: rgba(0,255,65,0.1); color: #00FF41; 
        font-size: 20px; font-weight: bold; transition: 0.5s; height: 65px; border-radius: 5px;
        box-shadow: 0 0 15px rgba(0,255,65,0.5);
    }
    .stButton > button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 40px #00FF41; transform: translateY(-3px); }
    /* مربعات القصة والتحقيق */
    .story-card { 
        background-color: rgba(10,10,10,0.9); border: 1px solid #00FF41; border-left: 5px solid #00FF41; 
        padding: 25px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,255,65,0.3);
        line-height: 1.8; font-size: 17px; direction: rtl; text-align: right;
    }
    /* مؤثرات الهاكينج */
    .hacked-text { color: #FF0000; font-weight: bold; animation: glitch 0.5s linear infinite alternate; }
    @keyframes glitch { 0% { text-shadow: 1px 0 red, -1px 0 blue; opacity: 0.8; } 100% { text-shadow: -1px 0 red, 1px 0 blue; opacity: 1; } }
    /* خطوط الإدخال */
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00FF41; border: 1px solid #00FF41; font-family: monospace; }
    /* العد التنازلي */
    .timer-display { font-size: 3em; color: #FFFF00; text-align: center; margin-bottom: 20px; font-family: 'Press Start 2P', cursive; text-shadow: 0 0 15px #FFFF00; }
    </style>
    """, unsafe_allow_html=True
)

# إدارة حالة اللعبة والتقدم
if 'game_state' not in st.session_state: st.session_state.game_state = "init"
if 'player_id' not in st.session_state: st.session_state.player_id = ""
if 'hack_level' not in st.session_state: st.session_state.hack_level = 0
if 'timer_start' not in st.session_state: st.session_state.timer_start = 0

# --- وظيفة محاكاة "تساقط الرموز" ---
def display_falling_code():
    if random.random() < 0.7: # احتمال ظهور الرموز
        st.markdown(f"<p style='color: rgba(0,255,65,{random.uniform(0.1, 0.5)}); font-size: {random.randint(10, 30)}px; position: absolute; left: {random.randint(0,100)}vw; top: {random.randint(0,100)}vh;'>{chr(random.randint(33,126))}</p>", unsafe_allow_html=True)
        
# --- المرحلة 1: التهيئة وبدء الموسيقى ---
if st.session_state.game_state == "init":
    st.markdown("<h1 class='hacked-text' style='text-align: center;'>⛔ نظام CODE BREAKER: سرقة البيانات الكبرى</h1>", unsafe_allow_html=True)
    st.image("https://r2.erweima.ai/i/6DAnC4M_S2m4_wS_Y1A5pA.png", width=500)
    
    st.warning("⚠️ تنبيه: يرجى تشغيل موسيقى القضية أدناه لتجربة غامرة.")
    st.audio("https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Yargi+Main+Theme&filename=mt/mtyzodm3nzm2mtyzody5_vj_2bl_2bjv_2bq2u.mp3")
    
    st.write("الكون الرقمي ينهار! تحتاجنا الآن أكثر من أي وقت مضى.")
    player_name = st.text_input("رمز تعريف المحقق (اسمك):")
    if st.button("تفعيل بروتوكول الكود-بريكر ⚡"):
        if player_name:
            st.session_state.player_id = player_name
            st.session_state.game_state = "chapter1"
            st.session_state.timer_start = time.time()
            st.rerun()

# --- المرحلة 2: الفصل الأول (قصة الكارثة) ---
elif st.session_state.game_state == "chapter1":
    st.markdown(f"<h2>📜 ملف سري للغاية: الفصل الأول - سقوط جدار أريحا</h2>", unsafe_allow_html=True)
    current_time_display = 180 - int(time.time() - st.session_state.timer_start)
    if current_time_display <= 0:
        st.session_state.game_state = "game_over"
        st.rerun()
    st.markdown(f"<div class='timer-display'>العد التنازلي: {current_time_display} ثانية</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="story-card">
    المحقق <b>{st.session_state.player_id}</b>، لقد أعلنا حالة الطوارئ القصوى. 
    عند الساعة 04:00 فجراً، استقبلت جميع الشاشات في العالم رسالة واحدة: <br>
    <code class="hacked-text">"SYSTEM OF ALL IS NOW MINE. ALL DATA BELONGS TO THE SHADOW. FILE: GRADES_DB.ENC"</code> <br><br>
    نظامنا المركزي ليس مخترقاً فحسب، بل تم اختطافه بالكامل! 
    <b>(الظل)</b>، وهو كيان رقمي غامض، شفر مليارات البيانات حول العالم، وبدأ بنظامكم التعليمي. 
    يطلب منا تسليم "الشيفرة الذهبية" (Golden Key) وهي مفتاح فك تشفير كل بيانات العالم. 
    إذا لم نفعل، سيدمر كل شيء خلال 3 دقائق.<br><br>
    لقد ترك لنا تلميحاً غامضاً: "البوابة الأولى هي حيث تبدأ كل رحلة.. ابحثوا عن الضعف في أول نقطة اتصال". 
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("دخول منطقة الاختراق ⚠️"):
        st.session_state.game_state = "chapter2"
        st.rerun()

# --- المرحلة 3: الفصل الثاني (تحليل الاختراق والأسئلة) ---
elif st.session_state.game_state == "chapter2":
    st.markdown(f"<h2>🔬 تحليل الاختراق: البحث عن الثغرات</h2>", unsafe_allow_html=True)
    current_time_display = 180 - int(time.time() - st.session_state.timer_start)
    if current_time_display <= 0:
        st.session_state.game_state = "game_over"
        st.rerun()
    st.markdown(f"<div class='timer-display'>الوقت المتبقي: {current_time_display} ثانية</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="story-card">
    لقد تتبعنا إشارة <b>الظل</b>. نقطة الدخول كانت عبر بريد إلكتروني لمعلمة للرياضيات. 
    الرسالة كانت بعنوان: <code class="hacked-text">'فائزة بجائزة آبل لعام 2024!'</code>.<br><br>
    <b>السؤال الأول:</b> الهاكر استخدم تقنية 'التزييف' لجعل الإيميل يبدو حقيقياً. أي من التواقيع التالية تكشف أن الإيميل مزيف؟
    </div>
    """, unsafe_allow_html=True)
    q1 = st.radio("اختيارك:", ["الرسالة مرسلة من Apple.com.sa", "الرسالة تحتوي على رابط http://apple.prize-win.xyz", "الرسالة فيها صور كثيرة"])

    st.markdown(f"""
    <div class="story-card">
    <b>السؤال الثاني:</b> بعد فتح الرابط، تم تحميل برنامج خبيث على جهاز المعلمة. 
    البرنامج بدأ بإنشاء ملفات وهمية لإخفاء نفسه. ما هو نوع هذا الهجوم؟
    </div>
    """, unsafe_allow_html=True)
    q2 = st.radio("اختيارك:", ["هجوم DDoS", "فيروس حصان طروادة (Trojan Horse)", "هجوم التصيد (Phishing)"])

    if st.button("تحليل البيانات واكتشاف الخطوة التالية 🔎"):
        if q1 == "الرسالة تحتوي على رابط http://apple.prize-win.xyz" and q2 == "فيروس حصان طروادة (Trojan Horse)":
            st.session_state.hack_level += 2
            st.session_state.game_state = "chapter3"
        else:
            st.error("❌ فشل التحليل! الهاكر تقدم خطوة. ابحثي عن المزيد من الأدلة.")
        st.rerun()

# --- المرحلة 4: الفصل الثالث (فك الشفرات والأسئلة) ---
elif st.session_state.game_state == "chapter3":
    st.markdown(f"<h2>🔐 فك الشفرات: الوصول لقلب الهاكر</h2>", unsafe_allow_html=True)
    current_time_display = 180 - int(time.time() - st.session_state.timer_start)
    if current_time_display <= 0:
        st.session_state.game_state = "game_over"
        st.rerun()
    st.markdown(f"<div class='timer-display'>الوقت المتبقي: {current_time_display} ثانية</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="story-card">
    لقد وصلنا إلى جهازه! لكنه محمي بـ 7 طبقات من التشفير. 
    وجدنا هذه الرسالة: <code class="hacked-text">"74 68 65 20 73 68 61 64 6f 77"</code>. 
    هذه شيفرة مفتاح الخادم الرئيسي! <br><br>
    <b>السؤال الثالث:</b> ما نوع هذا التشفير، وماذا تعني هذه الشيفرة باللغة الإنجليزية؟ (تلميح: هذه شيفرة نظام قديم).
    </div>
    """, unsafe_allow_html=True)
    q3 = st.radio("اختيارك:", ["ASCII Hexadecimal تعني 'the shadow'", "Base64 تعني 'my secret'", "MD5 Hash لا يمكن فكها"])

    st.markdown(f"""
    <div class="story-card">
    <b>السؤال الرابع:</b> لقد حددنا موقعه الجغرافي. إنه يستخدم شبكة 'واي فاي عامة' في مقهى. ما هو البروتوكول الأمني الذي يجب تفعيله فوراً لحماية نفسك في شبكات الواي فاي العامة؟
    </div>
    """, unsafe_allow_html=True)
    q4 = st.radio("اختيارك:", ["استخدام VPN (الشبكة الافتراضية الخاصة)", "تغيير اسم المستخدم", "إيقاف جدار الحماية"])

    if st.button("الخطوة الأخيرة: ضربة القضاء الرقمية 💥"):
        if q3 == "ASCII Hexadecimal تعني 'the shadow'" and q4 == "استخدام VPN (الشبكة الافتراضية الخاصة)":
            st.session_state.hack_level += 2
            st.session_state.game_state = "victory"
        else:
            st.error("❌ لا! الهاكر يغير موقعه! حان وقت التدخل العنيف.")
        st.rerun()

# --- المرحلة 5: النصر أو الخسارة ---
elif st.session_state.game_state == "victory":
    st.balloons()
    st.markdown(f"<h1 style='color: gold; text-align: center;'>🏆 انتصار المحققة {st.session_state.player_id}: تم إسقاط الظل!</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="story-card" style="border-color: gold;">
    بفضل ذكائكِ الخارق، تم تتبع (الظل)، فك تشفيره، والقبض عليه! <br>
    جميع البيانات تم استعادتها، وتم تأمين الشبكة العالمية. 
    لقد أثبتِّ أن العقل البشري، مع المعرفة الصحيحة، أقوى من أي ذكاء اصطناعي متمرد.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📝 تقرير القضاء النهائي والتوصيات المستقبلية:")
    final_report = st.text_area("اكتبي ملخصك الأمني وتوصياتك للأجيال القادمة (بصفتك الخبيرة العالمية):")
    
    if st.button("إغلاق الملف وتأكيد النصر 🎖️"):
        st.markdown(f"<p class='hacked-text'>جاري تحليل تقرير المحققة {st.session_state.player_id} بواسطة نظام CODE-CATCHER AI...</p>", unsafe_allow_html=True)
        time.sleep(2)
        st.success("✅ تحليل ممتاز! تم منحكِ رتبة 'الخبير السيبراني الأعلى'!")
        st.markdown(f"<h3 style='text-align: center;'>تحفة برمجية من إبداع: الجوري ✨</h3>", unsafe_allow_html=True)
        if st.button("بدء مهمة جديدة 🔄"):
            st.session_state.clear()
            st.rerun()

elif st.session_state.game_state == "game_over":
    st.markdown("<h1 class='hacked-text' style='text-align: center;'>❌ فشل النظام: لقد دُمرت البيانات!</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjV6aTFtZTRtZmNzbW5mdjFkY2N6d3B4cDhqZ2Z5ZnU4OWJ2OWwyaSZlcD12MV9pbnRlcm5uYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKSjPqcKGRZaO3u/giphy.gif", use_container_width=True)
    st.error(f"للأسف يا {st.session_state.player_id}، الهاكر كان أسرع. جميع البيانات تم مسحها.")
    if st.button("إعادة محاولة الإنقاذ 🔄"):
        st.session_state.clear()
        st.rerun()
