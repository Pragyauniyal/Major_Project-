import streamlit as st
from auth.login import login_user
from auth.register import register_user

def show_auth():

    # ===== CSS =====
    st.markdown("""
    <style>

    body {
        background-color: #0b1220;
    }

    .main {
        background: linear-gradient(180deg, #0b1220, #020617);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #e5e7eb;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        margin-bottom: 20px;
    }

    .form-box {
        background: #111827;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #1f2937;
        margin-top: 20px;
    }

    .section-title {
        font-size: 20px;
        margin-top: 15px;
        color: #e5e7eb;
    }

    .btn {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
    }

    </style>
    """, unsafe_allow_html=True)

    # ===== HEADER =====
    st.markdown("<div class='title'>🧠 Medi Scan</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Smart AI Powered Health System</div>", unsafe_allow_html=True)

    # ===== TABS =====
    tab1, tab2, tab3 = st.tabs([
    "🔐 Login",
    "🛡 Admin Login",
    "📄 Register"
])

    # ================= LOGIN =================
    # ================= LOGIN =================
    with tab1:

        st.markdown("<div class='form-box'>", unsafe_allow_html=True)

        st.markdown("### 🔐 Login")

        username = st.text_input("👤 Username", key="login_user")
        password = st.text_input("🔑 Password", type="password", key="login_pass")

        st.markdown("""
        <style>
        div.stButton > button {
            background: linear-gradient(90deg, #6366f1, #a855f7);
            color: white;
            border-radius: 10px;
            height: 45px;
            font-size: 16px;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("Login", use_container_width=True):

            user = login_user(username, password)

            if user:
                st.session_state["user"] = user[1]
                st.session_state["role"] = user[3]

                st.success("Login Success ✅")
                st.rerun()

            else:
                st.error("Invalid credentials ❌")


    # ================= ADMIN LOGIN =================
    with tab2:

        st.markdown("<div class='form-box'>", unsafe_allow_html=True)

        st.markdown("### 🛡 Admin Login")

        admin_user = st.text_input(
            "👤 Admin Username",
            key="admin_user"
        )

        admin_pass = st.text_input(
            "🔑 Admin Password",
            type="password",
            key="admin_pass"
        )

        if st.button("🛡 Login as Admin", use_container_width=True):

            user = login_user(admin_user, admin_pass)

            if user and user[3] == "admin":

                st.session_state["user"] = user[1]
                st.session_state["role"] = user[3]

                st.success("Admin Login Success ✅")
                st.rerun()

            else:
                st.error("Invalid Admin Credentials ❌")
        # 🔥 FORGOT PASSWORD BUTTON
        if st.button("🔑 Forgot Password", key="forgot_btn", use_container_width=True):
            st.session_state["page"] = "forgot"
            st.rerun() 

    # ================= REGISTER =================
    with tab3:

        st.markdown("<div class='form-box'>", unsafe_allow_html=True)

        st.markdown("### 📝 Create Account")

        username = st.text_input("👤 Username", key="reg_user")
        password = st.text_input("🔑 Password", type="password", key="reg_pass")

        role = st.selectbox("🎭 Role", ["user", "admin"], key="reg_role")

        st.markdown("### 🔒 Security Question")

        question = st.selectbox(
            "Select Question",
            ["Your first pet name?", "Your birth place?", "Your school name?"],
            key="reg_q"
        )

        answer = st.text_input("Answer", key="reg_ans")

        if st.button("✨ Create Account", use_container_width=True):
            msg = register_user(username, password, question, answer)
            st.success(msg)

        st.markdown("</div>", unsafe_allow_html=True)