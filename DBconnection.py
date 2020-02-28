import pymysql

class DBConnection():

    @staticmethod
    def getConnection():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', db='inventaris')

            return conn
        except Exception as e:
            print(e)