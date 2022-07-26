import pytest
from service.user_service import UserService

def test_chk_pwd_val_val(mocker):
    def mock_ud_chk_pwd(self, usn, pwd):
        if usn == "bob45" and pwd == "babyz":
            return (1, 'bob45', '$2a$06$dL6QNuXIa3KIw6w1XLapLul8WrqnvvERtmp.YOxDsoca9TZxhbtHW', 'Bob',
                     'Wehadababyitsaboy', None, 'finance_manager')
        else:
            return []

    mocker.patch('dao.user_dao.UserDao.check_password', mock_ud_chk_pwd)
    us = UserService()
    usn = 'bob45'
    pwd = 'babyz'
    actual = us.check_password(usn, pwd)
    assert actual == {'id': 1, 'role': 'finance_manager', 'first_name': 'Bob'}

def test_chk_pwd_val_inval(mocker):
    def mock_ud_chk_pwd(self, usn, pwd):
        if usn == "bob45" and pwd == "babyz":
            return (1, 'bob45', '$2a$06$dL6QNuXIa3KIw6w1XLapLul8WrqnvvERtmp.YOxDsoca9TZxhbtHW', 'Bob',
                     'Wehadababyitsaboy', None, 'finance_manager')
        else:
            return []

    mocker.patch('dao.user_dao.UserDao.check_password', mock_ud_chk_pwd)
    us = UserService()
    usn = 'bob45'
    pwd = 'baby'
    with pytest.raises(Exception) as e:
        us.check_password(usn, pwd)


def test_chk_pwd_inval_inval(mocker):
    def mock_ud_chk_pwd(self, usn, pwd):
        if usn == "bob45" and pwd == "babyz":
            return (1, 'bob45', '$2a$06$dL6QNuXIa3KIw6w1XLapLul8WrqnvvERtmp.YOxDsoca9TZxhbtHW', 'Bob',
                     'Wehadababyitsaboy', None, 'finance_manager')
        else:
            return []

    mocker.patch('dao.user_dao.UserDao.check_password', mock_ud_chk_pwd)
    us = UserService()
    usn = 'bob4'
    pwd = 'baby'
    with pytest.raises(Exception) as e:
        us.check_password(usn, pwd)