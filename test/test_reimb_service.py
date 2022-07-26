from service.reimb_service import ReimbService
import pytest
from model.reimbursement import Reimbursement
import datetime

def test_create_reimb(mocker):
    def mock_rd_create_reimb(self, reimb_obj):
        return f"Reimbursement for {reimb_obj.amount} for {reimb_obj.type} submitted."

    mocker.patch('dao.reimb_dao.ReimbDao.create_reimb', mock_rd_create_reimb)

    r_obj = Reimbursement(10.23, datetime.datetime.now(), 'food', None, None, 3)
    rs = ReimbService()
    actual = rs.create_reimb(r_obj)

    assert actual == "Reimbursement for 10.23 for food submitted."

def test_get_reimb(mocker):
    def mock_rd_get_reimb(self, reimb_id):
        r_obj = Reimbursement(10.23, datetime.datetime.now(), 'food', None, None, 3)
        r_obj.set_id(reimb_id)
        return r_obj

    mocker.patch('dao.reimb_dao.ReimbDao.get_reimb', mock_rd_get_reimb)
    rs = ReimbService()
    r_id = 1
    actual = rs.get_reimb(r_id)
    assert actual == '<model.reimbursement.Reimbursement object at 0x0000024E36CE58B0>'

