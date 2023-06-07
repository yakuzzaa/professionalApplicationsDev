from Reference import CSVReader
from append_data_in_table import add_new_date

try:
    add_new_date()
except KeyError:
    print("Попробуйте заново.")
    add_new_date()


if __name__ == "__main__":
    reader = CSVReader()

    print(f"Словарь с данными:{reader}")
    print(f"Сортировка по фио: {reader.fio_sorting('fio')}")
    print(f"Сортировка по стипендии: {reader.grant_sorting('grant')}")
    print(f"Сортировка по стипендии, которая больше value {reader.grant_more_than_sorting('grant','2000')}")

    print("Итерация")
    for i in reader:
        print(i)

    print('=' * 20)

    print('Генератор')
    for i in reader.generator():
        print(i)

    print('=' * 20)

    fio, grant, destination = input('Введите новые данные(ФИО, стипендия, назначение справки: ').split()
    reader.new_entry(fio, grant, destination)
    reader.save()