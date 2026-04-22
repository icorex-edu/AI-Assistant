# AI Executive Assistant Starter Kit

This is a production-style starter project for a web-based AI assistant with:

- Anthropic Claude API
- FastAPI backend
- PostgreSQL / Supabase-compatible schema
- Gmail API integration stub
- WhatsApp Cloud API webhook + sender stub
- Facebook Page publishing stub
- n8n workflow template
- Simple browser frontend

## What this project does

You can use it as the foundation for an assistant that can:

- manage tasks and reminders
- draft and send emails
- receive and respond to WhatsApp messages
- publish Facebook Page posts
- store conversations, tasks, and audit logs
- trigger scheduled or event-driven automations

## Project structure

```text
ai-executive-assistant/
  backend/
    app/
      main.py
      config.py
      database.py
      models.py
      schemas.py
      services/
      routers/
    requirements.txt
  frontend/
    index.html
    app.js
    styles.css
  infra/
    docker-compose.yml
    schema.sql
    .env.example
  n8n/
    ai_assistant_workflow.json
```

## Quick start

### 1) Copy env file

Create `.env` in `infra/` from `.env.example`.

### 2) Start PostgreSQL

```bash
cd infra
docker compose up -d db
```

### 3) Create virtual environment and install backend dependencies

```bash
cd ../backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4) Create database tables

Run `infra/schema.sql` in your PostgreSQL database.

### 5) Start the backend

```bash
uvicorn app.main:app --reload --port 8000
```

### 6) Open the frontend

Open `frontend/index.html` in your browser, or serve it with any static server.

## API setup notes

### Anthropic / Claude
Set:
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_MODEL`

The backend uses the Messages API pattern and can be extended with tool-calling logic.

### Gmail
Create OAuth credentials in Google Cloud and enable the Gmail API.
For development, you can begin with the Python quickstart pattern. For production, use proper OAuth consent, secure token storage, and least-privilege scopes.

### WhatsApp Cloud API
Set:
- `WHATSAPP_ACCESS_TOKEN`
- `WHATSAPP_PHONE_NUMBER_ID`
- `WHATSAPP_VERIFY_TOKEN`

Configure Meta webhook callbacks to:
- `GET /webhooks/whatsapp`
- `POST /webhooks/whatsapp`

### Facebook Page posting
Set:
- `FB_PAGE_ACCESS_TOKEN`
- `FB_PAGE_ID`

### n8n
Import `n8n/ai_assistant_workflow.json` into n8n and update the webhook URL to your backend.

## Suggested next build steps

1. Add user authentication
2. Add Gmail OAuth login flow
3. Add job queue for scheduled tasks
4. Add vector memory / retrieval
5. Add admin dashboard
6. Add tool permissions and approval rules
7. Add outbound message templates for WhatsApp

## Safety suggestion

For real-world use, keep a human approval step for:
- email sending
- WhatsApp outbound replies
- Facebook posting
- calendar invites
- any financial or sensitive action


## Live deployment

See `DEPLOY_RENDER_SUPABASE.md` for the fastest deployment path using Render + Supabase.
