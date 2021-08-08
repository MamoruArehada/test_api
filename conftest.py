import pytest
from client import APIClient


@pytest.fixture(scope='function')
def api():
    host = 'http://127.0.0.1:5000'
    return APIClient(host=host)
