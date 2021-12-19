from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use("Qt5Agg")


class DataFigure(FigureCanvas):
    def __init__(self):
        fig = Figure(figsize=(3.2, 2.3), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)

    def display(self, y):
        self.axes.plot(y)

    def test(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        self.axes.plot(x, y)
