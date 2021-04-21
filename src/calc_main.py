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