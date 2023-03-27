import csv
import datetime
import json


def get_payday(year, month):
    holidays = holidays_from_json()
    payday = datetime.date(year, month, 10)
    while payday.weekday() > 4 or payday in holidays:
        payday -= datetime.timedelta(days=1)
    reminder = payday - datetime.timedelta(days=3)
    return payday, reminder


def write_into_file():
    year = int(input("Enter the year: "))
    filename = f'paydays_{year}.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(
            ['Kuu'.center(12), 'Palgamaksmise kuupäev'.center(22), 'Meeldetuletuse saatmise kuupäev'.center(27)])
        writer.writerow(['_' * 12, '_' * 23, '_' * 26])
        for month in range(1, 13):
            payday, reminder = get_payday(year, month)
            writer.writerow(
                [datetime.date(year, month, 1).strftime('%B').center(12), payday.strftime('%d.%m.%Y').center(23),
                 reminder.strftime('%d.%m.%Y').center(27)])


def holidays_from_json():
    with open('holidays.json', 'r') as f:
        holidays = json.load(f)

    holiday_dates = []

    for holiday in holidays:
        if holiday['notes'] == "puhkepäev":
            holiday_dates.append(holiday['date'])
    print(holiday_dates)

    return holiday_dates


if __name__ == '__main__':
    write_into_file()
