import datetime

from airflow.decorators import dag
from airflow.operators.bash import BashOperator


@dag(start_date=datetime.datetime(2023, 12, 5), schedule="*/1 * * * *")
def generate_dag():
    # ランダムに失敗するコマンドを実行
    BashOperator(task_id="task",
                 bash_command="exit $((RANDOM % 2))")


generate_dag()
