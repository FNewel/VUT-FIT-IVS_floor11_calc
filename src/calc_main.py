## @file calc_main.py
# @author Martin Talajka
# @date 21.4.2021
# @brief The main logic of the calculator

import sys
import qtmodern.styles  # from https://github.com/gmarull/qtmodern

from PyQt5 import QtWidgets
from calc_gui import Ui_MainWindow




if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    qtmodern.styles.dark(app)

    MainWindow.show()
    sys.exit(app.exec_())

# End of file calc_main.py