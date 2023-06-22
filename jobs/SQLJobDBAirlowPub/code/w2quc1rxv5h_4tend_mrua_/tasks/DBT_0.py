def DBT_0():
    settings = {}
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    envs["DBT_FULL_REFRESH"] = "true"
    envs["DBT_PROFILE_SECRET"] = "AuQ_nDT2w7QBzqzQZov5J"
    envs["GIT_TOKEN_SECRET"] = ""
    envs["GIT_ENTITY"] = "branch"
    envs["GIT_ENTITY_VALUE"] = "dev"
    envs["GIT_SSH_URL"] = "https://github.com/abhisheks-prophecy/sql_db_app"
    envs["GIT_SUB_PATH"] = ""

    return BashOperator(
        task_id = "DBT_0",
        bash_command = f"$PROPHECY_HOME/run_dbt.sh \"dbt deps --profile run_profile; dbt seed --profile run_profile; dbt run --profile run_profile; \"",
        env = envs,
        append_env = True,
        **settings
    )
