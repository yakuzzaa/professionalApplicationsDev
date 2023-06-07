import csv
def add_new_date():
    writer = csv.writer(open("data.csv", "w"))
    writer.writerow(["number", "data", "fio", "grant", "destination"])
    writer.writerow(["1", "15.02.2023", "Petrov Andrey Nikolayevich", "2400", "work"])
    writer.writerow(["2", "16.02.2023", "Nikolaeva Annd Dmitievna", "6000", "pool"])
    writer.writerow(["3", "17.02.2023", "Denisov Aleksandr Petrovich", "1800", "profcom"])
    writer.writerow(["4", "18.02.2023", "Sofronova Arina Alekseevna", "0", "work"])
    writer.writerow(["5", "19.02.2023", "Ivanov Ivan Ivanovich", "9000", "pool"])
    while True:
        data_flag = input("Вы хотите добавить новые данные? y/n ")
        if data_flag == "y":
            number = int(input("Введите номер "))
            data = input("Введите дату ")
            fio = input("Введите ФИО ")
            grant = input("Введите стипендию ")
            destination = input("Укажите, куда берете справку ")
            writer.writerow([number, data, fio, grant, destination])
        else:
            break
