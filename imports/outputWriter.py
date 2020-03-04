from .utilities.singleton import Singleton
from .utilities.outputDirectoryManager import OutputDirectoryManager
import plotly
import plotly.graph_objs as go

class OutputWriter(metaclass=Singleton):
    def __init__(self):

        self.__output_dir_path = OutputDirectoryManager().getOutputDir()
        self.__timestamp_plot_path = self.__output_dir_path + '/' + 'SubcaseXtimestamp'
        self.__num_update_msg_plot_path = self.__output_dir_path + '/' + 'SubcaseXnumUpdatePackets'

    def createSubcaseXtimestampPlot(self,subcases_list):
        print('generating SubcaseXtimestamp Plot... ')
        #todo: check if subcases_list is a list of Subcase objects

        trace = go.Scatter(x=[sc.getName() for sc in subcases_list],  # ['zero meters','one meter','three meters','five meters'],
                           y=[sc.getAverageConvergenceTime() for sc in subcases_list],
                           error_y=dict(
                               type='data',
                               array=[2*sc.getStdevConvergenceTime() for sc in subcases_list],
                               visible=True
                           )
                           )
        layout = go.Layout(

            xaxis=dict(
                title='#Nodes'

            ),

            yaxis=dict(
                title='Convergence Time [ms]',
                # range=[0, 9000]
            )
        )

        data = [trace]

        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename=self.__timestamp_plot_path)

        return 0,None

    def createSubcaseXnumUpdatePackets(self,subcases_list):
        print('generating SubcaseXnumUpdatePackets Plot... ')
        #todo: check if subcases_list is a list of Subcase objects

        trace = go.Scatter(x=[sc.getName() for sc in subcases_list],
                           # ['zero meters','one meter','three meters','five meters'],
                           y=[sc.getAverageSentUpdatePackets() for sc in subcases_list],
                           error_y=dict(
                               type='data',
                               array=[2 * sc.getStdevSentUpdatePackets() for sc in subcases_list],
                               visible=True
                           )
                           )
        layout = go.Layout(

            xaxis=dict(
                title='#Nodes'

            ),

            yaxis=dict(
                title='# routing table updates',
                # range=[0, 9000]
            )
        )

        data = [trace]

        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename=self.__num_update_msg_plot_path)

        return 0,None


