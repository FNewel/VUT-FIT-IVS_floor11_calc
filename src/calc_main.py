## @file calc_main.py
# @author Martin Talajka
# @date 21.4.2021
# @brief The main logic of the calculator

import os
import re
import sys
import platform
import mathlib
import qtmodern.styles  # from https://github.com/gmarull/qtmodern

from PyQt5 import QtWidgets
from calc_gui import Ui_MainWindow

class calcLogic(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # Displayed text
        self.md_text = "" # Main display
        self.sd_text = "" # Secondary display
        # Symbols
        self.bin_ops = {'+', '-', '/', '*', '^'}
        self.un_ops = {'√', '!'}    # rnd( excluded
        self.parentheses = {'(',')'}
        self.open_par = 0
        # Is decimal point set in this number
        self.dec_p = False
        # Memory
        self.memory = "" 


    def sText(self, text):
        self.main_display.setText(text)

    # Append a number
    def aNum(self, n):
        self.md_text += n
        self.main_display.setText(self.md_text)

    # Append binary operator
    def aBinOp(self, op):
        if self.md_text != "":
            if self.md_text[-1] not in self.bin_ops:
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
        self.md_text += op
        self.main_display.setText(self.md_text)
        self.open_par +=1

    # Append decimal point
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

    # Delete last character (2 if last is factorial or root)
    def backSpace(self):
        if self.md_text != "":
            if len(self.md_text) > 3 and self.md_text[-4: -1:] == "rnd":
                self.md_text = self.md_text[:-4]
                self.open_par -= 1
            elif len(self.md_text) > 1 and self.md_text[-2] in self.un_ops:
                self.md_text = self.md_text[:-2]
                self.open_par -= 1
            else:
                if self.md_text[-1] == ".":
                    self.dec_p = False
                if self.md_text[-1] == "(":
                    self.open_par -= 1
                if self.md_text[-1] == ")":
                    self.open_par += 1
                self.md_text = self.md_text[:-1]
            self.main_display.setText(self.md_text)

    # Append parenthesis
    def aParenthesis(self, text):
        if text == "(":
            self.md_text += text
            self.main_display.setText(self.md_text)
            self.open_par += 1
        if text == ")" and self.open_par > 0:
            self.md_text += ")"
            self.main_display.setText(self.md_text)
            self.open_par -= 1

    # Clear both main and secondary displays
    def clearEverything(self):
        self.md_text = ""
        self.dec_p = False
        self.open_par = 0
        self.main_display.setText(self.md_text)

    # Change sign of number
    def changeSign(self):
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

    # Stores text on main display to memory
    def memSet(self):
        self.memory = self.md_text

    # Loads text from memory to main display (if not empty)
    def memLoad(self):
        if self.memory != "":
            self.md_text = self.memory
            self.main_display.setText(self.md_text)
    
    # Clears the memory
    def memClear(self):
        self.memory = ""

    # Calculates the result
    def calculate(self):
        self.repairInput()
        self.sd_text = self.md_text
        self.h_display.setText(self.sd_text)
        self.open_par = 0

    def repairInput(self):
        if self.open_par != 0: # Closes open parentheses
            for i in range(0, self.open_par):
                self.md_text += ")"

        i = 0
        positions = self.findAllPositions("\d\(|\)\d", self.md_text) # Fixes "N(" and ")N" input to "N*(" and ")*N"
        if positions:
            for pos in positions:
                tmp = "*" + self.md_text[(pos+i+1):]
                self.md_text = self.md_text[:-(len(self.md_text)-(pos+i+1))]
                self.md_text += tmp
                i += 1
        
        i=0
        positions = self.findAllPositions("\(\*|\*\)", self.md_text) # Fixes "(*" and "*)" input to "(" and ")"
        if positions:
            for pos in positions:
                if self.md_text[pos+i] == "(":
                    self.md_text = self.md_text[:pos+i+1] + self.md_text[pos+i+2:]
                else:
                    self.md_text = self.md_text[:pos+i] + self.md_text[pos+i+1:]
                i-= 1
    
    def findAllPositions(self, pattern, str):
        found = re.findall(pattern, self.md_text)
        positions = []
        if found:
            pos = 0
            for c in found:
                pos = str.find(c, pos)
                if pos == -1:
                    break
                positions.append(pos)
                pos += len(c)
        return positions



        


        

    # Function for UI color change (dark/white)
    def sColor(self, dark):
        if dark:
            # Dark Style Sheet
            qtmodern.styles.dark(app)
            self.frame.setStyleSheet("QFrame { background-color: rgb(49, 54, 59) }"
                                     "QLineEdit { background-color: rgb(68, 68, 68); border-style: outset; border-width: 0px; color: rgb(255, 255, 255) }"
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
                                     "QLineEdit { background-color: rgb(220, 220, 220); border-style: outset; border-width: 0px; color: rgb(0, 0, 0) }"
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