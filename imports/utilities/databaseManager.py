import sqlite3

class DatabaseManager():

    def __init__(self, sql_database_path):
        self.__sql_database_path = sql_database_path
        self.__conn = sqlite3.connect(self.__sql_database_path)


    def getUsersList(self):
        self.__conn = sqlite3.connect(self.__sql_database_path)
        cur = self.__conn.cursor()
        try:
            cur.execute("SELECT {c1} FROM {tn}". \
                        format(tn='devices', c1='BLE_address'))

            query_result = cur.fetchall()

            print('BBBB ',query_result)
        except sqlite3.Error as e:
            self.__conn.close()
            message = 'SQL Integrity error ' + str(e)
            return 11, message

        users = []
        for row in query_result:
            users.append(row[0])

        return 0,users