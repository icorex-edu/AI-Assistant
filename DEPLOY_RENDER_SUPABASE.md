# Deploy live with Render + Supabase

## Recommended architecture
- Backend: Render Web Service
- Frontend: Render Static Site
- Database: Supabase Postgres

## 1) Create Supabase project
Create a new project in Supabase, then open the **Connect** panel and copy your Postgres connection string.

Use either:
- direct database connection, or
- the pooler/session connection if your environment needs it

Paste that value into the backend environment variable:
- `DATABASE_URL`

## 2) Create GitHub repo
Upload this project to a new GitHub repository.

## 3) Deploy backend on Render
In Render:
- New → Web Service
- Connect your GitHub repo
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

Add environment variables:
- `APP_ENV=production`
- `FRONTEND_ORIGIN=*`
- `ANTHROPIC_API_KEY=...`
- `ANTHROPIC_MODEL=claude-sonnet-4-5`
- `DATABASE_URL=...`
- `GOOGLE_CLIENT_ID=...`
- `GOOGLE_CLIENT_SECRET=...`
- `GOOGLE_REDIRECT_URI=...`
- `WHATSAPP_ACCESS_TOKEN=...`
- `WHATSAPP_PHONE_NUMBER_ID=...`
- `WHATSAPP_VERIFY_TOKEN=...`
- `FB_PAGE_ACCESS_TOKEN=...`
- `FB_PAGE_ID=...`

After deploy, open:
- `/health`
- `/docs`

## 4) Deploy frontend on Render
In Render:
- New → Static Site
- Connect the same GitHub repo
- Root Directory: `frontend`
- Publish Directory: `.`

Before deploy, edit `frontend/config.js` and replace:
- `https://YOUR-BACKEND-SERVICE.onrender.com`
with your actual backend URL.

Then redeploy the static site.

## 5) Load database schema
Open Supabase SQL Editor and run the contents of:
- `infra/schema.sql`

## 6) Connect WhatsApp webhook
In Meta Developer dashboard, point the webhook to:
- `https://YOUR-BACKEND-SERVICE.onrender.com/webhooks/whatsapp`

Verification endpoint:
- `GET /webhooks/whatsapp`

Incoming messages endpoint:
- `POST /webhooks/whatsapp`

## 7) Facebook Page posting
Use a valid Page access token and Page ID, then test:
- `POST /integrations/facebook/post`

## 8) Gmail
The current project includes a safe placeholder only.
For production, add:
- Google OAuth sign-in flow
- token storage
- Gmail API send endpoint

## 9) Optional n8n
Import:
- `n8n/ai_assistant_workflow.json`

Then point it to your backend base URL.

## Go-live checklist
- Backend `/health` works
- Frontend can call backend
- Schema loaded in Supabase
- Claude API key added
- CORS checked
- Meta webhook verified
- Facebook Page token valid
- Gmail OAuth completed
