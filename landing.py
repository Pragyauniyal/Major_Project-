import streamlit as st

def show_landing():

    st.set_page_config(layout="wide")

    # ===== CSS =====
    st.markdown("""
    <style>

    .main {
        background: #0b1220;
        color: white;
    }

    .title {
        text-align: center;
        font-size: 46px;
        font-weight: bold;
        color: #60a5fa;
        margin-top: 20px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 26px;
        margin-top: 40px;
        margin-bottom: 15px;
        font-weight: bold;
        color: #e5e7eb;
    }

    /* ===== FEATURE BOX ===== */
    .feature-box {
        background: linear-gradient(135deg, #111827, #1f2937);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #374151;
        transition: 0.4s;
        height: 260px;
        color: #e5e7eb;
    }

    .feature-box h3 {
        color: #60a5fa;
    }

    .feature-box li {
        color: #9ca3af;
        font-size: 14px;
    }

    .feature-box:hover {
        transform: scale(1.04);
        border: 1px solid #3b82f6;
        box-shadow: 0px 0px 35px rgba(59,130,246,0.6);
    }

    /* ===== SMALL BOX ===== */
    .mini-box {
        background: #111827;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #1f2937;
        text-align: center;
        transition: 0.3s;
    }

    .mini-box:hover {
        border: 1px solid #3b82f6;
        box-shadow: 0px 0px 20px rgba(59,130,246,0.3);
    }

    .highlight {
        background: linear-gradient(90deg,#3b82f6,#06b6d4);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin-bottom: 25px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ===== HEADER =====
    st.markdown("<div class='title'>🩺 Medi Scan AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>AI-powered disease detection, smart reports & health risk analysis</div>", unsafe_allow_html=True)

    # ===== HIGHLIGHT STRIP =====
    st.markdown("""
    <div class='highlight'>
    ⚡ Multi Disease Detection | Smart Reports | Real-Time Risk Analysis
    </div>
    """, unsafe_allow_html=True)

    # ===== LOGIN BUTTON =====
    if st.button("🔐 Login / Signup", use_container_width=True):
        st.session_state["page"] = "login"
        st.rerun()

    # ===== CORE FEATURES =====
    st.markdown("<div class='section-title'>🧠 Core AI Features</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='feature-box'>
        <h3>❤️ Cardio Intelligence</h3>
        <p>
        AI analyzes heart-related symptoms, blood pressure & lifestyle data 
        to detect cardiovascular risks early.
        </p>
        <ul>
        <li>✔ Heart disease prediction</li>
        <li>✔ Blood pressure insights</li>
        <li>✔ Early warning alerts</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
        <h3>🧠 Mental Health AI</h3>
        <p>
        Detect stress, anxiety & mental patterns using intelligent NLP models.
        </p>
        <ul>
        <li>✔ Stress detection</li>
        <li>✔ Anxiety analysis</li>
        <li>✔ Emotional insights</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature-box'>
        <h3>🫁 Pulmonary Scanner</h3>
        <p>
        Evaluate lung conditions and oxygen levels for respiratory risk analysis.
        </p>
        <ul>
        <li>✔ Lung disease detection</li>
        <li>✔ Oxygen monitoring</li>
        <li>✔ Breathing analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ===== WHAT SYSTEM DOES =====
    st.markdown("<div class='section-title'>🚀 What Medi Scan AI Does</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='mini-box'>⚡ Instant Disease Detection</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='mini-box'>📊 Smart Risk Analysis</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='mini-box'>📄 AI Medical Reports</div>", unsafe_allow_html=True)

    # ===== HOW IT WORKS =====
    st.markdown("<div class='section-title'>⚙️ How It Works</div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='mini-box'>1️⃣ Enter Symptoms</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='mini-box'>2️⃣ AI Processing</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='mini-box'>3️⃣ Risk Detection</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='mini-box'>4️⃣ Report Generation</div>", unsafe_allow_html=True)

    # ===== ABOUT =====
    st.markdown("<div class='section-title'>👨‍💻 About Project</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='mini-box'>
        <b>💡 Tech Stack</b><br><br>
        Python • Streamlit • AI Models • SQLite
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='mini-box'>
        <b>🎯 Goal</b><br><br>
        Early disease detection using AI & smart reporting
        </div>
        """, unsafe_allow_html=True)