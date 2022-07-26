from flask import Blueprint, request, session, redirect, url_for, current_app, jsonify
from flask_cors import cross_origin
from service.user_service import UserService
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from model.user import User
from exception.invalid_param import InvalidParamError
from controller.user_controller import uc
import json
import datetime
from werkzeug.utils import secure_filename
import os

ec = Blueprint('employee_controller', __name__)
us = UserService()
rs = ReimbService()

# As an employee, I want to be able to submit and review my reimbursement requests

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ec.route('/e/reimbursements')
def get_all_reimbs_e():
    if "user" in session:
        # print("in ec /e/reimbursements:: session ~~ ", session)
        status = request.args.get('filter-status')
        filter_type = request.args.get('filter-type')
        if status == 'all-statuses':
            status = None
        if filter_type == 'all-types':
            filter_type = None
        try:
            reimbs = rs.get_all_reimbs(session['user']['id'], status, filter_type, session['user']['role'])
            to_return = {"reimbs": []}

            for re in reimbs:
                to_return["reimbs"].append(re.to_dict())

            # print("to_return from ec : ", to_return)
            return to_return, 201
        except InvalidParamError as e:
            return {
                'message': f"{e}"
            }, 400
    else:
        return {
            'message': 'must be logged in'
        }, 401


@ec.route('/e/reimbursement', methods=['POST'])
def submit_reimb():
    if "user" in session:
        print("ec.route/e/reimbursements ~~ ", session)
        time = datetime.datetime.now()
        amount= request.form.get('amount')
        type = request.form.get('type')
        descrip = request.form.get('description')
        print(amount)
        print("form: ", request.form.keys())
        print("files: ", request.files)
        print(request.args.to_dict())
        if 'receipt' in request.files.keys():
            receipt = request.files['receipt']
            receiptExt = receipt.filename.rsplit('.', 1)[1].lower()
            filename = f'{time}{type}{session["user"]["id"]}'
            filename = filename.replace("-", "").replace(':', '').replace(' ', '').replace('.', '') + '.' + receiptExt
            print(filename)
            receipt.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        else:
            raise InvalidParamError('must submit receipt.')
        print(amount, ", ", time, ", ", type, ", ", descrip, ", ", filename, ", ", session['user']['id'])
        reimb = Reimbursement(amount, time, type, descrip, filename, session['user']['id'])
        print(reimb.to_dict())
        rs.create_reimb(reimb)
        response = jsonify(mesage="reimbursement submitted")
        print(response.headers)
        return {
            'message': 'worked'
        }, 201
    else:
        return {
             'message': 'must be logged in'
        }, 401

