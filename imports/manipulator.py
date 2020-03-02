from .utilities.singleton import Singleton
from .utilities.databaseManager import DatabaseManager
from .inputDAO import InputDAO


class Manipulator(metaclass=Singleton):
    def __init__(self):

        inputdao = InputDAO()
        subdir =inputdao.getSubdirectoriesList()

        subdirectories_list= inputdao.getSubdirectoriesList()

        for subdir in subdirectories_list:
            res = self.manageSubcase(subdir)
            if res[0] != 0:
                err_code = '3C'  # C stands for custom
                err_mess = 'ERROR WHILE PROCESSING SUBDIR: ' + str(subdir)
                err_details = 'ErroDetails: ' + res[1]
                raise Exception(err_code, err_mess, err_details)



    def manageSubcase(self,subdir):

        inputdao = InputDAO()

        res = inputdao.getFilesInDirectory(subdir)

        if res[0] != 0:
            return res

        if len(res[1]) < 1:
            return 2,'Empty subdirectory'

        for db_file in res[1]:

            #todo manage result!!!
            res = self.__manageDBFile(db_file)



        return 0, None



    def __manageDBFile(self,db_file):
        db_manager = DatabaseManager(db_file)

        userList = db_manager.getUsersList()



        return 0,None