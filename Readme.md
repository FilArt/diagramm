testtest

        def plot(self):
            plot = self.graphicsView
            plot.setAspectLocked()

            # diagramm
            import numpy as np
            import scipy.special as sp

            a = int(self.lineEdit.text())
            k = int(self.lineEdit_2.text())

            # make polar data
            theta = np.linspace(0.000001, 2 * np.pi, 10000)
            arg = k * a * np.sin(theta)
            radius = 2 * sp.jvp(0, arg) / arg

            # TransMainWindow to cartesian and plot
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)

            # Add polar grid lines and clear previous
            plot.clear()
            plot.addLine(x=0, pen=0.2)
            plot.addLine(y=0, pen=0.2)
            for r in [0.25, 0.5, 1]:
                circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
                circle.setPen(pg.mkPen(0.15))
                plot.addItem(circle)

            plot.plot(y, abs(x))