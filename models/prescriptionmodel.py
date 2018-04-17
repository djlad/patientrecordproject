import pymysql
from models.dbconnect import Dbconnect
from models.queries import queries

class PresriptionModel(object):
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
                sql = queries["Add Prescription"].format(doctorID, patientID, prescription)
                cursor.execute(sql)
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
                sql = queries["Change Prescription"].format(doctorID, patientID, prescription)
                cursor.execute(sql)
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
                sql = queries["Remove Prescription"].format(doctorID, patientID, prescription)
                cursor.execute(sql)
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
                sql = queries["Get Patient Prescriptions"].format(patientID)
                cursor.execute(sql)
                # get result of prescriptions query
                result = cursor.fetchall()
        finally:
            connection.close()
        if result == None:
            return False
        else:
            return result