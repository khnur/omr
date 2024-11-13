FROM python:3.10.12
LABEL authors="nkozhamuratov"

COPY requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install fastapi uvicorn python-multipart

COPY omr.py .
COPY app.py .
COPY img ./img

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]