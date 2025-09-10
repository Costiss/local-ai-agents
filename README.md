# Local Agents

Running AI Agents Locally via Ollama and Google ADK

## Overview

This project provides a FastAPI-based service for running AI agents locally. It leverages [Ollama](https://ollama.com/) for LLM inference and [Google ADK](https://google.github.io/adk-docs/) for agent orchestration.

## Features

- FastAPI web server for agent interaction
- Local LLM support via Ollama
- SQLite-based session management

## Directory Structure

```
.
├── app
│   └── agents          # Directory for agent definitions
├── main.py             # FastAPI application entry point
└── pyproject.toml
```

## Getting Started

First, ensure you have [UV](https://docs.astral.sh/uv/getting-started/installation/) installed.

1. **Install dependencies**

   ```bash
   uv sync --locked
   ```

2. **Start Ollama Backend**

   ```bash
   docker compose up -d
   ```

3. **Initialize llama3 model**

   ```bash
   docker exec -it ollama ollama pull llama3
   ```

4. **Run the API server**
   ```bash
   make dev
   # or
   uv run fastapi dev main.py
   ```

Server will be available at `http://localhost:8000`.

## Requirements

- [UV](https://docs.astral.sh/uv/getting-started/installation/)
- [Docker](https://www.docker.com/get-started/)
- For CUDA (NVIDIA) support, install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
