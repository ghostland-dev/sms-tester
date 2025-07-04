FROM python:3.12-slim

WORKDIR /app

COPY sms_api.py ./
COPY sms_storage.json ./

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "sms_api:app", "--host", "0.0.0.0", "--port", "8000"] 