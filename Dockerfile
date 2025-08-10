# Use lightweight Python image
FROM python:3.10-slim

# Install system dependencies for audio processing
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ffmpeg git build-essential libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install deps (torch CPU-only wheels)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir torch==2.0.1+cpu torchaudio==2.0.2+cpu \
        --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose Streamlit's default port
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
