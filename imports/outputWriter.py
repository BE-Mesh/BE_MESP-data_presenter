from .utilities.singleton import Singleton
from .utilities.outputDirectoryManager import OutputDirectoryManager
from pathlib import Path
import sys
import re
import os

class OutputWriter(metaclass=Singleton):
    def __init__(self):

        self.__output_dir_path = OutputDirectoryManager().getOutputDir()




