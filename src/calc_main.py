## @file calc_main.py
# @author Martin Talajka
# @date 21.4.2021
# @brief The main logic of the calculator

import sys
import mathlib
import qtmodern.styles  # from https://github.com/gmarull/qtmodern

from PyQt5 import QtWidgets
from calc_gui import Ui_MainWindow

class calcLogic(QtWidgets.QMainWindow, Ui_MainWindow):
    print("-- Main --") #! Debug printout
    
    # Function for UI color change (dark/white)
    def sColor(self, dark):
        if dark:
            # Dark Style Sheet
            self.frame.setStyleSheet("QFrame { background-color: rgb(49, 54, 59) }"
                                    "QLineEdit { background-color: rgb(68, 68, 68); border-style: outset; border-width: 0px; color: rgb(255, 255, 255)}"
                                    "QPushButton { border-style: outset;border-color: rgb(0, 0, 0); border-width: 1px; border-radius: 10px; color: white }"
                                    "QPushButton[objectName^=\"n\"] { background-color: rgb(35, 35, 35) }"
                                    "QPushButton[objectName^=\"e\"] { background-color: rgb(96, 96, 96); font: 30pt \"Noto Mono\" }"
                                    "QPushButton[objectName^=\"b\"] { background-color: rgb(68, 68, 68) }"
                                    "QPushButton#button_delete{ font: 30pt \"Noto Mono\" }"
                                    "QPushButton:hover { background-color: rgb(122, 122, 122) }"
                                    "QPushButton:pressed { background-color: rgb(135, 135, 135) }"
                                    )
        else:
            # White Style Sheet     # TODO - farby treba spraviť !
            self.frame.setStyleSheet("QFrame { background-color: rgb(255,0,0) }"
                                    "QLineEdit { background-color: rgb(68, 68, 68); border-style: outset; border-width: 0px; color: rgb(0, 0, 0)}"
                                    "QPushButton { border-style: outset;border-color: rgb(0, 0, 0); border-width: 1px; border-radius: 10px; color: white }"
                                    "QPushButton[objectName^=\"n\"] { background-color: rgb(255,0,0) }"
                                    "QPushButton[objectName^=\"e\"] { background-color: rgb(255,0,0); font: 30pt \"Noto Mono\" }"
                                    "QPushButton[objectName^=\"b\"] { background-color: rgb(255,0,0) }"
                                    "QPushButton#button_delete{ font: 30pt \"Noto Mono\" }"
                                    "QPushButton:hover { background-color: rgb(255,0,0) }"
                                    "QPushButton:pressed { background-color: rgb(255,0,0) }"
                                    )

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = calcLogic()
    ui.setupUi(MainWindow)

    # TODO - toto upraviť aby to fungovalo s dark/white módom
    qtmodern.styles.dark(app)

    MainWindow.show()
    sys.exit(app.exec_())

# End of file calc_main.py