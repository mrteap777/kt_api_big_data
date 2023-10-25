import pandas as pd
import time
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from datetime import datetime
class DatabaseAPI:
    def __init__(self, host, username, password, database):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')

    def create_table(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def delete_from_table(self, table_name, **kwargs):
        if not kwargs:
            return  # No conditions specified, no action needed.

        where_conditions = " AND ".join([f"{key} = :{key}" for key in kwargs])
        query = f'DELETE FROM {table_name} WHERE {where_conditions}'

        with self.engine.begin() as conn:
            compiled = text(query)
            for key, value in kwargs.items():
                compiled = compiled.bindparams(**{key: value})
            conn.execute(compiled)

    def truncate_table(self, table_name):
        query = f'TRUNCATE TABLE {table_name}'
        with self.engine.begin() as conn:
            conn.execute(text(query))

    def read_sql(self, query):
        return pd.read_sql_query(query, self.engine)

    def insert_sql(self, df, table_name, if_exists='append'):
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)

    def execute(self, query):
        with self.engine.begin() as conn:
            conn.execute(text(query))

    @staticmethod
    def measure_execution_time(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time}")
            return result

        return wrapper
