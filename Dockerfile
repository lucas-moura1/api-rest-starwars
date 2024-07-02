FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
