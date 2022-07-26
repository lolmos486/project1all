from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
import datetime
from dao.user_dao import UserDao
from model.user import User
from service.user_service import UserService
from service.reimb_service import ReimbService


#(self, amount, submitted, type, descrip, receipt, author)

now = datetime.datetime.now()
re = Reimbursement(12.50, now, "other", "trololol", "idgaf", 4)
us = UserService()
rs = ReimbService()
ud = UserDao()

#
#
# users = us.get_all_users()
# for elem in users:
#     print(elem)

# get_reimb = rs.get_all_reimbs(None, None, None, 'finance_manager')
# for reimb in get_reimb:
#     print(reimb)

print(ud.check_password('bob45', 'babyz'))
# print(us.check_password('bob45', 'baby'))
# print(us.check_password('bob4', 'babyz'))






