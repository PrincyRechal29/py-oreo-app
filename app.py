from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Oreo App</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #1a1a2e;
      font-family: 'Segoe UI', sans-serif;
      color: white;
    }
    .card {
      text-align: center;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 24px;
      padding: 60px 80px;
    }
    .cookie { font-size: 80px; margin-bottom: 24px; }
    h1 { font-size: 42px; font-weight: 800; margin-bottom: 12px; }
    h1 span { color: #a78bfa; }
    p { color: #94a3b8; font-size: 16px; margin-bottom: 32px; }
    .badge {
      display: inline-block;
      padding: 8px 20px;
      border-radius: 999px;
      background: #a78bfa;
      color: white;
      font-size: 14px;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="cookie">🍪</div>
    <h1>Welcome to <span>Oreo App</span></h1>
    <p>A simple Python Flask app running in your browser.</p>
    <span class="badge">Python + Flask</span>
  </div>
</body>
</html>
"""

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
