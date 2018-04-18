import pymysql
from models.dbconnect import Dbconnect
from models.queries import queries

class PatientModel(object):
    def __init__(self):
        pass

    def add_patient(self, ID, name, age, weight, gender, height, address, phone, medicalhistory, insurance, DOB):
        '''
        method to add a patient index to the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql =queries["Add Patient"].format(ID, name, age, weight, gender, height, address, phone, medicalhistory, insurance, DOB)
                cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add patient success"
    
    def remove_patient(self, ID):
        '''
        method to remove a patient index from the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql =queries["Remove Patient"].format(ID)
                cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "remove patient success"
    
    def get_patient_info_by_name(self, name):
        '''
        method to get patient information from the database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients with passed name
                sql = queries["Get Patient Info"].format(name)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
        return result
    
    def get_patient_info_list(self, limit, offset):
        '''
        method to get a list of patients from offset to limit
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients within defined limit and offset
                sql = queries["Get Patient Info List"].format(limit, offset)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
        return result
    
    def change_patient_info(self, name, weight, address, phone, insurance, ID):
        '''
        method to change patient information on database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients with passed name
                sql = queries["Change Patient Info"].format(name, weight, address, phone, insurance, ID)
                cursor.execute(sql)
        finally:
            connection.close()
        return "successfully altered patient info"