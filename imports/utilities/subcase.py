

class Subcase():
    name = None
    __average_convergence_time = None

    def __init__(self,name, average_convergence_time,stdev_convergence_time,
                 average_sent_update_packets,stdev_sent_update_packets):
        self.name = name
        self.__average_convergence_time = average_convergence_time
        self.__stdev_convergence_time = stdev_convergence_time
        self.__average_sent_update_packets = average_sent_update_packets
        self.__stdev_sent_update_packets = stdev_sent_update_packets

    def getAverageConvergenceTime(self):
        return 0,self.__average_convergence_time

    def getStdevConvergenceTime(self):
        return 0,self.__stdev_convergence_time

    def getAverageSentUpdatePackets(self):
        return 0,self.__average_sent_update_packets

    def getStdevSentUpdatePackets(self):
        return 0,self.__stdev_sent_update_packets