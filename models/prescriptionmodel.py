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
                cursor.execute(sql, (doctorID, patientID, prescription))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add prescription success"
    
    def change_prescription(self, doctorID, patientID, prescription):
        '''
        method to change an existing prescription index in the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # change prescription information
                sql = queries["Change Prescription"]
                cursor.execute(sql, (doctorID, patientID, prescription))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "edit prescription success"
    
    def remove_prescription(self, doctorID, patientID, prescription):
        '''
        method to remove a prescription from the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # cremove prescription from database
                sql = queries["Remove Prescription"]
                cursor.execute(sql, (doctorID, patientID, prescription))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "edit prescription success"
    
    def get_prescriptions(self, patientID):
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
        if result == None:
            return False
        else:
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