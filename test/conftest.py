import pytest
from user_class import User

@pytest.fixture(scope='function')
def app_user():
    app_user = User(first_name='Bob', last_name='Parker', email_address="bob.parker@gmail.com", username="Bobtheboss")
    app_user.password_hash = '1234'
    yield app_user

