queries = {
    "Create Patients Table":
    '''
    CREATE TABLE Patients (name VARCHAR(20));
    ''',
    "Add Patient":
    '''
    INSERT INTO PatientInfo VALUES({},{},{},{},{},{},{},{},{},{},{});
    ''',
    "Get Patient Info":
    '''
    SELECT * FROM PatientInfo WHERE patientID={};
    ''',
    "Get Patient Info List":
    '''
    SELECT * FROM PatientInfo LIMIT {} OFFSET {};
    ''',
    "Change Patient Info":
    '''
    UPDATE PatientInfo SET `name`=%s, `weight`=%s, `address`=%s, `phone`=%s, `insurance`=%s, `height`=%s, medicalhistory=%s WHERE `patientID`=%s;
    ''',
    "Remove Patient":
    '''
    DELETE FROM PatientInfo WHERE patientID={};
    ''',
    "Add User":
    '''
    INSERT INTO user VALUES({}, {}, {}, {}, {});
    ''',
    "Remove User":
    '''
    DELETE FROM user WHERE userID={};
    ''',
    "Change Username":
    '''
    UPDATE user SET username={} WHERE username={} AND password={};
    ''',
    "Change Password":
    '''
    UPDATE user SET password={} WHERE username={} AND password={};
    ''',
    "Confirm Credentials":
    '''
    SELECT userID, userType, permissionLevel FROM user WHERE username={} AND password={};
    ''',
    "Create Appointment":
    '''
    INSERT INTO appointment VALUES({},{},"{}");
    ''',
    "Alter Appointment":
    '''
    UPDATE appointment SET time={} WHERE doctorID={},patientID={},time={};
    ''',
    "Remove Appointment":
    '''
    DELETE FROM appointment WHERE doctorID={},patientID={},time={};
    ''',
    "View Appointments":
    '''
    SELECT * FROM appointment WHERE doctorID={},patientID={},time={};
    ''',
    "Get Appointment List":
    '''
    SELECT appointment.time, patientInfo.name, appointment.doctorID
    FROM appointment
    INNER JOIN patientInfo ON appointment.patientID = patientInfo.patientID
    LIMIT {} OFFSET {};
    ''',
    #use this inner join when doctor id's are fixed
    #(right now the doctor ids don't match up to doctors)
    #--INNER JOIN doctorInfo ON appointment.doctorID = doctorInfo.doctorID
    "Add Prescription":
    '''
    INSERT INTO Prescription VALUES({},{},{});
    ''',
    "Change Prescription":
    '''
    UPDATE Prescription SET prescription={} WHERE doctorID={},patientID={},prescription={};
    ''',
    "Remove Prescription":
    '''
    DELETE FROM Prescription WHERE doctorID={},patientID={},prescription={);
    ''',
    "Get Patient Prescriptions":
    '''
    SELECT prescription FROM Prescription WHERE patientID={};
    ''',
    "Get Prescription List":
    '''
    SELECT * FROM prescription LIMIT {} OFFSET {}
    ''',
    "Add Doctor":
    '''
    INSERT INTO DoctorInfo VALUES({}, {}, {}, {});
    ''',
    "Change Doctor":
    '''
    UPDATE DoctorInfo SET `name`={}, `specialty`={}, `location`={};
    ''',
    "Get Doctor Info by Name":
    '''
    Select name,specialty,location FROM DoctorInfo WHERE name={};
    ''',
    "Get Doctor Info by Specialization":
    '''
    Select name,specialty,location FROM DoctorInfo WHERE specialty={};
    ''',
    "Get Doctor Info List":
    '''
    SELECT * FROM DoctorInfo LIMIT {} OFFSET {};
    ''',
    "Remove Doctor":
    '''
    DELETE FROM DoctorInfo WHERE doctorID={};
    '''
}