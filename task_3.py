import requests
from bs4 import BeautifulSoup

h = 0  # Индекс страницы. Увеличиваем пока дата создания не будет меньше даты введеной нами
dict = {'time': [], 'title': [], 'link': []}
count = 0
indicator = True
while indicator:
    count += 1
    url = f'https://stackoverflow.com/questions/tagged/python?tab=newest&page={count}&pagesize=50'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')#"html.parser")

    allNews = soup.find_all('h3', class_="s-post-summary--content-title")

    time = soup.findAll('time')

    for t in time:
        t = t.text
        dict['time'].append(t)

    question_data = dict.get('time')[-1]

    for i in allNews:
        title = i.text.strip()
        dict['title'].append(title)
        link = 'https://stackoverflow.com/' + i.find_all_next('a', class_="s-link")[0].get('href')
        dict['link'].append(link)

    if question_data == 'asked 2 days ago':
        indicator = False


count = 0
with open('questions.txt', 'a', encoding='utf-8') as file:
    while dict.get('time')[count] != 'asked 2 days ago':
        file.write('Вопрос: \n')
        file.write('Title: ' + dict.get('title')[count] + '\n')
        print('Title: ' + dict.get('title')[count])
        file.write('link: ' + dict.get('link')[count] + '\n')
        print('link: ' + dict.get('link')[count])
        print('время создания:' + dict.get('time')[count], '\n')
        file.write('время создания:' + dict.get('time')[count] + '\n')
        file.write(' ')
        count += 1

print(count)
print(f'Количество вопросов за последние два дня и с тэгом Python = {count}')
