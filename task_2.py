
import requests


class YandexDisc:

    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        """Метод получает путь с яндекс диска до файла"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        p = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=p)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        """ Метод записывает файл на яндекс диск"""
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}


if __name__ == '__main__':
    TOKEN = input('Введите TOKEN: ')
    ya = YandexDisc(token=TOKEN)
    ya.upload_file_to_disk('Задача№2.txt', '2209.txt')
