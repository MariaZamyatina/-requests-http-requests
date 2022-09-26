import requests
from bs4 import BeautifulSoup
import datetime

creation_data = input("Введите дату, с которй осуществлять поиск вопросов (в формате 2022-09-24): ")
creation_data_new = datetime.datetime.strptime(str(creation_data), '%Y-%m-%d')
creation_data_new = creation_data_new + datetime.timedelta(hours=3)

question_data = datetime.datetime.now()  # Инициализирую значение по умолчанию текущим временем

h = 0  # Индекс страницы. Увеличиваем пока дата создания не будет меньше даты введеной нами
dict = {'time': [], 'title': [], 'link': []}

while str(creation_data_new) <= str(question_data):

    url = "https://stackoverflow.com/questions/tagged/python?tab=newest&page=" + str(h) + '&pagesize=15'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    allNews = soup.find_all('h3', class_="s-post-summary--content-title")

    time = soup.findAll('time')
    for t in time:
        dict['time'].append(t.findAll('span', class_="relativetime")[0].get('title'))

    question_data = dict.get('time')[-1]

    for i in allNews:
        title = i.text.strip()
        dict['title'].append(title)
        link = 'https://stackoverflow.com/' + i.find_all_next('a', class_="s-link")[0].get('href')
        dict['link'].append(link)

    h += 1


count = 0
with open('questions.txt', 'a', encoding='utf-8') as file:
    while count <= len(dict.get('title')) - 1:
        file.write('Вопрос: \n')
        file.write('Title: ' + dict.get('title')[count] + '\n')
        print('Title: ' + dict.get('title')[count])
        file.write('link: ' + dict.get('link')[count] + '\n')
        print('link: ' + dict.get('link')[count])
        print('время создания:' + dict.get('time')[count], '\n')
        file.write('время создания:' + dict.get('time')[count] + '\n')
        file.write(' ')
        count += 1

print(f'Количество вопросов с {creation_data} и с тэгом Python = {len(dict.get("title"))}')