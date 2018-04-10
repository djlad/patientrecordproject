import pymysql
from models.queries import queries

class PatientModel(object):
    def __init__(self):
        pass

    def add_patient(self):
        print(queries["Create Patients Table"])
        return "add patient success"