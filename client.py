import requests


class APIClient:

    def __init__(self, host: str):
        self.host = host

    def get_users(self):
        return requests.get(url=f'{self.host}/users')

    def get_user(self, user_id: str or int):
        return requests.get(url=f'{self.host}/users/{user_id}')

    def create_user(self, first_name=None, second_name=None, age=None):
        json = {'first_name': first_name, 'second_name': second_name, 'age': age}
        return requests.post(url=f'{self.host}/users', json=json)

    def delete_user_by_body(self, user_id: str or int):
        json = {'id': user_id}
        return requests.delete(url=f'{self.host}/users', json=json)

    def delete_user_by_url(self, user_id: str or int):
        return requests.delete(url=f'{self.host}/users/{user_id}')

    def get_users_count(self):
        return len(self.get_users().json()['data'])


if __name__ == '__main__':
    api = APIClient('http://127.0.0.1:5000')
    api.create_user('', 'fdsf')