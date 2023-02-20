from with_standart_functions import chain_search_auto
from utils import random_generate, list_input, input_choice
from manual_realization import chain_replace

if __name__ == '__main__':
    a, b = input_choice()
    print(f'Список A {a}')
    print(f'Список B {b}')
    manual_flag = input("Вы хотите использовать ручную реализацию? (y/n)")
    if manual_flag == "y":
        chain_replace(a, b)
    else:
        chain_search_auto(a, b)


