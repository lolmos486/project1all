from dao.user_dao import UserDao
from model.user import User
from exception.invalid_param import InvalidParamError


class UserService():
    def __init__(self):
        self.ud = UserDao()

# Create
#     def create_user(self, user_object):
#         return self.ud.create_user(user_object)


# Read - as employee, as finance manager

    def check_password(self, username, password):
        if username in self.ud.get_all_usernames():
            check = self.ud.check_password(username, password)
            print(check)
            if check:
                return {'id': check[0], 'role': check[6], 'first_name': check[3]}
            else:
                raise InvalidParamError("Password incorrect")
        else:
            raise InvalidParamError("Username not in database.")

    def get_user_info(self, username):
        return self.ud.get_user(username)

    def get_all_users(self):
        return self.ud.get_all_users()

# Update - as employee, as finance manager

    # def update_user(self, user_obj):
    #     return self.ud.update_user(user_obj)
    #
    # def update_password(self, user_id, old_pass, new_pass):
    #     return self.ud.update_password(user_id, old_pass, new_pass)

# Delete
#
#     def delete_user(self, user_id):
#         return self.ud.delete_user(user_id)