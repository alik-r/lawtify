# 🏛️ Lawtify

A simple static legal platform with an appointment form and OpenAI-powered chatbot.

## 🚀 Getting Started (Local Dev)

### 1. Clone the Repo

```bash
git clone https://github.com/alik-r/lawtify.git
cd lawtify
```

### 2. Setup Python Environment

```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip install flask openai gunicorn
```

### 3. Set Environment Variable

Create a `.env` file or set manually:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or for one-time execution:

```bash
OPENAI_API_KEY='your-api-key-here' flask run
```

## 🧪 Local Testing Instructions

### Run Flask Dev Server

From inside `server/`:

```bash
flask run
```

Open your browser and test:

* `http://localhost:5000/` → Landing page
* `http://localhost:5000/contact` → Form page
* `http://localhost:5000/chat` → Chatbot

## ✅ Deployment-ready Notes

* Form data is saved to `server/submissions.json`.
* Chat history is **not** persisted.
* All static pages use TailwindCSS via CDN.