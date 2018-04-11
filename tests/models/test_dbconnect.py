import unittest
from models.dbconnect import Dbconnect
from config import Config


class TestDbconnect(unittest.TestCase):
    def test_init(self):
        config = Config.__annotations__
        Dbconnect.set_db_info(config)
        con = Dbconnect.get_connection()
        con.close()