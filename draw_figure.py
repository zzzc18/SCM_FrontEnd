from matplotlib.figure import Figure
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use("Qt5Agg")


class SpeedFigure(FigureCanvas):
    def __init__(self):
        fig = Figure(figsize=(3.2, 2.3), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)

    def display(self, y):
        x = [i for i in range(len(y))]
        self.axes.plot(y, color='blue')
        self.axes.fill_between(x, 0, y, facecolor='blue', alpha=0.3)


class TemperatureFigure(FigureCanvas):
    def __init__(self):
        fig = Figure(figsize=(3.2, 2.3), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)

    def display(self, y):
        x = [i for i in range(len(y))]
        self.axes.plot(y, color='coral')
        self.axes.fill_between(x, 0, y, facecolor='coral', alpha=0.3)
