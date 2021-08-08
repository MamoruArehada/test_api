import pytest
from validate_json import validate_json, json_schema_user


def test_get_user_validate_json(api):
    """
    Проверяю что запрошенный пользователь соответсвует json схеме
    :param api:
    :return:
    """
    res = api.get_user(user_id=99)
    print(res)
    print(res.status_code)
    
    res_json = res.json()
    print(res_json)
    assert res.status_code == 200
    user_data = res_json['data'][0]
    print(user_data)
    assert validate_json(user_data, json_schema_user), f'{user_data} не соответсвует модели json'


def test_get_user_check_match_user_in_current_users(api):
    """
    Проверяю что запрошеный пользователь оттадется в списке всех пользователей
    :param api:
    :return:
    """
    user_id = 2
    users = api.get_users()
    assert users.status_code == 200
    user = api.get_user(user_id=user_id)
    assert user.status_code == 200
    users_json = users.json()
    user_json = user.json()['data']
    assert user_json, 'нет данных о пользователе'
    user_for_check = None
    for item in users_json['data']:
        if item['id'] == user_id:
            user_for_check = item
            break
    assert user_for_check == user_json[0]


def test_get_user_check_response_do_not_exist_user(api):
    """
    Получаю список пользователей и делаю запрос на пользователя по id которого нет
    :param api:
    :return:
    """
    users = api.get_users()
    assert users.status_code == 200
    users_json = users.json()
    count_all_users = len(users_json['data'])
    assert count_all_users != 0
    do_not_exist_user_id = count_all_users
    user = api.get_user(user_id=do_not_exist_user_id)
    assert user.status_code == 404


@pytest.mark.parametrize('user_id', ["?user=1'", '?user=1"'])
def test_get_users_check_sql(api, user_id):
    """
    Проверяю наличие уязвимости на sql иньекцию
    :param api:
    :param user_id:
    :return:
    """
    res = api.get_user(user_id)
    assert res.status_code == 404
