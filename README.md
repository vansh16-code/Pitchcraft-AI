# 🎤 PitchCraft AI

PitchCraft AI is a full-stack AI-powered feedback tool that allows users to submit product pitches and receive constructive, investor-style feedback instantly using **LLaMA2 via Ollama**.  

Built with **Django + Ninja API** (backend) and **React + TailwindCSS** (frontend).

---

## 🚀 Features

- 📝 Submit product pitches via a sleek web form
- 🤖 Get instant AI-generated investor-style feedback
- 💾 Feedback stored in database for future reference
- ⚙️ Built with Django Ninja REST API & served to a React frontend
- 🧠 Uses LLaMA2 model locally with Ollama API

---

## 🧱 Tech Stack

| Layer     | Technology                     |
|-----------|--------------------------------|
| Frontend  | React (Vite) + Tailwind CSS    |
| Backend   | Django + Django Ninja          |
| AI Engine | Ollama with LLaMA2 model       |
| Database  | SQLite (default)               |
| API       | Django Ninja + Axios           |

---

## 📂 Project Structure

pitchcraft/
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── admin.py
│   └── api/
│       ├── __init__.py        # API registration (NinjaAPI instance)
│       ├── pitch.py           # Routes and Ollama logic
│       └── schemas.py         # Pydantic models
│
├── frontend/                  # Vite + React frontend
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       ├── api/
│       │   └── axios.js       # Axios config
│       └── components/
│           └── PitchForm.jsx  # Pitch submission UI
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md




---

## ⚙️ Setup Instructions

### 🔧 Backend (Django + Ninja)

```bash
# Create virtual environment
python -m venv env
env\Scripts\activate     # On Windows
# or
source env/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Django development server
python manage.py runserver
🧠 Start Ollama (LLaMA2 Model)
Make sure Ollama is installed and set up.


ollama serve
ollama run llama2
🌐 Frontend (React + Vite)
bash

cd frontend
npm install
npm run dev
Visit: http://localhost:5173

🔄 API Usage
Endpoint

POST /api/pitch/submit/

Sample Payload
json
Copy code
{
  "seller_name": "Aarav Sharma",
  "product_name": "EcoBrush",
  "pitch_text": "A biodegradable toothbrush with AI-driven brushing tracker."
}

Sample Response
json
Copy code
{
  "message": "Pitch submitted successfully",
  "id": 7,
  "ai_feedback": "Your pitch is innovative. To strengthen it, add market validation..."
}
⚠️ CORS Setup (for React ↔ Django)
In settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # Development only
🛣️ Roadmap
 🧑‍💼 User accounts & pitch history

 📊 Dashboard to view submitted pitches

 🎭 AI personality selector (VC / Shark / Angel Investor)

 📹 Upload video/audio pitches

 📈 Feedback scoring system

📘 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Django

Django Ninja

Ollama

LLaMA 2

React

TailwindCSS

