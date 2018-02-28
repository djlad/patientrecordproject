from flask import Blueprint, render_template

mainroutes = Blueprint("mainroutes", __name__)

@mainroutes.route('/')
def render_general_users_area():
    return render_template('general-users.html')

@mainroutes.route('/doctors')
def render_doctors_area():
    return 'doctors'

@mainroutes.route('/patients')
def render_patients_area():
    return 'patients'