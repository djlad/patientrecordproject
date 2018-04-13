from flask import Blueprint, render_template, request, url_for, redirect
from models.patientmodel import PatientModel

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