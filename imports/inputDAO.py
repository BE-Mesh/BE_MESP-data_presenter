from .utilities.singleton import Singleton
from pathlib import Path
import sys
import re
import os



class InputDAO(metaclass=Singleton):
    def __init__(self):

        self.__input_dir_path = self.__input_dir_path_validator()[1]
        self.__input_subdirectories_list = self.__retrieve_subdirectories_list()[1]



    def __input_dir_path_validator(self):


        if len(sys.argv) < 2:
            err_code = '1ID'  # ID stands for InputDao
            err_mess = 'MISSING INPUT DIRECTORY NAME'
            err_details = 'please pass the name of the directory containing the input files'
            raise ValueError(err_code, err_mess, err_details)

        input_dir_name_check = bool(re.match('^[a-zA-Z0-9\-_]+$', str(sys.argv[1])))

        if not input_dir_name_check:
            err_code = '2ID'  # ID stands for InputDao
            err_mess = 'INVALID NAME FOR AN INPUT DIR'
            err_details = 'please pass a name containing only letters/numbers/-/_  and no whitespace '
            raise ValueError(err_code, err_mess, err_details)



        script_root_path_str = str(Path(str(sys.argv[0])).absolute().parent.parent)
        input_dir_path = Path(script_root_path_str + "/results/2-ds-results/" + str(sys.argv[1])).absolute()

        if not input_dir_path.is_dir():
            err_code = '3ID'  # ID stands for InputDao
            err_mess = 'NO DIRECTORY FOUND '
            err_details = 'no directory found at ' + str(input_dir_path)
            raise ValueError(err_code, err_mess, err_details)

        return 0, str(input_dir_path)

    def __retrieve_subdirectories_list(self):

        subdirectories = [x[0] for x in os.walk(self.__input_dir_path)]
        subdirectories.pop(0) #removes __input_dir_path

        if len(subdirectories) < 1:
            err_code = '4ID'  # ID stands for InputDao
            err_mess = 'NO SUBDIRECTORIES FOUND '
            err_details = 'no subdirectories found at ' + str(self.__input_dir_path)
            raise ValueError(err_code, err_mess, err_details)

        return 0,subdirectories


    def getFilesInDirectory(self,dir):

        if dir not in self.__input_subdirectories_list:
            return 1,'InputDAO: directory must be one of the subdirectories of input folder'

        files_list= []

        for (dirpath, dirnames, filenames) in os.walk(dir):
            files_list.extend(filenames)


            files_list_filtered = []

        for file_entry in files_list:
            name_check = bool(re.match('^(?!\.).*(\.db)$', file_entry))
            if name_check:
                files_list_filtered.append(dir + '/' + file_entry)


        return 0, files_list_filtered








    def getInputDirPath(self):
        return self.__input_dir_path


    def getSubdirectoriesList(self):
        return self.__input_subdirectories_list