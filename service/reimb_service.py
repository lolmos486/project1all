from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
from exception.invalid_param import InvalidParamError

# Read
#     Employee: where reimb_author = employee_id
#     FM: where reimb_author = *

class ReimbService():
    def __init__(self):
        self.rd = ReimbDao()

# Create
    def create_reimb(self, reimb_object):
        return self.rd.create_reimb(reimb_object)


# Read - as employee, as finance manager

    def get_reimb(self, reimb_id):
        return self.rd.get_reimb()

    def get_all_reimbs(self, user_id, filter_status, filter_type, role):
        # print("service: user_id = ", user_id, ", filter-status = ", filter_status, " filter type = ", filter_type)
        if not user_id and not role == "finance_manager":
            raise InvalidParamError("You must be a finance manager to see all reimbursement requests.")
        return self.rd.get_reimbs(user_id, filter_status, filter_type)
        # to_return = []
        # print("in service", reimbs)
        # for re in reimbs:
        #     to_return.append(re.to_dict())
        #     print("service: ", re.to_dict())
        # print("to return from service ", to_return)
        # return to_return


# Update - as employee? as finance manager
    def update_reimb_status(self, reimb_id, status, resolver):
        return self.rd.update_reimb_status(reimb_id, status, resolver)

# Delete
    def delete_reimb(self, reimb_id):
        return self.rd.delete_reimb(reimb_id)