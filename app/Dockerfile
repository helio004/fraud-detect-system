FROM python:3.9

WORKDIR /app

COPY requirements.txt .

ENV MODEL_PATH "models/fraud_detection"

RUN pip install -r requirements.txt
RUN mkdir -p $MODEL_PATH

COPY ./ .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
