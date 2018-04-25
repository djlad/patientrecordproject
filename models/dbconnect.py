import pymysql
import config


class Dbconnect(object):
    host = ''
    user = ''
    password = ''
    db_name = ''
    connection = None

    @staticmethod
    def set_db_info(config):
        Dbconnect.host = config['DATABASE_URI']
        Dbconnect.user = config['USERNAME']
        Dbconnect.password = config['PASSWORD']
        Dbconnect.db_name = config['DATABASE']
    
    @staticmethod
    def get_connection():
        print('hi')
        print(Dbconnect.host)
        connection = pymysql.connect(host=Dbconnect.host,
                                    user=Dbconnect.user,
                                    password=Dbconnect.password,
                                    db=Dbconnect.db_name,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        return connection

config_dic = vars(config.Config)["__annotations__"]
Dbconnect.set_db_info(config_dic)