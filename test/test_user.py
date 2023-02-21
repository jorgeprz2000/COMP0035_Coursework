import hashlib
import pytest

def test_user_username_checker(app_user):
    username = app_user.username
    assert username == 'Bobtheboss'
    assert username != 'BOBTHEBOSS'
    assert username != "BobtheBoss"
    assert username != "D0lnUt"

def test_password_hash_throws_TypeError(app_user):
    with pytest.raises(TypeError):
        app_user.password_hash = 1234


def test_return_includes_correct_attributes(app_user):
    assert app_user.username in repr(app_user)
    assert app_user.email_address in repr(app_user)
    assert app_user.first_name and app_user.last_name in repr(app_user)
    assert app_user.password_hash not in repr(app_user)


def test_hash_password_works(app_user):
    assert app_user.password_hash != '1234'
    hashed_password = hashlib.sha256(str.encode('1234')).hexdigest()
    assert app_user.password_hash == hashed_password


def test_check_password(app_user):
    assert app_user.check_password('1234') == True
    assert app_user.check_password("12345") == False

