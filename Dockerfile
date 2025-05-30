# Base Image
FROM python:3.12-slim

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

RUN apt-get update && apt-get install -y curl build-essential \
    && rm -rf /var/lib/apt/lists/* # Clean up apt cache to keep image size small


# Set the working directory inside the container
WORKDIR /app


# (Optional, but good practice if you want to use uv for faster installs)
# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Ensure uv is in the PATH for the current session (for RUN commands that follow)
ENV PATH="/root/.local/bin:${PATH}"

# Copy application code
COPY pyproject.toml ./

# Create and set up virtual environment
RUN uv pip install . --system && \
    uv venv && \
    uv sync && \
    uv build

# Copy your entire application code
COPY . .

# Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501

# Command to run your Streamlit application
# Replace `your_streamlit_app.py` with the actual name of your Streamlit file
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]