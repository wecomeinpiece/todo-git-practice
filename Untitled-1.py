print ("hello python    =)" )
import random
import time

# Загадываем случайное число от 1 до 100
secret_number = random.randint(1, 100)

while True:
    try:
        # Просим пользователя ввести число
        user_input = input("Угадай число от 1 до 100: ")
        guess = int(user_input)
        
        # Проверяем, совпадает ли число
        if guess == secret_number:
            print("Ты угадал!!! 🎉")
            time.sleep(20)  # Пауза 20 секунд перед завершением
            break  # Завершаем цикл, игра окончена
        elif guess < secret_number:
            print("Загаданное число больше… 😕 Попробуй ещё раз.")
        else:
            print("Загаданное число меньше… 😕 Попробуй ещё раз.")
    except ValueError:
        print("Пожалуйста, введи целое число.")