# 🎤 PitchCraft AI

PitchCraft AI is a full-stack web app that allows users (sellers or founders) to submit product pitches and receive **AI-powered investor-style feedback**.  
Built using **Django + Ninja API** for the backend, **React + Tailwind** for the frontend, and **Ollama (LLaMA2)** for AI responses.

---

## 🚀 Features

- ✍️ Submit your product pitch via an interactive form
- 🤖 Receive instant AI-generated feedback (simulating an investor)
- 📄 Feedback is saved in the database for future use
- ⚙️ Uses LLaMA 2 via `Ollama` locally
- 🌐 REST API built with Django Ninja
- 🎨 Stylish React frontend with TailwindCSS

---

## 🛠️ Tech Stack

| Layer      | Tech                          |
|------------|-------------------------------|
| Frontend   | React (Vite) + Tailwind CSS   |
| Backend    | Django + Django Ninja         |
| AI Engine  | Ollama running LLaMA2 locally |
| Database   | SQLite (default)              |
| API Client | Axios                         |

---

## 📁 Project Structure

pitchcraft/
├── core/
│ ├── models.py
│ ├── api/
│ │ ├── init.py # API registration
│ │ ├── pitch.py # Router + logic
│ │ └── schemas.py # Pydantic schemas
├── manage.py
├── db.sqlite3
└── frontend/ # React Vite frontend

yaml
Copy code

---

## ⚙️ Setup Instructions

### 📦 Backend (Django + Ninja)

1. Create virtual env & install dependencies:

```bash
python -m venv env
env\Scripts\activate          # Windows
# or
source env/bin/activate       # macOS/Linux

pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Start the server:

bash
Copy code
python manage.py runserver
🧠 Start Ollama AI server
Make sure Ollama is installed and running:

bash
Copy code
ollama serve
ollama run llama2
💻 Frontend (React + Vite)
bash
Copy code
cd frontend
npm install
npm run dev
Visit: http://localhost:5173

📬 Sample Pitch Payload
json
Copy code
{
  "seller_name": "Aarav Sharma",
  "product_name": "EcoBrush",
  "pitch_text": "A biodegradable toothbrush made from bamboo with AI-driven brushing tracker."
}
🛡️ CORS Setup (in Django)
In settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # for development only
💡 Future Ideas
User accounts & pitch history dashboard

AI persona selection (Shark Tank, VC, Angel)

Upload video/audio pitches

Scoring system & feedback comparison

🧠 Credits
Django

Django Ninja

Ollama

React

Tailwind CSS
