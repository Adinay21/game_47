import random


def start_game(range_min, range_max, attempts, starting_balance):
    target_number = random.randint(range_min, range_max)
    balance = starting_balance

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Попробуйте угадать число от {range_min} до {range_max}.")
    print(f"У вас есть {attempts} попыток.")
    print(f"Ваш начальный капитал: {balance}\n")

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt} из {attempts}. Текущий баланс: {balance}")

        try:
            bet = int(input("Введите вашу ставку: "))
            if bet > balance:
                print("Недостаточно средств для этой ставки.")
                continue

            guess = int(input(f"Введите ваше число ({range_min} - {range_max}): "))

            if guess == target_number:
                print(f"Поздравляю! Вы угадали число {target_number}.")
                balance += bet * 2
                print(f"Ваш баланс увеличился до {balance}.\n")
                break
            else:
                balance -= bet
                print(f"Неправильно. Остаток баланса: {balance}.\n")

            if balance <= 0:
                print("Ваш баланс исчерпан. Игра окончена.")
                break

        except ValueError:
            print("Неправильный ввод. Попробуйте снова.\n")

    print(f"Игра окончена. Загаданное число было: {target_number}. Ваш итоговый баланс: {balance}.")

# dfghjk
