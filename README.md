# 📘 LLM API Usage

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Gemini%20%7C%20OpenAI%20%7C%20HuggingFace-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streaming-Supported-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Environment-.env-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge" />
</p>

---

## Overview

**LLM API Usage** is a **practical, no-fluff repository** demonstrating how to work with **modern Large Language Model APIs** in real-world Python applications.

Unlike generic “GPT wrappers”, this repo focuses on:

* **Correct API usage**
* **Streaming responses**
* **Error-safe implementations**
* **Provider-specific quirks**
* **Production-friendly patterns**

This repository is ideal as:

* A **learning reference**
* A **starter base** for GenAI projects
* A **portfolio / resume project**

---

## Supported Providers

### Google Gemini

* Standard text generation
* Token streaming (real-time output)
* Gemini usage via **OpenAI-compatible client**

### Hugging Face

* Serverless Inference API
* Open-source models:

  * Mistral
  * Phi-3
  * Qwen
  * Zephyr
* Streaming implementation
* Graceful handling of:

  * Cold starts
  * 503 / model loading errors

### OpenAI

* Chat completions
* Streaming completions
* Industry-standard API patterns

---

## Why This Repository Is Different

| Typical Repos                     | This Repo                 |
| --------------------------------- | ------------------------- |
| Just `.chat.completions.create()` | Full streaming lifecycle  |
| One provider                      | Multi-provider comparison |
| No error handling                 | Production-safe checks    |
| Toy examples                      | Real integration patterns |

---

## Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/OpenAI-API-black?style=flat-square" />
  <img src="https://img.shields.io/badge/Google-Gemini-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/HuggingFace-Inference-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Streaming-Enabled-success?style=flat-square" />
</p>

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SoumilMalik24/LLM-API-Usage.git
cd LLM-API-Usage
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-genai huggingface_hub openai python-dotenv
```

---

## Environment Configuration

Create a `.env` file in the root directory:

```env
# Google Gemini
GOOGLE_API_KEY=your_gemini_api_key_here

# Hugging Face
HF_API_TOKEN=your_huggingface_token_here

# OpenAI
OPENAI_API_KEY=your_openai_api_key_here
```

> Never commit `.env` to GitHub.

---

## Usage

### Google Gemini

```bash
python gemini_usage.py
python gemini_streaming.py
python gemini_using_openai.py
```

### Hugging Face

```bash
python huggingface_api_usage.py
python huggingface_streaming.py
```

### OpenAI

```bash
python openai_api_usage.py
python openai_streaming.py
```

---

## Streaming: Important Note

Some streaming responses include **final empty chunks**.

 Correct way:

```python
if chunk.choices and chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="")
```

Incorrect way (causes IndexError):

```python
print(chunk.choices[0].delta.content)
```

---

## Common Issues & Fixes

### Hugging Face – `503 Service Unavailable`

**Reason:** Model is cold or unavailable
**Fix:** Use lightweight models like:

* `microsoft/Phi-3.5-mini-instruct`
* `meta-llama/Llama-3.2-3B-Instruct`

---

### Gemini – `404 Model Not Found`

**Fix:** Use:

* `gemini-1.5-flash`
* `gemini-2.0-flash-exp`

---

## Who Should Use This Repo?

* B.Tech / CS students
* GenAI beginners
* MLOps learners
* Backend developers integrating LLMs
* Anyone building **RAG / Agentic AI systems**

---

## 📜 License

Licensed under the **MIT License**.
Feel free to fork, modify, and use in your own projects.


