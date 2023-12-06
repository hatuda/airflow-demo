import datetime

from airflow.decorators import dag
from airflow.operators.bash import BashOperator


@dag(dag_id="demo", start_date=datetime.datetime(2023, 12, 5), schedule="*/1 * * * *")
def generate_dag():
    # ランダムに失敗するコマンドを実行
    bash = BashOperator(task_id="task",
                        bash_command="exit $((RANDOM % 2))")
    # AWSのFargateタスクを実行する場合にはBashOperatorの代わりにEcsRunTaskOperatorを使います。
    dependent_bash = BashOperator(task_id="dependent",
                                  bash_command="echo after")

    bash >> dependent_bash


generate_dag()
