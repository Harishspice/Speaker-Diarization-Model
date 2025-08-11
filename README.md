# Speaker-Diarization-Model

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg?logo=streamlit)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/Models-HuggingFace-yellow.svg?logo=huggingface)](https://huggingface.co/)

> Real-time **speaker diarization** and **speech transcription** in a beautiful web app, powered by **Pyannote**, **Whisper**, and **SpeechBrain** — all packaged in Docker for easy deployment.

---

## ✨ Features
- **🔊 Speaker Diarization** — Detects "who spoke when" in an audio file.
- **📝 Speech Transcription** — Converts speech to text using OpenAI Whisper.
- **👥 Multi-Speaker Support** — Labels and differentiates multiple speakers.
- **🌐 Web UI** — Drag & drop audio upload via Streamlit.
- **📦 Dockerized** — Zero setup, runs anywhere.
- **🤗 HuggingFace Integration** — Uses pretrained diarization models.

---

## 🖥️ Tech Stack
- **Python 3.10+**
- **Streamlit** — UI
- **Pyannote.audio** — Diarization
- **SpeechBrain** — Speaker embeddings
- **OpenAI Whisper** — Speech-to-text
- **Docker** — Containerization

---

## 🔑 Prerequisites
- **Docker** installed ([Download here](https://www.docker.com/))
- **HuggingFace Token** (with access to Pyannote models) → [Create Token](https://huggingface.co/settings/tokens)

---

## 🚀 Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/speaker-diarization.git
cd speaker-diarization
```
### 2️⃣ Build the Docker image
```bash
docker build -t speaker-diarization .
```
### 3️⃣ Run the container
```bash
docker run -it --rm -p 8501:8501 -e HUGGINGFACE_TOKEN="your_token_here" speaker-diarization
```

## 📂 Project Structure
```bash
.
├── app.py               # Streamlit frontend
├── final_pipeline.py    # Core diarization + transcription logic
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build instructions
└── README.md            # Project documentation
```

---

## 🔮 Conclusion
This project bridges cutting-edge **speaker diarization** and **speech transcription** into a single, easy-to-use web application.  
By combining **Pyannote.audio** for precise speaker segmentation, **Whisper** for accurate transcription, and **Streamlit** for an intuitive UI — all packaged with **Docker** — it ensures that advanced speech processing is accessible to developers, researchers, and real-world applications without complicated setup.

Whether you’re building meeting transcription tools, analyzing interviews, or researching conversational patterns, this app delivers **high accuracy**, **scalability**, and **portability** right out of the box.

