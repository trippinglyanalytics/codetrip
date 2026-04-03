# Portfolio Project: Cloud Deployment + CI/CD

This repository now includes everything needed to satisfy the project handoff brief via **both tracks**:

- **Path A (Cloud-ready):** Dockerized static portfolio application.
- **Path B (CI/CD):** GitHub Actions workflow that runs build + test on every push/PR.

## What is included

- A responsive single-page portfolio site (`index.html`, `style.css`, `script.js`)
- A Docker image definition for deployment (`Dockerfile`, `nginx.conf`)
- A lightweight build pipeline (`npm run build`) that creates a `dist/` folder
- A lightweight automated test suite (`npm test`) that validates core portfolio content
- A GitHub Actions workflow (`.github/workflows/ci.yml`) that runs on push and pull requests

## Run locally

```bash
npm ci
npm run build
npm test
npm run dev
```

Then open: <http://localhost:8080>

## Run with Docker

```bash
docker build -t portfolio-app .
docker run --rm -p 8080:80 portfolio-app
```

Then open: <http://localhost:8080>

## CI/CD workflow

The workflow executes the following jobs:

1. Install dependencies (`npm ci`)
2. Build static assets (`npm run build`)
3. Run tests (`npm test`)
4. Store `dist/` as a workflow artifact

This satisfies the required GitHub Actions pipeline with explicit **build** and **test** steps.

## Suggested cloud deployment options

You can ship this container image to:

- **Azure App Service (Container)**
- **Google Cloud Run**
- **AWS ECS / Fargate**

Because the app is static and served by Nginx, it is inexpensive and straightforward to run.
