## @file calc_main.py
# @author Martin Talajka
# @date 21.4.2021
# @brief The main logic of the calculator

import os
from os import MFD_ALLOW_SEALING
import sys
import platform
import mathlib
import qtmodern.styles  # from https://github.com/gmarull/qtmodern

from PyQt5 import QtWidgets
from calc_gui import Ui_MainWindow

class calcLogic(QtWidgets.QMainWindow, Ui_MainWindow):
    print("-- Main --") #! Debug printout

    # Variable holds text displayed on main display
    md_text = ""

    #Symbols
    bin_ops = {'+', '-', '/', '*', '^'}
    un_ops = {'√', '!'}
    parentheses = {'(',')'}
    open_par = 0

    #Is decimal point set in this number
    dec_p = False

    def sText(self, text):
        self.main_display.setText(text)

    # Append a number
    def aNum(self, n):
        self.md_text += n
        self.main_display.setText(self.md_text)

    # Append binary operator
    def aBinOp(self, op):
        if self.md_text != "":
            if self.md_text[-1].isdigit() or self.md_text[-1] == ")":
                self.md_text += op
                self.main_display.setText(self.md_text)
                self.dec_p = False
            elif self.md_text[-1] in self.bin_ops:
                self.md_text = self.md_text[:-1]
                self.md_text += op
                self.main_display.setText(self.md_text)
                self.dec_p = False

    # Append unary operator 
    def aUnOp(self, op):
        if self.md_text == "" or self.md_text[-1] in self.bin_ops:
            self.md_text += op
            self.main_display.setText(self.md_text)
            self.open_par +=1

    #Append decimal point
    def aDecPoint(self):
        if self.dec_p == False:
            if self.md_text != "" and self.md_text[-1].isdigit():
                self.md_text += "."
                self.main_display.setText(self.md_text)
                self.dec_p = True
            else:
                self.md_text += "0."
                self.main_display.setText(self.md_text)
                self.dec_p = True

    #Delete last character (2 if last is factorial or root)
    def BackSpace(self):
        if self.md_text != "":
            if len(self.md_text) > 1 and self.md_text[-2] in self.un_ops:
                self.md_text = self.md_text[:-2]
            else:
                if self.md_text[-1] == ".":
                    self.dec_p = False
                self.md_text = self.md_text[:-1]
            self.main_display.setText(self.md_text)

    #Append parenthesis
    def aParenthesis(self, text):
        if text == "(":
            self.md_text += text
            self.main_display.setText(self.md_text)
            self.open_par += 1
        if text == ")" and self.open_par > 0:
            self.md_text += ")"
            self.main_display.setText(self.md_text)
            self.open_par -= 1

    #Clear both main and secondary displays
    def ClearEverything(self):
        self.md_text = ""
        self.dec_p = False
        self.open_par = 0
        self.main_display.setText(self.md_text)


    # Opens Guide PDF on a specific system (Windows/Linux)
    def oPDF_g(self):
        srcDir = os.path.dirname(os.path.realpath(__file__))
        pdf_path = srcDir + os.path.sep + 'CalcGuide.pdf'
        if platform.system() == "Windows":
            os.startfile(pdf_path)
        elif platform.system() == "Linux":
            os.system('xdg-open \"{}\"'.format(pdf_path))

    #Change sign of number
    def ChangeSign(self):
        if self.md_text.isnumeric() or self.md_text == "":
            self.md_text = "-" + self.md_text
            self.main_display.setText(self.md_text)
        elif self.md_text[0] == "-" and self.md_text[1:].isnumeric():
            self.md_text = self.md_text[1:]
            self.main_display.setText(self.md_text)

    # Opens Guide PDF on a specific system (Windows/Linux)
    def oPDF_g(self):
        srcDir = os.path.dirname(os.path.realpath(__file__))
        pdf_path = srcDir + os.path.sep + 'CalcGuide.pdf'
        if platform.system() == "Windows":
            os.startfile(pdf_path)
        elif platform.system() == "Linux":
            os.system('xdg-open \"{}\"'.format(pdf_path))

    # Function for UI color change (dark/white)
    def sColor(self, dark):
        if dark:
            # Dark Style Sheet
            qtmodern.styles.dark(app)
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
            # White Style Sheet
            qtmodern.styles.light(app)
            self.frame.setStyleSheet("QFrame { background-color: rgb(243, 243, 243) }"
                                     "QLineEdit { background-color: rgb(220, 220, 220); border-style: outset; border-width: 0px; color: rgb(0, 0, 0)}"
                                     "QPushButton { border-style: outset;border-color: rgb(0, 0, 0); border-width: 1px; border-radius: 10px; color: black }"
                                     "QPushButton[objectName^=\"n\"] { background-color: rgb(252, 252, 252) }"
                                     "QPushButton[objectName^=\"e\"] { background-color: rgb(200, 200, 200); font: 30pt \"Noto Mono\" }"
                                     "QPushButton[objectName^=\"b\"] { background-color: rgb(220, 220, 220) }"
                                     "QPushButton#button_delete{ font: 30pt \"Noto Mono\" }"
                                     "QPushButton:hover { background-color: rgb(235, 235, 235) }"
                                     "QPushButton:pressed { background-color: rgb(255, 255, 255) }"
                                    )

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = calcLogic()
    ui.setupUi(MainWindow)

    # Default set dark theme
    qtmodern.styles.dark(app)

    MainWindow.show()
    sys.exit(app.exec_())

# End of file calc_main.py