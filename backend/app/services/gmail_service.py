import base64
from email.mime.text import MIMEText


class GmailService:
    def build_raw_message(self, to_email: str, subject: str, body: str) -> str:
        message = MIMEText(body)
        message["to"] = to_email
        message["subject"] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return raw

    def send_email_placeholder(self, to_email: str, subject: str, body: str) -> dict:
        # Replace this with actual Gmail OAuth token handling and Gmail API call.
        raw_message = self.build_raw_message(to_email, subject, body)
        return {
            "status": "draft_only",
            "message": "Implement Gmail OAuth and messages.send here.",
            "raw_preview_length": len(raw_message),
            "to": to_email,
            "subject": subject,
        }
