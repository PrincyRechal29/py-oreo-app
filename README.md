# py-oreo-app

A simple Python Flask web app. Visit it in your browser after running locally.

## Run locally

```bash
cd /d/repos/py-oreo-app
pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5000** in your browser.

## Endpoints

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/health` | Health check — returns `{"status": "ok"}` |
