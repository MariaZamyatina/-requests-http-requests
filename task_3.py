from pprint import pprint
import json
import requests
import datetime


def get_time_in_seconds(time_in_seconds):
    """function converts ordinary date to date in total seconds"""
    time_new = datetime.datetime.now() - datetime.datetime.strptime(str(time_in_seconds), '%Y-%b-%d')
    return time_new.total_seconds()


def get_questions(date_time):
    u = "https://api.stackexchange.com/2.3/questions"
    time_in_seconds = get_time_in_seconds(date_time)
    time_in_seconds = '{:.0f}'.format(time_in_seconds)

    p = {
        "fromdate": str(time_in_seconds),
        "tagged": "Python",
        "site": "stackoverflow",
        "sort": "activity"
    }
    pprint(requests.get(u, params=p).json())

    with open('questions.json', 'w') as file:
        json.dump(requests.get(u, params=p).json(), file, indent=2)


if __name__ == '__main__':
    from_time = str(input('Введите дату, с которой осуществить выборку вопросов (в формате 2022-Sep-23): '))
    get_questions(from_time)