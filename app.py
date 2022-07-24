from flask import Flask
from flask_cors import CORS
from flask_session import Session
from controller.employee_controller import ec
from controller.user_controller import uc
from controller.finance_manager_controller import fmc

UPLOAD_FOLDER = './receipts'



if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = "hello"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_ORIGINS'] = ['http://127.0.0.1:5503']
    CORS(app)
    Session(app)
    app.register_blueprint(uc)
    app.register_blueprint(ec)
    app.register_blueprint(fmc)

    app.run(port=8080, debug=True)
