from model.reimbursement import Reimbursement
import psycopg
import datetime


class ReimbDao:
    def __init__(self):
        pass

# Create
    def create_reimb(self, reimb_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO ers_reimbursement (reimb_amount, submitted, reimb_type, description, "
                            f"receipt, reimb_author, status) VALUES ('{reimb_obj.amount}', '{reimb_obj.submitted}', "
                            f"'{reimb_obj.type}', '{reimb_obj.descrip}', '{reimb_obj.receipt}', '{reimb_obj.author}', "
                            f"'{reimb_obj.status}');")
                conn.commit()
        return f"Reimbursement for {reimb_obj.amount} for {reimb_obj.type} submitted."

# Read
    def get_reimb(self, reimb_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM ers_reimbursement WHERE reimb_id = '{reimb_id}';")
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], line[8])
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    return reimb

    def get_reimbs(self, user_id, filter_status, filter_type):
        reimbs = []
       #print("dao: user_id = ", type(user_id), ", filter-status = ", type(filter_status), " filter type = ", filter_type)
        call = "SELECT * FROM ers_reimbursement INNER JOIN ers_users on ers_reimbursement.reimb_author = ers_users.user_id"
        if user_id or filter_status or filter_type:
            call = call + f" WHERE "
            if user_id:
                call = call + f"reimb_author = '{user_id}'"
                if filter_status or filter_type:
                    call = call + " AND "
            if filter_status:
                call = call + f"status = '{filter_status}'"
                if filter_type:
                    call = call + " AND "
            if filter_type:
                call = call + f"reimb_type = '{filter_type}'"
        call = call + " ORDER BY status DESC, submitted;"
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(call)
                for line in cur:
                    reimb = Reimbursement(line[1], line[2], line[5], line[6], line[7], f"{line[13]} {line[14]}")
                    reimb.set_id(line[0])
                    reimb.set_status(line[4])
                    reimb.set_resolved(line[3])
                    reimb.set_resolver(line[9])
                    # print("dao:", reimb)
                    reimbs.append(reimb)
                # print("in dao", reimbs)
                return reimbs


# Update
    def update_reimb_status(self, reimb_id, status, resolver):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE ers_reimbursement SET status = '{status}', resolved = "
                            f"'{datetime.datetime.now()}', reimb_resolver = '{resolver}' WHERE reimb_id = "
                            f"'{reimb_id}';")
                conn.commit()
                return f"Reimbursement request {reimb_id} has been {status}."



# Delete
    def delete_reimb(self, reimb_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM ers_reimbursement WHERE reimb_id = '{reimb_id}';")
                conn.commit()
            return f"Reimbursement {reimb_id} has been deleted."