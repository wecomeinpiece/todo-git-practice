import random

def guess_the_number():
    # Загадываем число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            # Получаем ввод от пользователя
            user_input = input("Введи своё число: ")
            guess = int(user_input)
            attempts += 1

            # Сравниваем с загаданным числом
            if guess < secret_number:
                print("Моё число больше!")
            elif guess > secret_number:
                print("Моё число меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")

if __name__ == "__main__":
    guess_the_number()