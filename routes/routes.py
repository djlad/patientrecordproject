from flask import Blueprint, render_template, request
from models.patientmodel import PatientModel

mainroutes = Blueprint("mainroutes", __name__)

@mainroutes.route('/')
def render_general_users_area():
    patient_model = PatientModel()
    patient_model.add_patient()
    #return render_template('general-users.html')
    return render_template('index.html')


@mainroutes.route('/adduser')
def add_user():
    request = {
        "username":"sample username",
        'password':"sample password"
    }
    userModel.addUser(request["username"], request["password"])
    return 'doctors'

@mainroutes.route('/patients')
def render_patients_area():
    return 'patients'