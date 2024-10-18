FROM python:3.9.19

WORKDIR /app
ENV AIRFLOW_HOME "/app"
ENV AIRFLOW__CORE__LOAD_EXAMPLES 'false'

COPY requirements.txt requirements.txt
RUN export SLUGIFY_USES_TEXT_UNIDECODE=yes && \
    pip install -r requirements.txt

ENV PIPELINE_NAME "fraud_detection"
ENV DAGS_DIR "${AIRFLOW_HOME}/dags"
ENV DATA_DIR "${AIRFLOW_HOME}/data"
ENV SERVING_DIR "${AIRFLOW_HOME}/models/${PIPELINE_NAME}"
ENV PYTHONPATH "${DAGS_DIR}:${PYTHONPATH}"

RUN mkdir -p $DAGS_DIR \
    $DATA_DIR \
    $SERVING_DIR

COPY ./dag.py $DAGS_DIR
COPY ./src/ $DAGS_DIR/src/
COPY ./data/ $DATA_DIR

EXPOSE 8080

ENTRYPOINT airflow db reset --yes &&\
    airflow db migrate && \
    airflow users create \
        --password admin \
        --username admin \
        --firstname Peter \
        --lastname Parker \
        --role Admin \
        --email admin@example.org &&\
    airflow webserver -p 8080 & \
    sleep 10s && \
    airflow scheduler
