class User:
    def __init__(self, username, password, fname, lname, email, role):
        self.user_id = 0
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.role = role

    def set_user_id(self, uid):
        self.user_id = uid

    def to_dict(self):
        return {
            'user id': self.user_id,
            'username': self.username,
            'first name': self.fname,
            'last name': self.lname,
            'email': self.email,
            'role': self.role
        }

    def __str__(self):
        return f"User {self.username} ({self.user_id}): {self.fname} {self.lname}. {self.role}, {self.email}."

    def update_password(self, new_pass):
        self.password = new_pass





    