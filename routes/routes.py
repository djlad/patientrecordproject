from flask import Blueprint, render_template, request, url_for, redirect
from models.patientmodel import PatientModel
<<<<<<< Updated upstream
=======
from models.usermodel import UserModel
from models.doctormodel import DoctorModel
from models.appointmentmodel import AppointmentModel
from models.prescriptionmodel import PrescriptionModel
from models.dbconnect import Dbconnect
import json
>>>>>>> Stashed changes

mainroutes = Blueprint("mainroutes", __name__)

@mainroutes.route('/')
def render_general_users_area():
    return redirect(url_for('static', filename='index.html'))

@mainroutes.route('/adduser')
def add_user():
    request = {
        "username":"sample username",
        'password':"sample password"
    }
    UserModel.add_user(request["username"], request["password"])
    return 'doctors'

<<<<<<< Updated upstream
@mainroutes.route('/patients')
def render_patients_area():
    return 'patients'
=======
@mainroutes.route('/getpatients', methods=['GET', 'Post'])
def get_patients():
    pm = PatientModel()
    patient_list = pm.get_patient_info_list()
    return jsonify(patient_list)

@mainroutes.route('/get', methods=['GET', 'Post'])
def get_entries():
    entryType = request.form['entryType']
    if entryType == 'patient':
        pm = PatientModel()
        entry_list = pm.get_patient_info_list()
    elif entryType == 'doctor':
        dm = DoctorModel()
        entry_list = dm.get_doctor_info_list()
    elif entryType == 'appointment':
        am = AppointmentModel()
        entry_list = am.get_appointment_info_list()
    elif entryType == 'prescription':
        pm = PrescriptionModel()
        entry_list = pm.get_prescription_info_list()
    return jsonify(entry_list)


@mainroutes.route('/getpatientbyid', methods=['Post'])
def get_patient_by_id():
    pm = PatientModel()
    id = request.form['id']
    patientInfo = pm.get_patient_info_by_id(id)
    return jsonify(patientInfo)

@mainroutes.route('/save', methods=['Post'])
def save_entry():
    pm = PatientModel()
    req = request.get_json()
    entry = req['entry']
    print(req['userInfo'])
    pm.change_patient_info(entry['name'],
                           entry['weight'],
                           entry['address'],
                           entry['phone'],
                           entry['insurance'],
                           entry['height'],
                           entry['medicalhistory'],
                           entry['patientID'])
    return 'save finished'


@mainroutes.route('/addentry', methods=['Post'])
def addEntry():
    entryType = request.form['entryType']
    '''
    1. get last user
    2. increment id by 1
    3. add respective user type
    '''
    if entryType == 'patient':
        pass
    return 'entry saved'
>>>>>>> Stashed changes
