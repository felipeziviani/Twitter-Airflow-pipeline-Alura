from os.path import join
from airflow.models import DAG
from datetime import datetime, timedelta
from operators.twitter_operator import TwitterOperator

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

default_args = {
    "owner": "felipe",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="twitter_dag",
    start_date=datetime(2026, 1, 1),  
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["twitter", "pipeline"]
) as dag:

    twitter_task = TwitterOperator(
        task_id="twitter_task",

        file_path=join(
            "datalake/twitter_datascience",
            "extract_date={{ ds }}",
            "datascience_{{ ds_nodash }}.json"
        ),

        query="datascience",
        start_time="{{ macros.ds_add(ds, -1) }}T00:00:00.000Z",
        end_time="{{ ds }}T00:00:00.000Z",
    )