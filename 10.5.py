#  кеширование данных с помощью redis
import redis
import json

red = redis.Redis( host='localhost', port=6379)
# создаем запись
red.set('var1', 'value1')

#  создаем словарь для записи
dict1 = {'key1': 'value1', 'key2': 'value2'}

# с помощью dumps() из модуля json меняем словарь на строчку
red.set('dict1', json.dumps(dict1))

#  с помощью loads() из модуля json
#  превращаем полученные из кеша обратно в словарь
converted_dict = json.loads(red.get('dict1'))

#  убеждаемся что получили действительно словарь
print(red.get('var1'))
print(red.get('dict1'))
print(type(converted_dict))
print(converted_dict)