# flask-container-demo 🌶️

> A minimal Flask service with a `/health` endpoint — a clean, deployable example of the app → container → Kubernetes path.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-MIT-green"/>
</p>

---

## Overview

A small Flask web app that renders a landing page and exposes a health-check endpoint. It's the "hello world" of a deployable service — the smallest unit you can containerize, add probes to, and ship to Kubernetes.

Matching manifests live in [`k8s-platform-labs`](https://github.com/PrincyRechal29/kubernetes) under `py-oreo-app/`.

## Quickstart

```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Endpoints

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/health` | Health check — returns `{"status": "ok"}` for readiness/liveness probes |

## What this demonstrates

- A minimal, **probe-ready** web service suitable for Kubernetes.
- The smallest sensible **containerization** target for CI/CD demos.

## Roadmap

- [ ] Add a `Dockerfile` with `HEALTHCHECK`
- [ ] Add a GitHub Actions build-and-push workflow

## License

MIT
