from validate_json import validate_json, json_schema_user


def test_get_users_validate_json(api):
    """
    Проверяю что пользователи соответсвуют json схеме
    :param api:
    :return:
    """
    res = api.get_users()
    res_json = res.json()
    assert res.status_code == 200
    for item in res_json['data']:
        assert validate_json(item, json_schema_user), f'{item} не соответсвует модели json'


def test_get_users_unique_ids(api):
    """
    Проверяю что у пользователей уникальные id
    :param api:
    :return:-
    """
    res = api.get_users()
    res_json = res.json()
    assert res.status_code == 200
    ids = []
    for item in res_json['data']:
        assert isinstance(item['id'], int)
        assert ids not in ids
        ids.append(item['id'])
