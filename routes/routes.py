from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from flask import current_app as app
from models.patientmodel import PatientModel
from models.dbconnect import Dbconnect
import json

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
    userModel.addUser(request["username"], request["password"])
    return 'doctors'

@mainroutes.route('/patients')
def render_patients_area():
    return 'patients'

@mainroutes.route('/getpatients', methods=['GET', 'Post'])
def get_patients():
    pm = PatientModel()
    patient_list = pm.get_patient_info_list()
    return jsonify(patient_list)


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
    entry = json.loads(req['entry'])
    pm.change_patient_info(entry['name'],
                           entry['weight'],
                           entry['address'],
                           entry['phone'],
                           entry['insurance'],
                           entry['height'],
                           entry['patientID'])
    return 'save finished'
