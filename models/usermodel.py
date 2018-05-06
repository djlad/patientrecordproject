import pymysql
import hashlib
from models.dbconnect import Dbconnect
from models.patientmodel import PatientModel
from models.queries import queries

class UserModel(object):
    def __init__(self):
        pass
    
    def add_user(self, id, username, password, userType, permissionLevel):
        '''
        method to add a user to the system
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # create a new user index
                sql = queries["Add User"]
                passe = hashlib.sha256()
                passe.update(password.encode())
                cursor.execute(sql, (id, username, passe.hexdigest(), userType, int(permissionLevel)))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "add user success"

    def remove_user(self, id):
        '''
        method to remove user from system
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # remove user from database
                sql = queries["Remove User"]
                cursor.execute(sql, (id))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            # remove patient pertaining to user
            PatientModel().remove_patient(id)
        finally:
            connection.close()
        return "remove user success"

    def change_username(self, newUsername, username, password):
        '''
        method to change username of user
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # modify user's username with inputted credentials
                sql = queries["Change Username"]
                passe = hashlib.sha256()
                passe.update(password.encode())
                cursor.execute(sql, (newUsername, username, passe.hexdigest()))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
        return "username changed success"
    
    def confirm_credentials(self, username, password):
        '''
        method to confirm inputted credentials against those stored on database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # confirm account credentials
                sql = queries["Confirm Credentials"]
                passe = hashlib.sha256()
                passe.update(password.encode())
                cursor.execute(sql, (username, passe.hexdigest()))
                # get result of confirming credentials
                result = cursor.fetchone()
        finally:
            connection.close()
        return result
    
    def get_last_entry(self):
        '''
        method to get last entry stored on database
        '''
        connection = Dbconnect.get_connection()
        try:
            with connection.cursor() as cursor:
                # confirm account credentials
                sql = queries["Get Last User"]
                cursor.execute(sql)
                # get result of confirming credentials
                result = cursor.fetchone()
        finally:
            connection.close()
        return result