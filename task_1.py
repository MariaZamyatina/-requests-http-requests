import requests


def get_superhero_glossary():
    u = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url=u)
    if response.status_code > 300:
        print('error')
    if 100 < response.status_code < 300:
        res = response.json()
        heroes = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
        for hero in res:
            if hero.get("name") in heroes:
                intelligence = hero.get('powerstats').get('intelligence')
                heroes[hero.get("name")] = intelligence
    return max(heroes)


if __name__ == '__main__':
    print(f'Самый умный из трех супергероев- Hulk, Captain America или Thanos: {get_superhero_glossary()}')
