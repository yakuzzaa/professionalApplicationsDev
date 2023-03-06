# Через timestamp вывести время и дату в читабельном формате (без библиотек)

timestamp = input("Введите timestamp: ")

def parse_epoch_time(timestamp):
    year = 1970 #ведем отсчет от этой даты
    month = 1
    day = 1
    timestamp = float(timestamp)
    t_seconds = int(timestamp)
    m_seconds = int((timestamp - t_seconds) * 1000000)
    minutes, seconds = divmod(t_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    while True:
        days_in_year = 365
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_year = 366
        if days >= days_in_year:
            year += 1
            days -= days_in_year
        else:
            break
    while True:
        d_in_mounth = 31
        if month in [4, 6, 9, 11]:
            d_in_mounth = 30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                d_in_mounth = 29
            else:
                d_in_mounth = 29
        if days >= d_in_mounth:
            month += 1
            days -= d_in_mounth
        else:
            break
    day += days
    return f"Сейчас {year} год, {month} месяц, {day} день, {hours} часов, {minutes} минут, {seconds} секунд и {m_seconds} милисекунд."


time = parse_epoch_time(timestamp)
print(time)