from service.reimb_service import ReimbService
import pytest
from model.reimbursement import Reimbursement


def test_create_reimb(mocker):
    def mock_rd_create_reimb(self, reimb_obj):
        return f"Reimbursement for {reimb_obj.amount} for {reimb_obj.type} submitted."

    mocker.patch('dao.reimb_dao.ReimbDao.create_reimb', mock_rd_create_reimb)

    r_obj = Reimbursement(10.23, '2022-07-26 06:40:27.310597', 'food', None, None, 3)
    rs = ReimbService()
    actual = rs.create_reimb(r_obj)

    assert actual == "Reimbursement for 10.23 for food submitted."

def test_get_reimb(mocker):
    def mock_rd_get_reimb(self, reimb_id):
        r_obj = Reimbursement(10.23, '2022-07-26 06:40:27.310597', 'food', None, None, 3)
        r_obj.set_id(reimb_id)
        return r_obj.to_dict()

    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb', mock_rd_get_reimb)
    rs = ReimbService()
    r_id = 1
    actual = rs.get_reimb(r_id)
    assert actual == {'amount': 10.23, 'date_resolved': 'None', 'date_submitted': '2022-07-26 06:40:27.310597',
                      'description': None, 'receipt': None, 'reimb_id': 1, 'resolver_id': None, 'status': 'pending',
                      'submitter_id': 3, 'type': 'food'}


def test_get_all_reimbs_e_suc(mocker):
    def mock_rd_get_reimbs(self, user_id, filter_status, filter_type):
        if user_id == 2:
            return['reimb1', 'reimb7']
        elif not user_id:
            return['reimb1', 'reimb2', 'reimb3', 'reimb7']
        else:
            return []

    mocker.patch('dao.reimb_dao.ReimbDao.get_reimbs', mock_rd_get_reimbs)
    rs = ReimbService()
    uid = 2
    f_status = None
    f_type = None
    actual = rs.get_all_reimbs(uid, f_status, f_type, 'employee')

    assert actual == ['reimb1', 'reimb7']

def test_get_all_reimbs_fm_suc(mocker):
    def mock_rd_get_reimbs(self, user_id, filter_status, filter_type):
        if user_id == 2:
            return['reimb1', 'reimb7']
        elif not user_id:
            return['reimb1', 'reimb2', 'reimb3', 'reimb7']
        else:
            return []

    mocker.patch('dao.reimb_dao.ReimbDao.get_reimbs', mock_rd_get_reimbs)
    rs = ReimbService()
    uid = None
    f_status = None
    f_type = None
    actual = rs.get_all_reimbs(uid, f_status, f_type, 'finance_manager')

    assert actual == ['reimb1', 'reimb2', 'reimb3', 'reimb7']

def test_get_all_reimbs_e_as_fm(mocker):
    def mock_rd_get_reimbs(self, user_id, filter_status, filter_type):
        if user_id == 2:
            return['reimb1', 'reimb7']
        elif not user_id:
            return['reimb1', 'reimb2', 'reimb3', 'reimb7']
        else:
            return []

    mocker.patch('dao.reimb_dao.ReimbDao.get_reimbs', mock_rd_get_reimbs)
    rs = ReimbService()
    uid = None
    f_status = None
    f_type = None

    with pytest.raises(Exception) as e:
        rs.get_all_reimbs(uid, f_status, f_type, 'employee')



