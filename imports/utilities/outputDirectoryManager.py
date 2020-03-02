from .singleton import Singleton
import sys
import os
import re
from pathlib import Path




#todo
class OutputDirectoryManager(metaclass=Singleton):
    def __init__(self):
        self.__output_dir = self.__output_dir_path_validator()[1]


    def __output_dir_path_validator(self):


        if len(sys.argv) < 3:
            err_code = '1OW'  # OW stands for OutputWriter
            err_mess = 'MISSING OUTPUT DIRECTORY NAME'
            err_details = 'please pass the name of the output subdirectory'
            raise ValueError(err_code, err_mess, err_details)

        input_dir_name_check = bool(re.match('^[a-zA-Z0-9\-_]+$', str(sys.argv[2])))

        if not input_dir_name_check:
            err_code = '2OW'   # OW stands for OutputWriter
            err_mess = 'INVALID NAME FOR AN OUTPUT DIR'
            err_details = 'please pass a name containing only letters/numbers/-/_  and no whitespace '
            raise ValueError(err_code, err_mess, err_details)


        script_root_path_str = str(Path(str(sys.argv[0])).absolute().parent.parent)
        output_dir_path = Path(script_root_path_str + "/results/3-dp-results/" + str(sys.argv[2])).absolute()
        print("Checking if ./results/3-dp-results/" + str(sys.argv[2]) + " exists...")
        try:
            os.makedirs(output_dir_path)
        except OSError as e:
            print("/results/3-dp-results/" + str(sys.argv[2]) + " already exists, continuing... ")

        print("Output directory initialized")
        return 0, str(output_dir_path)

    def getOutputDir(self):
        return self.__output_dir