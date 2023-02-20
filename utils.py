from random import randint


# функция для ввода списка с клавиатуры
def list_input():
    return list(map(int, input().split()))


# генерация и добавление случайных чисел в массив
def random_generate(x):
    arr = list((randint(1, 5) for i in range(x)))
    return arr


# ввод элементов разными способами
def input_choice():
    generation_flag = input("Вы хотите сгенерировать числа случайным образом? (y/n)")
    if generation_flag == "y":
        return using_random_generation()
    return using_manual_input()


def using_manual_input():
    try:
        print("Введите элементы списка A через пробел: ")
        a = list_input()
        print("Введите элементы списка B через пробел: ")
        b = list_input()
        return a, b
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз")
        using_manual_input()


def using_random_generation():
    try:
        count_a = int(input("Сколько элементов вы хотите добавить в список A?: "))
        a = random_generate(count_a)

        count_b = int(input("Сколько элементов вы хотите добавить в список B?: "))
        b = random_generate(count_b)
    except ValueError:
        print("Некорректный ввод!")
        using_random_generation()

    return a, b
