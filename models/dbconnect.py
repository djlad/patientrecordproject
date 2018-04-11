import pymysql


class Dbconnect(object):
    host = ''
    user = ''
    password = ''
    db_name = ''
    connection = None

    def set_db_info(config):
        Dbconnect.host = config['DATABASE_URI']
        Dbconnect.user = config['USERNAME']
        Dbconnect.password = config['PASSWORD']
        Dbconnect.db_name = config['DATABASE']
    
    def get_connection():
        connection = pymysql.connect(host=Dbconnect.host,
                                    user=Dbconnect.user,
                                    #password=Dbconnect.password,
                                    db=Dbconnect.db_name,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        return connection