
#     st.warning("⚠️ Login First")
import streamlit as st
import pandas as pd
import sqlite3

from agents.cardio import cardio_agent
from agents.psycho import psycho_agent
from agents.pulmo import pulmo_agent
from utils.preprocess import clean_text
from pdf_utils import build_pdf_bytes

from auth.login import login_user
from auth.register import register_user
from database import *
from database import reset_admin

from auth_ui import show_auth
# ===== INIT =====
create_db()
create_admin()
reset_admin()

# ===== SESSION =====
if "user" not in st.session_state:
    st.session_state["user"] = None
    st.session_state["role"] = None
from landing import show_landing

if st.session_state.get("page") != "login" and st.session_state["user"] is None:
    show_landing()
    st.stop()
# =========================
# 🔐 LOGIN / REGISTER / FORGOT
# =========================

# ===== FORGOT PASSWORD =====
if st.session_state.get("page") == "forgot":

    st.title("🔑 Reset Password")

    username = st.text_input("Enter Username", key="forgot_username")
    new_pass = st.text_input("New Password", type="password", key="forgot_password")

    if st.button("Get Question", key="get_q"):
        user = get_user_by_username(username)

        if user:
            st.session_state["reset_user"] = user
        else:
            st.error("User not found")

    if "reset_user" in st.session_state:
        user = st.session_state["reset_user"]

        st.write("Question:", user[4])

        answer = st.text_input("Answer")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Reset Password", key="reset_pass"):
            if answer == user[5]:
                update_password(username, new_pass)
                st.success("Password Updated ✅")
                st.session_state["page"] = "login"
                st.rerun()
            else:
                st.error("Wrong Answer ❌")

# ===== LOGIN PAGE =====
elif st.session_state["user"] is None:

    show_auth()   # 👈 बस ये डालना है
    st.stop()     # 👈 बहुत important (dashboard run nahi hoga)
    # ================= USER LOGIN =================
    with tab1:
        u = st.text_input("Username", key="user_login_username")
        p = st.text_input("Password", type="password", key="user_login_password")

        if st.button("Login User", key="login_user_btn"):
            user = login_user(u, p)
            if user and user[3] == "user":
                st.session_state["user"] = user[1]
                st.session_state["role"] = user[3]
                st.rerun()
            else:
                st.error("Invalid")

        if st.button("Forgot Password", key="forgot_btn"):
            st.session_state["page"] = "forgot"
            st.rerun()

    # ================= ADMIN LOGIN =================
    with tab2:
        u = st.text_input("Admin Username", key="admin_login_username")
        p = st.text_input("Admin Password", type="password", key="admin_login_password")

        if st.button("Login Admin", key="login_admin_btn"):
            user = login_user(u, p)
            if user and user[3] == "admin":
                st.session_state["user"] = user[1]
                st.session_state["role"] = user[3]
                st.rerun()
            else:
                st.error("Invalid Admin")

    # ================= REGISTER =================
    with tab3:
        u = st.text_input("Username", key="register_username")
        p = st.text_input("Password", type="password", key="register_password")

        question = st.selectbox("Security Question", [
            "Your pet name?",
            "Your birth place?",
            "Your school name?"
        ], key="register_question")

        answer = st.text_input("Answer", key="register_answer")

        if st.button("Register", key="register_btn"):
            st.success(register_user(u, p, question, answer))


# ================= DASHBOARD (AFTER LOGIN) =================
else:

    # ===== ADMIN PANEL =====
    if st.session_state["role"] == "admin":

        admin_menu = st.sidebar.radio(
            "Admin Menu",
            ["Dashboard", "Search / Manage", "All Reports", "Manage Users", "Settings"]
        )

        # ===== DASHBOARD =====
        if admin_menu == "Dashboard":

            st.title("📊 Admin Dashboard — Analytics")

            reports = get_all_reports()
            users = get_all_users()

            col1, col2, col3, col4 = st.columns(4)

            total_reports = len(reports)
            total_users = len(users)

            high = medium = low = 0

            for r in reports:
                text = str(r)

                if "High" in text:
                    high += 1
                elif "Medium" in text:
                    medium += 1
                else:
                    low += 1

            col1.metric("📄 Total Reports", total_reports)
            col2.metric("👥 Total Users", total_users)
            col3.metric("⚠️ High Risk", high)
            col4.metric("🟢 Low Risk", low)

            st.divider()

            # ===== RISK =====
            st.subheader("⚠️ Risk Distribution")

            risk_df = pd.DataFrame({
                "Risk": ["Low", "Medium", "High"],
                "Count": [low, medium, high]
            })

            st.bar_chart(risk_df.set_index("Risk"))

            st.divider()

            # ===== DISEASE =====
            st.subheader("🦠 Disease Distribution")

            cardio = psycho = pulmo = 0

            for r in reports:
                t = str(r).lower()

                if "heart" in t: cardio += 1
                if "mental" in t: psycho += 1
                if "lung" in t: pulmo += 1

            disease_df = pd.DataFrame({
                "Disease": ["Heart", "Mental", "Lungs"],
                "Count": [cardio, psycho, pulmo]
            })

            st.bar_chart(disease_df.set_index("Disease"))

            st.divider()

            # ===== DISEASE =====
            st.subheader("🦠 Disease Distribution")

            cardio = psycho = pulmo = 0

            for r in reports:
                t = str(r).lower()

                if "heart" in t: cardio += 1
                if "mental" in t: psycho += 1
                if "lung" in t: pulmo += 1

            disease_df = pd.DataFrame({
                "Disease": ["Heart", "Mental", "Lungs"],
                "Count": [cardio, psycho, pulmo]
            })

            st.bar_chart(disease_df.set_index("Disease"))

            st.divider()

            # ===== RECENT =====
            st.subheader("🕒 Recent Activity")

            for r in reports[-5:]:
                st.write(f"👤 {r[1]} submitted a report")

            st.divider()

            st.success("✅ Server Running")
            st.success("✅ Database Connected")
            st.info("ℹ️ Real-time Analytics Enabled")


        # ===== SEARCH / MANAGE =====
        elif admin_menu == "Search / Manage":

            st.title("🔍 Search Reports")

            keyword = st.text_input("Search by username or report", key="search1")

            reports = get_all_reports()

            found = False

            for r in reports:
                if keyword.lower() in str(r).lower():
                    st.write("------")
                    st.write(f"🆔 ID: {r[0]}")
                    st.write(f"👤 User: {r[1]}")
                    st.write(f"📄 Report: {r[2]}")
                    st.write(f"❤️ Cardio: {r[3]}")
                    st.write(f"🧠 Psycho: {r[4]}")
                    st.write(f"🫁 Pulmo: {r[5]}")
                    found = True

            if keyword and not found:
                st.warning("No results found")

        # ===== ALL REPORTS =====
        if admin_menu == "All Reports":

            st.title("📄 All Reports")

            reports = get_all_reports()

            for r in reports:

                st.write("------")
                st.write(f"🆔 ID: {r[0]}")
                st.write(f"👤 User: {r[1]}")
                st.write(f"📄 Report: {r[2]}")
                st.write(f"❤️ Cardio: {r[3]}")
                st.write(f"🧠 Psycho: {r[4]}")
                st.write(f"🫁 Pulmo: {r[5]}")

                col1, col2 = st.columns(2)

                with col1:
                    st.download_button(
                        "⬇ Download",
                        data=r[2],
                        file_name=f"report_{r[0]}.txt",
                        key=f"download_{r[0]}"
                    )

                with col2:
                    if st.button("🗑 Delete", key=f"delete_{r[0]}"):
                        delete_report(r[0])
                        st.success("Deleted Successfully")
                        st.rerun()

        # ===== USERS =====
        elif admin_menu == "Manage Users":

            st.title("👥 Manage Users")

            users = get_all_users()

            for u in users:
                st.write("------")
                st.write(f"ID: {u[0]} | Username: {u[1]} | Role: {u[2]}")

        # ===== SETTINGS =====
        elif admin_menu == "Settings":

            st.title("⚙️ Admin Settings")

            new_pass = st.text_input("New Admin Password", type="password", key="admin_pass")

            if st.button("Update Password"):

                conn = sqlite3.connect("medi_ai.db")
                cursor = conn.cursor()

                cursor.execute(
                    "UPDATE users SET password=? WHERE username='admin'",
                    (new_pass,)
                )

                conn.commit()
                conn.close()

                st.success("Password Updated Successfully")
 # ================= USER PANEL =================
# ================= USER PANEL =================
   # ================= USER PANEL =================
    else:

        menu = st.sidebar.radio(
            "User Menu",
            ["AI Assistant", "Generate Report", "My Reports", "Profile"]
        )

        # ===== AI ASSISTANT =====
        if menu == "AI Assistant":

            # ===== WELCOME HEADER =====
            st.markdown("""
            <div style="
                background: linear-gradient(90deg,#1e293b,#0f172a);
                padding:20px;
                border-radius:12px;
                border:1px solid #334155;
                margin-bottom:20px;
            ">
                <h2 style="margin:0;">🤖 Smart AI Assistant</h2>
                <p style="color:#94a3b8;">Analyze your symptoms and get instant AI insights</p>
            </div>
            """, unsafe_allow_html=True)

            # ===== CARDS =====
            col1, col2, col3 = st.columns(3)

            col1.markdown("""<div style="background:#111827;padding:15px;border-radius:10px;">❤️ <b>Cardio AI</b><br>Detect heart-related risks instantly</div>""", unsafe_allow_html=True)
            col2.markdown("""<div style="background:#111827;padding:15px;border-radius:10px;">🧠 <b>Psycho AI</b><br>Analyze mental health & stress</div>""", unsafe_allow_html=True)
            col3.markdown("""<div style="background:#111827;padding:15px;border-radius:10px;">🫁 <b>Pulmo AI</b><br>Lung & breathing analysis</div>""", unsafe_allow_html=True)

            st.divider()

            # ===== INPUT =====
            st.subheader("📝 Enter Symptoms")

            text = st.text_area("Describe symptoms with age", height=120, key="ai_input")

            # ===== BUTTON STYLE =====
            st.markdown("""
            <style>
            div.stButton > button {
                background: linear-gradient(90deg,#6366f1,#9333ea);
                color:white;
                border-radius:8px;
                height:45px;
                font-size:16px;
            }
            </style>
            """, unsafe_allow_html=True)

            # ===== ANALYZE =====
            if st.button("🚀 Analyze Now", use_container_width=True):

                if text.strip() == "":
                    st.warning("⚠️ Please enter symptoms")
                else:
                    clean = clean_text(text)

                    c = cardio_agent(clean)
                    p = psycho_agent(clean)
                    l = pulmo_agent(clean)

                    st.subheader("📊 AI Results")

                    r1, r2, r3 = st.columns(3)
                    r1.success(f"❤️ Cardio\n\n{c}")
                    r2.info(f"🧠 Psycho\n\n{p}")
                    r3.warning(f"🫁 Pulmo\n\n{l}")

                    risk = "Low"

                    if "high" in str(c).lower() or "high" in str(p).lower() or "high" in str(l).lower():
                        risk = "High"
                    elif "moderate" in str(c).lower() or "stress" in str(p).lower():
                        risk = "Medium"

                    st.subheader("🚨 Overall Risk")

                    if risk == "High":
                        st.error("🔴 HIGH RISK")
                    elif risk == "Medium":
                        st.warning("🟡 MEDIUM RISK")
                    else:
                        st.success("🟢 LOW RISK")


        # ===== GENERATE REPORT =====
        elif menu == "Generate Report":
            # ===== STYLING =====
            st.markdown("""
            <style>
            .section-box {
                background: #0f172a;
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #334155;
                margin-bottom: 20px;
            }
            .section-title {
                font-size: 20px;
                margin-bottom: 10px;
                color: #38bdf8;
            }
            </style>
            """, unsafe_allow_html=True)

            # ===== HEADER =====
            st.markdown("""
            <div style="
                background: linear-gradient(90deg,#1e293b,#0f172a);
                padding:20px;
                border-radius:12px;
                border:1px solid #334155;
                margin-bottom:20px;
            ">
                <h2>📊 Generate Smart Medical Report</h2>
                <p style="color:#94a3b8;">Fill your health details for AI-based diagnosis</p>
            </div>
            """, unsafe_allow_html=True)

            # ===== PATIENT =====
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">👤 Patient Info</div>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                name = st.text_input("Name")
            with col2:
                age = st.number_input("Age", 0, 120)
            with col3:
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])

            st.markdown('</div>', unsafe_allow_html=True)

            # ===== PARAMETERS =====
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🩺 Health Parameters</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                glucose = st.number_input("Glucose", 0, 500)
                bp = st.number_input("Blood Pressure", 0, 200)
                heart_rate = st.number_input("Heart Rate", 0, 200)
                cholesterol = st.number_input("Cholesterol", 0, 400)

            with col2:
                bmi = st.number_input("BMI", 0.0, 60.0)
                oxygen = st.number_input("Oxygen Level (%)", 0, 100)
                temp = st.number_input("Temperature", 0.0, 45.0)

            st.markdown('</div>', unsafe_allow_html=True)

            # ===== SYMPTOMS =====
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">⚠️ Symptoms</div>', unsafe_allow_html=True)

            symptoms = st.text_area("Describe your symptoms")

            st.markdown('</div>', unsafe_allow_html=True)

            # ===== BUTTON =====
            if st.button("🚀 Generate AI Report", use_container_width=True):

                text = ""

                if glucose: text += f"glucose {glucose} "
                if bp: text += f"bp {bp} "
                if heart_rate: text += f"heart rate {heart_rate} "
                if cholesterol: text += f"cholesterol {cholesterol} "
                if bmi: text += f"bmi {bmi} "
                if oxygen: text += f"oxygen {oxygen} "
                if temp: text += f"temperature {temp} "
                if symptoms: text += f"{symptoms} "

                risk = "Low"

                if bp > 140 or cholesterol > 240 or glucose > 180:
                    risk = "High"
                elif bp > 120 or glucose > 140:
                    risk = "Medium"

                if text.strip() == "":
                    st.warning("⚠️ Please enter some data")
                else:
                    clean = clean_text(text)

                    c = cardio_agent(clean)
                    p = psycho_agent(clean)
                    l = pulmo_agent(clean)

                    st.subheader("📄 AI Diagnosis")

                    st.write("❤️ Cardio:", c)
                    st.write("🧠 Psycho:", p)
                    st.write("🫁 Pulmo:", l)

                    st.success(f"Risk Level: {risk}")

                    report_data = {
                        "title": "AI Medical Report",
                        "patient": {"Name": name, "Age": age, "Gender": gender},
                        "vitals": {"Glucose": glucose, "BP": bp},
                        "results": {"Cardio": c, "Psycho": p, "Pulmo": l},
                        "risk": risk
                    }

                    pdf_bytes = build_pdf_bytes(report_data)

                    st.download_button("📄 Download Report", pdf_bytes, "report.pdf")

                    save_report(st.session_state["user"], text, c, p, l)

                    st.success("Report Saved ✅")