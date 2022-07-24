from model.user import User
import psycopg

class UserDao:
    def __init__(self):
        pass

# Create
    def create_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO ers_users (username, password, first_name, last_name, email, role) "
                            f"VALUES ('{user_object.username}', '{user_object.password}', '{user_object.fname}', "
                            f"'{user_object.lname}', '{user_object.email}', '{user_object.role}');")
                conn.commit()
                return f"User {user_object.username} has been added to the system."

# Read
    def get_user(self, username):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_users WHERE username = '{username}';")
                for line in cur:
                    user = User(line[1], line[2], line[3], line[4], line[5], line[6])
                    user.set_user_id(line[0])
                    return user

    def check_password(self, username, password):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_users WHERE username = '{username}' "
                            f"AND password = crypt('{password}', password);")
                return cur.fetchone()

    def get_all_users(self):
        users = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_users")
                for line in cur:
                    user = User(line[1], line[2], line[3], line[4], line[5], line[6])
                    user.set_user_id(line[0])
                    users.append(user.to_dict())
                return users

    def get_all_usernames(self):
        users = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_users")
                for line in cur:
                    users.append(line[1])
                return users
# Update
    def update_user(self, user_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE ers_users SET first_name = '{user_obj.fname}', last_name = "
                            f"'{user_obj.lname}', email = '{user_obj.email}', role = '{user_obj.role}' WHERE "
                            f"user_id = {user_obj.user_id} AND password = crypt('{user_obj.password}', password);")
                conn.commit()
            return f"User {user_obj.username} has been updated. {user_obj}"

    def update_password(self, user_id, old_pass, new_pass):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE ers_users SET password = crypt('{new_pass}', gen_salt('bf')) WHERE "
                            f"user_id = {user_id} AND password = crypt('{old_pass}', password);")
                conn.commit()
                return "Password updated"

# Delete
    def delete_user(self, user_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE * FROM ers_users WHERE user_id = {user_id};")
                conn.commit()
            return f"User {user_id} deleted"
