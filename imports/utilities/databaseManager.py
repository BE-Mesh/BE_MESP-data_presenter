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

        except sqlite3.Error as e:
            self.__conn.close()
            message = 'SQL Error ' + str(e)
            return 1, message

        users = []
        for row in query_result:
            users.append(row[0])

        return 0,users

    def getSentMessageEvents(self,device_id,type):
        self.__conn = sqlite3.connect(self.__sql_database_path)
        cur = self.__conn.cursor()

        try:
            # SELECT * FROM events JOIN typeEvent_message_sent ON events.event_id = typeEvent_message_sent.event_id WHERE( events.submitter_id='AAAAA' and events.type = 0 and typeEvent_message_sent.message_type=0)

            cur.execute("SELECT * FROM {tn} "
                        "JOIN typeEvent_message_sent ON events.event_id = typeEvent_message_sent.event_id "
                        "WHERE( events.submitter_id='{submitter_id}' and events.type = {type} and typeEvent_message_sent.message_type=0)". \
                        format(tn='events', submitter_id=device_id, type=type))

            query_result = cur.fetchall()

        except sqlite3.Error as e:
            self.__conn.close()
            message = 'SQL Error ' + str(e)
            return 1, message



        return 0, query_result