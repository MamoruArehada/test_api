import pytest


# positive
@pytest.mark.parametrize('first_name, second_name, age', [('Aleksey', 'Alekseyvich', 56),
                                                          ('Alexandr', 'Alexandrovich', 35)])
def test_create_user_check_added_with_valid_values(api, first_name, second_name, age):
    """
    Проверяю добавление пользователя с валидными значениями
    :param api:
    :param first_name:
    :param second_name:
    :param age:
    :return:
    """
    count_all_users = api.get_users_count()
    res = api.create_user(first_name, second_name, age)
    res_json = res.json()['data'][0]
    user_id = res_json.pop('id')
    assert res.status_code == 201

    assert res_json == {'first_name': first_name, 'second_name': second_name, 'age': age}
    count_all_users_after_add_empty_user = api.get_users_count()
    assert count_all_users == count_all_users_after_add_empty_user - 1

    res_user = api.get_user(user_id)
    res_user_json = res_user.json()['data'][0]
    res_user_json.pop('id')
    assert res_user_json == {'first_name': first_name, 'second_name': second_name, 'age': age}


# negative
@pytest.mark.parametrize('first_name, second_name, age', [('Aleksey', 'Alekseyvich', None),
                                                          ('Aleksey', None, 56),
                                                          (None, 'Alekseyvich', 56),
                                                          (None, None, 56),
                                                          (None, 'Alekseyvich', None),
                                                          ('Aleksey', None, None)])
def test_create_user_check_do_not_added_with_empty_values(api, first_name, second_name, age):
    """
    Проверяю добавление пользователя с пустыми значениями
    :param api:
    :param first_name:
    :param second_name:
    :param age:
    :return:
    """
    count_all_users = api.get_users_count()
    res = api.create_user(first_name, second_name, age)
    assert res.status_code != 201

    count_all_users_after_add_empty_user = api.get_users_count()
    assert count_all_users == count_all_users_after_add_empty_user


@pytest.mark.parametrize('first_name, second_name, age', [('Aleksey', 'Alekseyvich', '56'),
                                                          (15, 'Alekseyvich', 56),
                                                          ('Aleksey', 56, 56),
                                                          (56, 56, 56),
                                                          ('Aleksey', 56, 56),
                                                          ('Aleksey', 56, '56'),
                                                          ('Aleksey', 'Alekseyvich', -1),
                                                          ('Aleksey', 'Alekseyvich', 125),
                                                          ('!@#$%^&*()-~_+10', '!@#$%^&*()-~_+10', 125)])
def test_create_user_check_do_not_added_with_invalid_values(api, first_name, second_name, age):
    """
    Проверяю добавление пользователя с невалидными значениями
    :param api:
    :param first_name:
    :param second_name:
    :param age:
    :return:
    """
    count_all_users = api.get_users_count()
    res = api.create_user(first_name, second_name, age)
    assert res.status_code != 201

    count_all_users_after_add_empty_user = api.get_users_count()
    assert count_all_users == count_all_users_after_add_empty_user
