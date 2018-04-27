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
                sql =queries["Add Appointment"]
                cursor.execute(sql, (doctorid, patientid, appointmenttime))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add appointment success"
    
    def change_appointment(self, doctorid, patientid, appointmenttime):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql =queries["Change Appointment"]
                cursor.execute(sql, (doctorid, patientid, appointmenttime))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "change appointment success"
    
    def cancel_appointment(self,doctorid, patientid, appointmenttime):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["Remove Appointment"]
                cursor.execute(sql, (doctorid, patientid, appointmenttime))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "change appointment success"

    def view_appointment(self, doctorid, patientid):
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = queries["View Appointments"]
                cursor.execute(sql, (doctorid, patientid))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            result = cursor.fetchall()
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