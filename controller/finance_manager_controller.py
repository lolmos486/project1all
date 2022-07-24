from flask import Blueprint, request, session, render_template, redirect, url_for, current_app, send_from_directory
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from exception.invalid_param import InvalidParamError
import json
from flask_cors import CORS


fmc = Blueprint('finance_manager_controller', __name__)
rs = ReimbService()

# As a finance manager, I want to be able to view and approve reimbursement requests

@fmc.route('/fm/reimbursements')
def get_all_reimbs_fm():
    if "user" in session:
        print("in fmc /fm/reimbursements:: session ~~ ", session)
        status = request.args.get('filter-status')
        filter_type = request.args.get('filter-type')
        if status == 'all-statuses':
            status = None
        if filter_type == 'all-types':
            filter_type = None
        try:
            reimbs = rs.get_all_reimbs(None, status, filter_type, session['user']['role'])
            to_return = {"reimbs": []}

            for re in reimbs:
                to_return["reimbs"].append(re.to_dict())

            json_return = json.dumps(to_return)
            # json_return = json_return.replace("'",'"')
            # print("to_return from fmc : ", json_return)
            return json_return, 201
        except InvalidParamError as e:
            return {
                       'message': f"{e}"
                   }, 400
    else:
        return {
            'message': 'must be logged in'
        }, 401


@fmc.route('/fm/reimbursements', methods=['PUT'])
def approve_reimbs():
    print("from fm/reimb PUT ", session)
    if "user" in session:
        json_input = request.get_json()
        print("json input ~~ ", json_input)
        update_str = json.dumps(json_input['to_update']).replace("'","").replace('"',"")
        update_list = list(update_str.split(','))
        for reimb in update_list:
            rs.update_reimb_status(reimb, json_input['status'], session["user"]['id'])
        return {
            'message': f"Reimbursements {update_list} have been {json_input['status']}."
        }, 201
    else:
        return {
           'message': 'must be logged in'
       }, 401


@fmc.route('/get-receipt/<receipt>')
def get_receipt(receipt):
    print(receipt)
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], receipt, as_attachment=True)
