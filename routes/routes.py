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
<<<<<<< Updated upstream
    print(userInfo)
=======
    # get inputted data from login form
>>>>>>> Stashed changes
    username = userInfo['username']
    password = userInfo['password']
    # create a usermodel object
    um = UserModel()
    # confirm credentials to those on server
    userInfo = um.confirm_credentials(username, password)
<<<<<<< Updated upstream
    if userInfo == None:
=======
    # if uaerInfo == None, set isvalid flag to false, otherwise set to true
    if not userInfo:
>>>>>>> Stashed changes
        isvalid = False
    else:
        isvalid = True
    # if isvalid is true, return json of information, otherwise return invalid credentials
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
<<<<<<< Updated upstream
=======
    print(entryType)
>>>>>>> Stashed changes
    if entryType == 'patient':
        pm = PatientModel()
        info = pm.get_patient_info_by_id(id)
    elif entryType == 'doctor':
        dm = DoctorModel()
        info = dm.get_doctor_by_id(id)
        #info = [{'testdata':'placeholder'}]
    elif entryType == 'appointment':
        am = AppointmentModel()
        info = am.get_appointment_by_id(id)
        #info = [{'testdata':'placeholder'}]
    elif entryType == 'prescription':
        pm = PrescriptionModel()
        info = pm.get_prescription_by_id(id)
        #info = [{'testdata':'placeholder'}]
    return jsonify(info)

@mainroutes.route('/save', methods=['Post'])
def save_entry():
    req = request.get_json()
    entryType = request.form['entryType']
    if 'patient':
        pm = PatientModel()
        pm.change_patient_info(entry['name'],
                           entry['weight'],
                           entry['address'],
                           entry['phone'],
                           entry['insurance'],
                           entry['height'],
                           entry['medicalhistory'],
                           entry['patientID'])
    elif 'doctor':
        dm = DoctorModel()
        dm.change_doctor_info(entry['name'], 
                           entry['specialty'], 
                           entry['location'])
<<<<<<< Updated upstream
=======
    elif entryType == 'appointment':
        am = AppointmentModel()
        am.change_appointment(entry['appointmentID'],
                            entry["time"])
    elif entryType == 'prescription':
        pm = PrescriptionModel()
        pm.change_prescription(entry['prescriptionID'],
                            entry['prescription'])
        print(entry)
>>>>>>> Stashed changes
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
    elif entryType == 'prescription':
        pm = PrescriptionModel()
        pm.add_prescription(0,0,"")
    elif entryType == 'appointment':
        am = AppointmentModel()
        am.make_appointment(0,0,"1111-11-11 11:11:11")
    return 'entry saved'

<<<<<<< Updated upstream
=======

@mainroutes.route('/deleteentry', methods=['Post'])
def delete_entry():
    entryType = request.form['entryType']
    ID = request.form['ID']
    if entryType == 'patient':
        print(entryType)
        print(ID)
        pm = PatientModel()
        pm.remove_patient(ID)
    elif entryType == 'doctor':
        print(entryType)
        print(ID)
        dm = DoctorModel()
        dm.remove_patients(ID)
    elif entryType == 'prescription':
        print(entryType)
        print(ID)
        pm = PrescriptionModel()
        pm.remove_prescription(ID)
    elif entryType == 'appointment':
        print(entryType)
        print(ID)
        am = AppointmentModel()
        am.cancel_appointment(ID)
    return 'entry deleted'

>>>>>>> Stashed changes
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