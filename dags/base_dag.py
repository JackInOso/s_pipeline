from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


hook = PostgresHook(postgres_conn_id='Postgres')

request = "insert into public.data (name, birth_date, age) values ('Anton', '2004.11.14', 19)"


def insert():
    hook.run(request)


with DAG(
    dag_id="base_dag",
    default_args={
        "owner": "demid",
    }
) as dag:

    t = PythonOperator(
        task_id='insert_postgres',
        python_callable=insert
        )