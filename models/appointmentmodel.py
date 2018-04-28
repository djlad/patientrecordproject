import pymysql
from models.dbconnect import Dbconnect
from models.queries import queries

class AppointmentModel(object):
    def __init__(self):
        pass
    
    def make_appointment(self, doctorid, patientid, appointmenttime):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["Add Appointment"]
                cursor.execute(sql, (None, doctorid, patientid, appointmenttime))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add appointment success"
    
    def change_appointment(self, appointmentID, appointmenttime):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["Change Appointment"]
                cursor.execute(sql, (appointmenttime, appointmentID))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "change appointment success"
    
    def cancel_appointment(self, appointmentID):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["Remove Appointment"]
                cursor.execute(sql, (appointmentID))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "change appointment success"

    def get_appointment_by_id(self, appointmentID):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["Get Appointment by ID"]
                cursor.execute(sql, (appointmentID))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
        
    def get_appointment_info_list(self, limit=1000, offset = 0):
        '''
        method to get list of appointments
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # get all patients within defined limit and offset
                sql = queries["Get Appointment List"]
                cursor.execute(sql, (limit, offset))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result