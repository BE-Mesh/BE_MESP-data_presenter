

class Subcase():
    name = None
    __average_convergence_time = None

    def __init__(self,name, average_convergence_time):
        self.name = name
        self.__average_convergence_time = average_convergence_time


    def getAverageConvergenceTime(self):
        return 0,self.__average_convergence_time

