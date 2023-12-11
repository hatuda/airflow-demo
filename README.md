# `Airflow`検証

[Airflow を Docker で動かす](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
形式のものになります。<br>
以下の手順で起動できます。

1. 初期化

```shell
docker compose up airflow-init
```

2. 起動

```shell
docker compose up
```

3. [ログイン画面](http://localhost:8080/)にアクセス
    - **ログインID,パスワードは`airflow`です。**

## ``DAG``作成のための初期設定

[pipenv](https://pipenv.pypa.io/en/latest/)による設定管理を行っているため、以下のコマンドを最初に<br>
実行する必要がある。

```shell
 pipenv install
```

- **上記コマンドの実行についてはpipenvのインストールが事前に必要になります。**
- **[pyenv](https://github.com/pyenv-win/pyenv-win)
  をインストールすることにより指定されたバージョンのPythonもインストールされるため、<br>**
  **こちらもインストールした方がいいです。**