import redis

#  читаем данные из кеша, записанные в другой скрипт

red = redis.Redis( host='localhost', port=6379)

print(red.get('var1'))
print(red.get('dict1'))

# удаление по ключу
red.delete('var1') # удаляются ключи с помощью метода .delete()
print(red.get('var1'))