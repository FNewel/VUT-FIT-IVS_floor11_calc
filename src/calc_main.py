## @file calc_main.py
# @author Martin Talajka
# @date 21.4.2021
# @brief The main logic of the calculator

import os
import re
import sys
import platform

from PyQt5.QtCore import dec, left, right
import mathlib
import qtmodern.styles  # from https://github.com/gmarull/qtmodern

from PyQt5 import QtWidgets
from calc_gui import Ui_MainWindow
from collections import OrderedDict

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
        # Error flag
        self.error = False
        # Displaying result from previous equation
        self.result = False


    def sText(self, text):
        self.main_display.setText(text)

    # Append a number
    def aNum(self, n):
        if self.result:
            self.result = False
            self.dec_p = False
            self.md_text = ""
        self.md_text += n 
        self.main_display.setText(self.md_text)

    # Append binary operator
    def aBinOp(self, op):
        self.result = False
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
        if self.result:
            self.result = False
            self.dec_p = False
            self.md_text = ""
        self.md_text += op
        self.main_display.setText(self.md_text)
        self.open_par +=1

    # Append decimal point
    def aDecPoint(self):
        if self.result:
            self.result = False
            self.dec_p = False
            self.md_text = ""
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
        self.result = False
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
        if self.result:
            self.result = False
            self.dec_p = False
            self.md_text = ""
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
        self.sd_text = ""
        self.dec_p = False
        self.open_par = 0
        self.result = False
        self.main_display.setText(self.md_text)
        self.h_display.setText(self.sd_text)

    # Change sign of number
    def changeSign(self):
        self.result = False
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

        #1. Solve parentheses
        while "(" in self.md_text:
            par_pairs = self.findParPairs(self.md_text)
            par_strings = {}
            for k ,v in par_pairs.items():
                par_strings[k] = self.md_text[k+1:v]

            par_strings = OrderedDict(reversed(list(par_strings.items())))
            for k, v in par_strings.items():
                if not "(" in v:
                    result = self.calculateString(v)
                    if self.error:
                        self.error = False
                        self.md_text = ""
                        return
                    tmp = self.md_text[k+len(v)+2:]
                    self.md_text = self.md_text[:k] + str(result) + tmp

        self.md_text = self.calculateString(self.md_text)
        if self.error:
            self.md_text = ""
            self.error = False
            return
        self.repairOutput()
        if self.error:
            self.md_text = ""
            self.error = False
            return
        self.main_display.setText(self.md_text)
        self.result = True
        self.open_par = 0
        if not "." in self.md_text:
            self.dec_p = False
        else:
            self.dec_p = True
        return
        
            


    # Repairs any syntax errors still present in the input string
    def repairInput(self):
        
        # Closes open parentheses
        if self.open_par != 0: 
            for i in range(0, self.open_par):
                self.md_text += ")"

        # Removes leading and trailing zeroes
        positions = self.findAllPositions("\d+", self.md_text)
        numbers = re.findall("\d+", self.md_text)
        pos_num = {}
        for i in range(0, len(positions)):
            pos_num[positions[i]] = numbers[i]
        pos_num = dict(reversed(list(pos_num.items())))
        if pos_num: 
            for pos, string in pos_num.items():
                if pos - 1 >= 0 and self.md_text[pos-1] == ".":
                    new_string = string.rstrip("0")
                    if new_string == "":
                        self.md_text = self.md_text[:pos-1] + self.md_text[pos+len(string):]
                    else:
                        self.md_text = self.md_text[:pos] + new_string + self.md_text[pos+len(string):]
                else:
                    new_string = int(string)
                    new_string = str(new_string)
                    self.md_text = self.md_text[:pos] + new_string + self.md_text[pos+len(string):]

        # Turns N.NaN into N
        positions = self.findAllPositions("\.", self.md_text)
        positions.reverse()
        for pos in positions:
            if (pos + 1 >= len(self.md_text)) or (not self.md_text[pos + 1].isdigit()):
                self.md_text = self.md_text[:pos] + self.md_text[pos+1:]

        # Fixes "N(" and ")N" input to "N*(" and ")*N"
        i = 0
        positions = self.findAllPositions("\d\(|\)\d|\d!|\dr|\)\(", self.md_text)
        if positions:
            for pos in positions:
                tmp = "*" + self.md_text[(pos+i+1):]
                self.md_text = self.md_text[:-(len(self.md_text)-(pos+i+1))]
                self.md_text += tmp
                i += 1
        
        # Fixes "(op" and "op)" input to "(" and ")"
        i=0
        positions = self.findAllPositions("\(\*|\*\)|\(/|/\)|\(\+|\+\)|\(^|^\)", self.md_text)
        if positions:                                                
            for pos in positions:
                if self.md_text[pos+i] == "(":
                    self.md_text = self.md_text[:pos+i+1] + self.md_text[pos+i+2:]
                else:
                    self.md_text = self.md_text[:pos+i] + self.md_text[pos+i+1:]
                i-= 1
        
        


        
    
    # Finds all positions of found patterns in string and returns them in a list
    def findAllPositions(self, pattern, str):
        found = re.findall(pattern, str)
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

    # Returns parenthesis pairs from text
    def findParPairs(self, text):
        open_pars = [] 
        pairs = {}
        for i, c in enumerate(text):
            if c == '(':
                open_pars.append(i)
            if c == ')':
                pairs[open_pars.pop()] = i
        return pairs

    # Function caculates a string
    def calculateString(self, text):
        
        text = self.calcRnd(text)
        if self.error:
            return

        text = self.calcFact(text)
        if self.error:
            return

        text = self.calcRoot(text)
        if self.error:
            return

        text = self.calcExp(text)
        if self.error:
            return

        text = self.calcMulDiv(text)
        if self.error:
            return

        text = self.calcPlusMin(text)
        if self.error:
            return

        return str(text)

    # Function calculates rnd() (if there is one)
    def calcRnd(self, text):
        while(text.find("r") >= 0):
            rnd_num = ""

            pos = text.find("r")

            rnd_num = self.getRightOperand(text, pos + 2)     
            
            if rnd_num == "":
                tmp = mathlib.rng(100)
            else:
                try:
                    tmp = mathlib.rng(int(rnd_num))
                except ValueError:
                    self.errorHandler("ERR_rnd_zero")
                    return
                except TypeError:
                    self.errorHandler("ERR_rnd_flt")
                    return
                
            text = text[:pos] + str(tmp) + text[pos + 3 + len(str(rnd_num)):]
        return text

    # Function calculates factorial (if there is one)
    def calcFact(self, text):
        while(text.find("!") >= 0):
            fact_num = ""

            pos = text.find("!")

            fact_num = self.getRightOperand(text, pos)

            try:
                tmp = mathlib.fact(fact_num)
            except ValueError:
                self.errorHandler("ERR_fact_neg")
                return
            except TypeError:
                self.errorHandler("ERR_fact_flt")
                return

            text = text[:pos] + str(tmp) + text[pos + 1 + len(str(fact_num)):]
        return text

    # Function calculates root (if there is one)
    def calcRoot(self, text):
        while(text.find("√") >= 0):
            root_num = ""
            root_lvl = ""
            implicit_root = False
            
            pos = text.find("√")

            root_num = self.getRightOperand(text,pos)

            root_lvl = self.getLeftOperand(text,pos)

            if root_lvl == "":
                implicit_root = True
                root_lvl = 2
                
            try:
                tmp = mathlib.root(root_lvl, root_num)
            except ValueError:
                self.errorHandler("ERR_root_badVal_n")
                return
            except TypeError:
                self.errorHandler("ERR_root_n_flt")
                return
            except ZeroDivisionError:
                self.errorHandler("ERR_root_n_zero")
                return
            
            if implicit_root == True:
                root_lvl = ""

            text = text[:pos-len(str(root_lvl))] + str(tmp) + text[pos + 1 + len(str(root_num)):]
        return text

    # Function calculates exponent in expression (if there is one) #TODO: Loop it 
    def calcExp(self, text):
        while(text.find("^") >= 0):
            exp_n = ""
            exp_x = ""
            
            pos = text.find("^")
            
            exp_n = self.getRightOperand(text, pos)

            exp_x = self.getLeftOperand(text, pos)

            if exp_x == "" or exp_n == "":
                self.errorHandler("ERR_exp_no_op")
                return

            try:
                tmp = mathlib.exp(exp_x, exp_n)
            except ValueError:
                self.errorHandler("ERR_exp_n_neg")
                return
            except TypeError:
                self.errorHandler("ERR_n_flt")
                return

            text = text[:pos-len(str(exp_x))] + str(tmp) + text[pos + 1 + len(str(exp_n)):]
        return text

    # Function calculates multiplications and divisions in expression (if there are any)
    def calcMulDiv(self, text):
        while(text.find("*") >= 0 or text.find("/") >= 0):
            left_num = ""
            right_num = ""
            
            for char in text:
                if char == "*" or char == "/":
                    pos = text.find(char)
                    break

            right_num = self.getRightOperand(text, pos)
            
            left_num = self.getLeftOperand(text, pos)

            if left_num == "" or right_num == "":
                self.errorHandler("ERR_mul_div_no_op")
                return

            if text[pos] == "/":
                try:
                    tmp = mathlib.div(left_num, right_num)
                except ZeroDivisionError:
                    self.errorHandler("ERR_div_zero")
                    return
            if text[pos] == "*":
                tmp = mathlib.mul(left_num, right_num)

            text = text[:pos-len(str(left_num))] + str(tmp) + text[pos + 1 + len(str(right_num)):]
            
        return text

    # Function calculates additions and subtractions (if there are any)
    def calcPlusMin(self, text):
        while(text.find("+") >= 0 or text[1:].find("-") >= 0):
            left_num = ""
            right_num = ""
            pos = 0
            for char in text[1:]:
                if char == "+" or char == "-":
                    pos = text[1:].find(char)
                    pos += 1
                    break
            if pos == 0:
                break
            
            right_num = self.getRightOperand(text, pos)
            
            left_num = self.getLeftOperand(text, pos)

            if left_num == "" or right_num == "":
                self.errorHandler("ERR_plus_min_no_op")
                return

            if text[pos] == "+":
                tmp = mathlib.add(left_num, right_num)
            if text[pos] == "-":
                tmp = mathlib.sub(left_num, right_num)

            text = text[:pos-len(str(left_num))] + str(tmp) + text[pos + 1 + len(str(right_num)):]
            
        return text

    
    #Return the left operand of a binary function on position pos from text
    def getLeftOperand(self, text, pos):
        left_op = ""
        i = -1
        if pos + i < 0:
            return left_op
        while (text[pos+i].isdigit() or text[pos+i] == "." or text[pos+i] == "-"):
            if text[pos+i] == "-":
                if(pos+i == 0) or (not text[pos+i-1].isdigit()):
                    left_op += text[pos+i]
                else:
                    break
            else:
                left_op += text[pos+i]
            i -= 1
            if (pos + i) < 0:
                break
        left_op = left_op[::-1]


        try:
            left_op = int(left_op)
        except:
            try:
                left_op = float(left_op)
            except:
                left_op = ""

        return left_op

    # Return the right operand of a binary function on position pos from text
    def getRightOperand(self,text,pos):
        right_op = ""
        i = 1
        if pos + i >= len(text):
            return right_op
        while (text[pos+i].isdigit() or text[pos+i] == "." or ((i == 1) and text[pos+i] == "-")):
            right_op += text[pos+i]
            i += 1
            if (pos + i) >= len(text):
                break

        try:
            right_op = int(right_op)
        except:
            try:
                right_op = float(right_op)
            except:
                right_op = ""
        
        return right_op


    # Handles error printing onto the main display
    def errorHandler(self, err_msg):
        self.md_text = err_msg
        self.sd_text = ""
        self.main_display.setText(self.md_text)
        self.h_display.setText(self.sd_text)
        self.open_par = 0
        self.dec_p = False
        self.error = True
        return

    def repairOutput(self):
        result = 0
        try:
            result = float(self.md_text)
        except ValueError:
            self.errorHandler("ERR_out_NaN")
        result = round(result, 6)
        if result % 1 == 0:
            result = int(result)
        self.md_text = str(result)

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
                                     "QPushButton[objectName^=\"e\"] { background-color: rgb(165, 165, 165); font: 30pt \"Noto Mono\" }"
                                     "QPushButton[objectName^=\"b\"] { background-color: rgb(200, 200, 200) }"
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