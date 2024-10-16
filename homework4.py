mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

while True:
    command = input('Введите действие ("1", "2", "3", "0"):').lower()
    if command == '1':
        if len(mentors) <= 10:
            add_mentor = input('Введите имя нового ментора: ').title()
            if len(add_mentor) <= 15:
                if add_mentor not in mentors:
                    mentors.append(add_mentor)
                else:
                    print("Данный ментор уже существует")
            else:
                print("Слишком длинное имя")
        else:
            print("Максимальное количество")

    elif command == '2':
        change_mentor = input('Введите имя ментора, которого хотите заменить:').title()
        new_mentor = input('Имя нового ментора: ').title()
        if len(new_mentor) <= 15:
            if new_mentor not in mentors:
                mentors[mentors.index(change_mentor)] = new_mentor
            else:
                print('Данный ментор уже существует')
        else:
            print('Слишком длинное имя')

    elif command == '3':
        question = input('Выберите как удалить ментора: имя - по имени/ индекс - по индексу')
        if question == 'имя':
            del_mentor_name = input('Введите имя ментора для удаления: ').title()
            if del_mentor_name in mentors:
                mentors.remove(del_mentor_name)
            else:
                print('Такого ментора нет')
        elif question == 'индекс':
            del_mentor_index = int(input('Введите индекс ментора для удаления: '))
            if (del_mentor_index <=
                    (len(mentors) -1)):
               mentors.pop(del_mentor_index)
            else:
                print('Такого индекса не существует')
        else:
            print('Введите имя или индекс')

    elif command == '0':
        mentors_tuple = tuple(mentors)
        print(f'Новый список менторов: {mentors_tuple}')
        break

    else:
        print('Вводите только команды')
#         fghjkl;
