queries = {
    "Create Patients Table":
    '''
    CREATE TABLE Patients (name VARCHAR(20));
    ''',
    "Add Patient":
    '''
    INSERT INTO PatientInfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    ''',
    "Get Patient Info":
    '''
    SELECT * FROM PatientInfo WHERE patientID=%s;
    ''',
    "Get Patient Info List":
    '''
    SELECT * FROM PatientInfo LIMIT %s OFFSET %s;
    ''',
    "Change Patient Info":
    '''
    UPDATE PatientInfo SET `name`=%s, `weight`=%s, `address`=%s, `phone`=%s, `insurance`=%s, `height`=%s, medicalhistory=%s WHERE `patientID`=%s;
    ''',
    "Remove Patient":
    '''
    DELETE FROM PatientInfo WHERE patientID=%s;
    ''',
    "Add User":
    '''
    INSERT INTO user VALUES(%s,%s,%s,%s,%s);
    ''',
    "Get Last User":
    '''
    SELECT * FROM user ORDER BY userID DESC LIMIT 1;
    ''',
    "Remove User":
    '''
    DELETE FROM user WHERE userID=%s;
    ''',
    "Change Username":
    '''
    UPDATE user SET username=%s WHERE username=%s AND password=%s;
    ''',
    "Change Password":
    '''
    UPDATE user SET password=%s WHERE username=%s AND password=%s;
    ''',
    "Confirm Credentials":
    '''
    SELECT * FROM user WHERE username=%s AND password=%s;
    ''',
    "Create Appointment":
    '''
    INSERT INTO appointment VALUES(%s,%s,%s,%s);
    ''',
    "Alter Appointment":
    '''
    UPDATE appointment SET `time`=%s WHERE `appointmentID`=%s;
    ''',
    "Get Appointment by ID":
    '''
    SELECT appointment.time, patientInfo.name as patient,
           appointment.appointmentID, doctorInfo.name as doctor
    FROM appointment
    INNER JOIN patientInfo ON appointment.patientID = patientInfo.patientID
    INNER JOIN doctorInfo ON appointment.doctorID = doctorInfo.doctorID
    WHERE appointmentID=%s;
    ''',
    "Get Appointments by patientID":
    '''
    SELECT appointment.time, patientInfo.name as patient,
           appointment.appointmentID, doctorInfo.name as doctor
    FROM appointment
    INNER JOIN patientInfo ON appointment.patientID = patientInfo.patientID
    INNER JOIN doctorInfo ON appointment.doctorID = doctorInfo.doctorID
    WHERE patientInfo.patientID=%s;
    ''',
    "Remove Appointment":
    '''
    DELETE FROM appointment WHERE appointmentID=%s;
    ''',
    "View Appointments":
    '''
    SELECT * FROM appointment WHERE doctorID=%s,patientID=%s,time=%s;
    ''',
    "Get Appointment List":
    '''
    SELECT appointment.time, patientInfo.name as patient,
           appointment.appointmentID, doctorInfo.name as doctor
    FROM appointment
    INNER JOIN patientInfo ON appointment.patientID = patientInfo.patientID
    INNER JOIN doctorInfo ON appointment.doctorID = doctorInfo.doctorID
    LIMIT %s OFFSET %s;
    ''',
    "Add Prescription":
    '''
    INSERT INTO Prescription VALUES(%s,%s,%s,%s);
    ''',
    "Change Prescription":
    '''
    UPDATE Prescription SET `prescription`=%s WHERE `prescriptionID`=%s;
    ''',
    "Remove Prescription":
    '''
    DELETE FROM Prescription WHERE `prescriptionID`=%s;
    ''',
    "Get Patient Prescriptions":
    '''
    SELECT prescription FROM Prescription WHERE patientID=%s;
    ''',
    "Get Prescription List":
    '''
    SELECT prescription.prescription, prescription.prescriptionID,
           doctorInfo.name as doctor, patientInfo.name as patient
    FROM prescription
    INNER JOIN patientInfo ON prescription.patientID = patientInfo.patientID
    INNER JOIN doctorInfo ON prescription.doctorID = doctorInfo.doctorID
    LIMIT %s OFFSET %s;
    ''',
    "Get Prescription by ID":
    '''
    SELECT * FROM prescription WHERE `prescriptionID`=%s;
    ''',
    "Add Doctor":
    '''
    INSERT INTO DoctorInfo VALUES(%s, %s, %s, %s);
    ''',
    "Change Doctor":
    '''
    UPDATE DoctorInfo SET `name`=%s, `specialty`=%s, `location`=%s WHERE DoctorID=%s;
    ''',
    "Get Doctor Info by Name":
    '''
    Select name,specialty,location FROM DoctorInfo WHERE name=%s;
    ''',
    "Get Doctor Info by Specialization":
    '''
    Select name,specialty,location FROM DoctorInfo WHERE specialty=%s;
    ''',
    "Get Doctor by ID":
    '''
    SELECT * FROM doctorInfo WHERE doctorID=%s;
    ''',
    "Get Doctor Info List":
    '''
    SELECT * FROM DoctorInfo LIMIT %s OFFSET %s;
    ''',
    "Remove Doctor":
    '''
    DELETE FROM DoctorInfo WHERE `doctorID`=%s;
    '''
}