import sqlite3
import bcrypt

# ===== CREATE DATABASE =====
def create_db():
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    # USERS TABLE (FIXED ✅)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password BLOB,
        role TEXT,
        security_question TEXT,
        security_answer TEXT
    )
    """)

    # REPORTS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        report_text TEXT,
        cardio TEXT,
        psycho TEXT,
        pulmo TEXT
    )
    """)

    conn.commit()
    conn.close()


# ===== CREATE DEFAULT ADMIN =====
def create_admin():
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", ("admin",))
    user = cursor.fetchone()

    if not user:
        hashed = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())

        cursor.execute("""
        INSERT INTO users 
        (username, password, role, security_question, security_answer)
        VALUES (?, ?, ?, ?, ?)
        """, ("admin", hashed, "admin", "Admin default question", "admin"))

        conn.commit()

    conn.close()


# ===== RESET ADMIN PASSWORD =====
def reset_admin():
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())

    cursor.execute(
        "UPDATE users SET password=? WHERE username=?",
        (hashed, "admin")
    )

    conn.commit()
    conn.close()


# ===== SAVE REPORT =====
def save_report(username, text, c, p, l):
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports (username, report_text, cardio, psycho, pulmo)
    VALUES (?, ?, ?, ?, ?)
    """, (username, text, c, p, l))

    conn.commit()
    conn.close()


# ===== GET USER REPORTS =====
def get_user_reports(username):
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports WHERE username=?", (username,))
    data = cursor.fetchall()

    conn.close()
    return data


# ===== GET ALL USERS =====
def get_all_users():
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, role FROM users")
    data = cursor.fetchall()

    conn.close()
    return data


# ===== GET ALL REPORTS =====
def get_all_reports():
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports")
    data = cursor.fetchall()

    conn.close()
    return data


# ===== DELETE REPORT =====
def delete_report(report_id):
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM reports WHERE id=?", (report_id,))

    conn.commit()
    conn.close()


# ===== GET USER BY USERNAME =====
def get_user_by_username(username):
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


# ===== UPDATE PASSWORD =====
def update_password(username, new_password):
    conn = sqlite3.connect("medi_ai.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

    cursor.execute(
        "UPDATE users SET password=? WHERE username=?",
        (hashed, username)
    )

    conn.commit()
    conn.close()