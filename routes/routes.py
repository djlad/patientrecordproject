from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from flask import current_app as app
from models.patientmodel import PatientModel
from models.usermodel import UserModel
from models.doctormodel import DoctorModel
from models.appointmentmodel import AppointmentModel
from models.prescriptionmodel import PrescriptionModel
from models.dbconnect import Dbconnect
import random
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
    UserModel.add_user(request["username"], request["password"])
    return 'doctors'



@mainroutes.route('/login', methods=['Post'])
def login():
    userInfo = request.get_json()
    username = userInfo['username']
    password = userInfo['password']
    #TODO: this function must verify the username/password
    #and return the userInfo of this user.
    um = UserModel()
    userInfo = um.confirm_credentials(username, password)
    print('userInfo')
    print(userInfo)
    if not userInfo:
        isvalid = False
    else:
        isvalid = True
    if isvalid:
        return jsonify(userInfo)
    else:
        return 'invalid credentials'

@mainroutes.route('/getpatients', methods=['GET', 'Post'])
def get_patients():
    pm = PatientModel()
    patient_list = pm.get_patient_info_list()
    return jsonify(patient_list)

@mainroutes.route('/getentries', methods=['GET', 'Post'])
def get_entries():
    entryType = request.form['entryType']
    print(entryType)
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
    else:
        entry_list = [{'error':'invalid entry request'}]
    return jsonify(entry_list)


@mainroutes.route('/getentrybyid', methods=['Post'])
def get_entry_by_id():
    id = request.form['id']
    entryType = request.form['entryType']
    print('hello world')
    print(entryType)
    if entryType == 'patient':
        pm = PatientModel()
        info = pm.get_patient_info_by_id(id)
    elif entryType == 'doctor':
        dm = DoctorModel()
        info = [{'testdata':'placeholder'}]
    elif entryType == 'appointment':
        am = AppointmentModel()
        info = [{'testdata':'placeholder'}]
    elif entryType == 'prescription':
        pm = PrescriptionModel()
        info = [{'testdata':'placeholder'}]
    return jsonify(info)

@mainroutes.route('/save', methods=['Post'])
def save_entry():
    req = request.get_json()
    entryType = req['entryType']
    entry = req['entry']

    if entryType == 'patient':
        pm = PatientModel()
        pm.change_patient_info(entry['name'],
                           entry['weight'],
                           entry['address'],
                           entry['phone'],
                           entry['insurance'],
                           entry['height'],
                           entry['medicalhistory'],
                           entry['patientID'])
    elif entryType == 'doctor':
        dm = DoctorModel()
        dm.change_doctor_info(entry['name'], 
                           entry['specialty'], 
                           entry['location'])
    elif entryType == 'appointment':
        print(entry)
        
    return 'save finished'


@mainroutes.route('/addentry', methods=['Post'])
def addEntry():
    entryType = request.form['entryType']
    if entryType == 'patient':
        '''
        1. create usermodel object
        2. add a new user
        3. get just added user
        4. create patientmodel object
        5. add a default patient entry
        return
        '''
        um = UserModel()
        um.add_user(None,random_garbage(),random_garbage(),"patient", 3)
        lastEntry = um.get_last_entry()
        pm = PatientModel()
        pm.add_patient(lastEntry['userID'],"",0,0,"",0,"","","","","1111-11-11")
    elif entryType == "doctor":
        '''
        1. create usermodel object
        2. add a new user
        3. get just added user
        4. create doctormodel object
        5. add a default doctor entry
        return
        '''
        um = UserModel()
        um.add_user(None,random_garbage(),random_garbage(),"doctor", 2)
        lastEntry = um.get_last_entry()
        dm = DoctorModel()
        dm.add_doctor(lastEntry['userID'],"","","")
    return 'entry saved'


@mainroutes.route('/deleteentry', methods=['Post'])
def delete_user():
    entryType = request.form['entryType']
    ID = request.form['ID']
    print(entryType)
    print(ID)
    return 'entry deleted'

def random_garbage():
    '''
    function to create a random username and password when creating a new user
    '''
    returnString = ""
    junk = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX1234567890@_-+="
    for i in range(0, 10):
        rand = random.randint(0, len(junk)-1)
        returnString+=junk[rand]
    return returnString