const API_BASE = window.APP_CONFIG?.API_BASE || "http://127.0.0.1:8000";

document.getElementById("sendBtn").addEventListener("click", async () => {
  const message = document.getElementById("message").value;
  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      user_id: "demo-user",
      message,
      channel: "web"
    })
  });
  const data = await res.json();
  document.getElementById("replyBox").textContent = JSON.stringify(data, null, 2);
});

document.getElementById("taskBtn").addEventListener("click", async () => {
  const title = document.getElementById("taskTitle").value;
  const description = document.getElementById("taskDesc").value;
  const res = await fetch(`${API_BASE}/tasks`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title, description })
  });
  const data = await res.json();
  document.getElementById("taskBox").textContent = JSON.stringify(data, null, 2);
});

document.getElementById("fbBtn").addEventListener("click", async () => {
  const message = document.getElementById("fbMessage").value;
  const res = await fetch(`${API_BASE}/integrations/facebook/post`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message })
  });
  const data = await res.json();
  document.getElementById("fbBox").textContent = JSON.stringify(data, null, 2);
});
