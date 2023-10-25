from database_api import DatabaseAPI
import pandas as pd
# Параметры для подключения к БД
db_host = '127.0.0.1'
db_username = 'postgres'
db_name = 'postgres'

# Создание объекта API
api = DatabaseAPI(db_host, db_username, input('ввод пароля'), db_name)

@api.measure_execution_time
def time_consuming_method():
    # Simulate a time-consuming operation
    import time
    time.sleep(2)  # Sleep for 2 seconds

# Call the decorated method
time_consuming_method()

# Создание таблицы
data = pd.DataFrame({'id': [1, 2, 3], 'names': ['Alice', 'Bob', 'Charlie']})
api.create_table(data, 'users')

# Очистка таблицы
# api.truncate_table('users')

print(api.read_sql('SELECT * FROM users'))

#Запись данных в таблицу
new_data = pd.DataFrame({'id': [4, 5], 'names': ['David', 'Eve']})
api.insert_sql(new_data, 'users')

print(api.read_sql('SELECT * FROM users'))

api.delete_from_table('users', id=4, names='David')
print(api.read_sql('SELECT * FROM users'))
api.delete_from_table('users', names='Eve')
print(api.read_sql('SELECT * FROM users'))
api.delete_from_table('users')
print(api.read_sql('SELECT * FROM users'))
# # Выполнение произвольного SQL-запроса





