import sqlite3


db_name = '''homework_8.db'''

db = sqlite3.connect(db_name)

cursor = db.cursor()



print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
city_id = input('Введите id города: 1 - Bishkek, 2 - Osh, 3 - New-York, 4 - Rome, '
                '5 - Milan, 6 - Talas, 7 - Naryn, 8 - Chicago, 9 - Ostyn, 10 - Mayami, 11 - Jalal-Abbad: ')

for students in sqlite3.students:
    if city_id == '0':
        break
    elif city_id == '1':
        print(students.city_id == 1)
    elif city_id == '2':
        print(students.city_id == 2)
    elif city_id == '3':
        print(students.city_id == 3)
    elif city_id == '4':
        print(students.city_id == 4)
    elif city_id == '5':
        print(students.city_id == 5)
    elif city_id == '6':
        print(students.city_id == 6)
    elif city_id == '7':
        print(students.city_id == 7)
    elif city_id == '8':
        print(students.city_id == 8)
    elif city_id == '9':
        print(students.city_id == 9)
    elif city_id == '10':
        print(students.city_id == 10)
    elif city_id == '11':
        print(students.city_id == 11)
    else:
        print('Такого id не существует')



db.commit()
db.close()
