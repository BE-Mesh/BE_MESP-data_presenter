from .utilities.singleton import Singleton
from .utilities.outputDirectoryManager import OutputDirectoryManager
import plotly
import plotly.graph_objs as go

class OutputWriter(metaclass=Singleton):
    def __init__(self):

        self.__output_dir_path = OutputDirectoryManager().getOutputDir()


    def createSubcaseXtimestampPlot(self,subcases_list):
        print('generating SubcaseXtimestamp Plot... ')
        return 0,None

    def createSubcaseXnumUpdatePackets(self,subcases_list):
        print('generating SubcaseXnumUpdatePackets Plot... ')
        return 0,None


