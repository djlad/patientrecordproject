import pymysql
from models.dbconnect import Dbconnect
from models.queries import queries

class PrescriptionModel(object):
    def __init__(self):
        pass
    
    def add_prescription(self, doctorID, patientID, prescription):
        '''
        method to add a new prescription index to database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # create a new user index
                sql = queries["Add Prescription"]
                cursor.execute(sql, (None, doctorID, patientID, prescription))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add prescription success"
    
    def change_prescription(self, prescriptionID, prescription):
        '''
        method to change an existing prescription index in the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # change prescription information
                sql = queries["Change Prescription"]
                cursor.execute(sql, (prescription, prescriptionID))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "edit prescription success"
    
    def remove_prescription(self, prescriptionID):
        '''
        method to remove a prescription from the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # cremove prescription from database
                sql = queries["Remove Prescription"]
                cursor.execute(sql, (prescriptionID))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "edit prescription success"
    
    def get_prescriptions_for_patient(self, patientID):
        '''
        method to get all precriptions for a certain patient
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all prescriptions assigned to a patient
                sql = queries["Get Patient Prescriptions"]
                cursor.execute(sql, (patientID))
                # get result of prescriptions query
                result = cursor.fetchall()
        finally:
            connection.close()
        return result
    
    def get_prescription_by_id(self, prescriptionID):
        '''
        method to get prescription by id
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all prescriptions assigned to a patient
                sql = queries["Get Prescription by ID"]
                cursor.execute(sql, (prescriptionID))
                # get result of prescriptions query
                result = cursor.fetchone()
        finally:
            connection.close()
        return result
    
    def get_prescription_info_list(self, limit=1000, offset = 0):
        '''
        method to get list of prescriptions
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients within defined limit and offset
                sql = queries["Get Prescription List"]
                cursor.execute(sql, (limit, offset))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result