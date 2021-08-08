import pytest


def test_delete_user_by_body(api):
    """
    Проверка удадления пользователя с указанием id в теле запроса
    :param api:
    :return:
    """
    user_id = 2
    count_all_users = api.get_users_count()
    res = api.delete_user_by_body(user_id=user_id)
    assert res.status_code == 200

    count_all_users_after_del_empty_user = api.get_users_count()
    assert count_all_users == count_all_users_after_del_empty_user + 1, 'Количество пользователей не изменилось'

    res_user = api.get_user(user_id=user_id)
    assert res_user.status_code == 404


@pytest.mark.parametrize('user_id', [200, -1])
def test_delete_user_by_body_do_not_exist(api, user_id):
    """
    Проверка удадления несуществуещего пользователя с указанием id в теле запроса
    :param api:
    :return:
    """
    count_all_users = api.get_users_count()
    res = api.delete_user_by_body(user_id=user_id)
    assert res.status_code == 404

    count_all_users_after_del_empty_user = api.get_users_count()
    assert count_all_users == count_all_users_after_del_empty_user, 'Количество пользователей изменилось'