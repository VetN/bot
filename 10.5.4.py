#  программа записывает и кеширует номера.
#  Может записать номер, показать номер
import redis
red = redis.Redis( host='localhost', port=6379)

cont = True

while cont:
    action = input('write or read')
    if action == 'write':
        name = input("name")
        phone = input("phone")
        red.set(name, phone) # заносим в базу
    elif action == 'read':
        name = input('name')
        phone=red.get(name)
        print(phone)
        if phone:
            print(f'{name} phone is {str(phone)}')
    elif action == 'delete':
        name = input('name')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found{name}")
    elif action == 'stop':
        break

