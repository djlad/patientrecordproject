import unittest
from models.patientmodel import PatientModel

class TestPatientModel(unittest.TestCase):
    def test_add_patient(self):
        pm = PatientModel()
        actual_output = pm.add_patient()
        self.assertEqual(actual_output, "add patient success")
    

if __name__=='__main__':
    unittest.main()
        