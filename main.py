from database_api import DatabaseAPI
import pandas as pd
# Параметры для подключения к БД
db_host = '127.0.0.1'
db_name = 'postgres'

# Создание объекта API
api = DatabaseAPI(db_host, input('введите логин'), input('ввод пароля'), db_name)


@api.measure_execution_time
def time_consuming_method():
    import time
    time.sleep(2)


time_consuming_method()


# Создание таблицы
data = pd.DataFrame({'id': [1, 2, 3,15,18], 'pc': ['хуперпк', 'диэнэс', 'юпитер','куплиновка','интел ньюк'],'price':[1000, 2000, 0,145,18124234]})
api.create_table(data, 'pc')
print(api.read_sql('SELECT * FROM pc'))
# трукейт(очистка)
# api.truncate_table('pc')
print(api.read_sql('SELECT * FROM pc'))


#инсерт
new_data = pd.DataFrame({'id': [4, 5], 'pc': ['Аннна', 'Олег'],'price':[1000000,0]})
api.insert_sql(new_data, 'pc')
print(api.read_sql('SELECT * FROM pc'))

api.delete_from_table('pc', id=5)
print(api.read_sql('SELECT * FROM pc'))


api.delete_from_table('pc', pc='хуперпк')
print(api.read_sql('SELECT * FROM pc'))


api.delete_from_table('pc')
print(api.read_sql('SELECT * FROM pc'))





