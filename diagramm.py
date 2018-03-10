# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagramm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(225, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "k"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "a"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "Построить диаграмму"))

        self.pushButton.clicked.connect(self.plot)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

