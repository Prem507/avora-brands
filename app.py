from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import re
from datetime import datetime

app = Flask(__name__)
DB = "avora.db"

# ---------- Database Setup ----------

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            message TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            cover_letter TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------- Routes ----------

@app.route("/")
def home():
    return render_template("contact.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

# ---------- API: Submit Contact ----------

@app.route("/api/contact", methods=["POST"])
def submit_contact():
    data = request.get_json()

    name    = (data.get("name") or "").strip()
    email   = (data.get("email") or "").strip()
    phone   = (data.get("phone") or "").strip()
    message = (data.get("message") or "").strip()

    # Validation
    if not name or not email or not message:
        return jsonify({"success": False, "error": "Name, email, and message are required."}), 400
    if not is_valid_email(email):
        return jsonify({"success": False, "error": "Please enter a valid email address."}), 400

    # Save to DB
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)",
        (name, email, phone, message)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": f"Thanks {name}! We'll get back to you soon."})

# ---------- API: Submit Application ----------

@app.route("/api/apply", methods=["POST"])
def submit_application():
    data = request.get_json()

    job_title    = (data.get("job_title") or "").strip()
    name         = (data.get("name") or "").strip()
    email        = (data.get("email") or "").strip()
    phone        = (data.get("phone") or "").strip()
    cover_letter = (data.get("cover_letter") or "").strip()

    if not name or not email or not job_title:
        return jsonify({"success": False, "error": "Name, email, and job title are required."}), 400
    if not is_valid_email(email):
        return jsonify({"success": False, "error": "Please enter a valid email address."}), 400

    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO applications (job_title, name, email, phone, cover_letter) VALUES (?, ?, ?, ?, ?)",
        (job_title, name, email, phone, cover_letter)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": f"Application submitted for {job_title}! We'll review it and reach out."})

# ---------- Run ----------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
