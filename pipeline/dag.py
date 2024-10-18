from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.preprocess import preprocess_data
from src.train import train_model
from src.evaluation import evaluate_model


default_args = {
    'owner': 'helio',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'fraud_detection_pipeline',
    default_args=default_args,
    description='Pipeline de detecção de fraudes',
    schedule_interval=timedelta(days=1),
) as dag:

    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
        dag=dag,
    )

    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
        dag=dag,
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
        dag=dag,
    )

    preprocess_task >> train_task >> evaluate_task
