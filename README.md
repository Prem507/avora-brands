# Avora Brands – Contact & Careers Pages

A simple full-stack web app built with **Python (Flask)** and **SQLite**.

---

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install flask

# 2. Run the app
python app.py

# 3. Open in browser
http://localhost:5000
```

---

## 📁 Project Structure

```
avora-brands/
├── app.py              ← Flask backend (routes + API + DB)
├── avora.db            ← SQLite database (auto-created on first run)
├── requirements.txt
├── README.md
└── templates/
    ├── base.html       ← Shared layout (nav, footer, styles)
    ├── contact.html    ← Contact page
    └── careers.html    ← Careers page with 3 job listings
```

---

## 🌐 Pages

| Page | URL | What it does |
|------|-----|-------------|
| Contact | `/contact` | Form with Name, Email, Phone, Message |
| Careers | `/careers` | 3 job listings with Apply modal |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contact` | Saves contact form to DB |
| POST | `/api/apply` | Saves job application to DB |

Both return JSON: `{ "success": true, "message": "..." }` or `{ "success": false, "error": "..." }`

---

## 🗃️ Database

SQLite (`avora.db`) is auto-created with 2 tables:
- **contacts** – name, email, phone, message, timestamp
- **applications** – job_title, name, email, phone, cover_letter, timestamp

---

## 💡 Approach

I kept it as simple as possible:

1. **Flask** handles routing and API — minimal setup, no extra frameworks
2. **SQLite** for storage — no server needed, just a file
3. **Vanilla HTML/CSS/JS** in Jinja2 templates — no React or build tools
4. **Validation** is done on both frontend (JS) and backend (Python)
5. **Toast notifications** replace page reloads for a smooth experience

---

## 🔮 Bonus (Future improvements)

- Email notifications via `smtplib` or SendGrid
- Deploy to Render / Railway (free tier, just push to GitHub)
- Add admin dashboard to view submissions
- File upload for resume/CV

---

## 📦 Deploy to Render (Free)

1. Push to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `python app.py`

Done!
