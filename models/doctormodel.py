import pymysql
from models.dbconnect import Dbconnect
from models.queries import queries

class DoctorModel(object):
    def __init__(self):
        pass
    
    def add_doctor(self, doctorID, name, specialty, location):
        '''
        method to add doctor index tot database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # create a new user index
                sql = queries["Add Doctor"]
                cursor.execute(sql, (doctorID, name, specialty, location))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add doctor success"

    def change_doctor_info(self, name, specialty, location):
        '''
        method to modify existing doctor index
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # create a new user index
                sql = queries["Change Doctor"]
                cursor.execute(sql, (name, specialty, location))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "change doctor success"
    
    def get_doctor_info_by_name(self, name):
        '''
        method to get doctor information by name
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all prescriptions assigned to a patient
                sql = queries["Get Doctor Info by Name"]
                cursor.execute(sql, (name))
                # get result of prescriptions query
                result = cursor.fetchall()
        finally:
            connection.close()
        if result == None:
            return False
        else:
            return result
    
    def get_doctor_info_by_specialization(self, specialization):
        '''
        method to get doctor information by specialization
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all prescriptions assigned to a patient
                sql = queries["Get Doctor Info by Specialization"]
                cursor.execute(sql, (specialization))
                # get result of prescriptions query
                result = cursor.fetchall()
        finally:
            connection.close()
        if result == None:
            return False
        else:
            return result
    
    def get_doctor_info_list(self, limit=1000, offset=0):
        '''
        method to get a list of doctorInfo from offset to limit
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients within defined limit and offset
                sql = queries["Get Doctor Info List"]
                cursor.execute(sql, (limit, offset))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result
    
    def remove_patients(self, doctorID):
        '''
        remove doctor from database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all prescriptions assigned to a patient
                sql = queries["Remove Doctor"]
                cursor.execute(sql, (doctorID))
        finally:
            connection.close()
        return "remove doctor success"