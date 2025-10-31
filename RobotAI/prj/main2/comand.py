'''
QCheckbox       A checkbox
QComboBox	    A dropdown list box
QDateEdit	    For editing dates and datetimes
QDateTimeEdit	For editing dates and datetimes
QDial	        Rotateable dial
QDoubleSpinBox	A number spinner for floats
QFontComboBox	A list of fonts
QLCDNumber	    A quite ugly LCD display
QLabel	        Just a label, not interactive
QLineEdit	    Enter a line of text
QProgressBar	A progress bar
QPushButton	    A button
QRadioButton	A toggle set, with only one active item
QSlider	        A slider
QSpinBox	    An integer spinner
QTimeEdit	    For editing times
'''
import const as c
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QFontComboBox,
    QLineEdit,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import (
    QSize,
    Qt
)

# needed for accessing command line arguements
import sys 

SETCMD = {
    0: 'move',
    1: 'start auto-exploration',
    2: 'move to ({x}, {y}) position'
}

# APP CLASS
class CommandApp():
    def __init__(self, width=640, height=480):

        self.w = width
        self.h = height

        self.x = None
        self.y = None

        # App instance
        self.app = QApplication(sys.argv)

        # main wndow
        self.window = QWidget()

        # window settings
        self.window.setWindowTitle(c.APP_NAME)

        # window size
        self.window.setFixedSize(QSize(self.w, self.h))
    #
    def mainloop(self):
        
        # setup UI
        self.setupUI()

        # show the window
        self.window.show()

        # start the app loop
        self.app.exec()
    # 
    def setupUI(self):
        layout = QVBoxLayout()

        # move CMD: move robot auto-exploration
        moveLabel = QLabel("move Command")
        moveBtn = QPushButton("move")
        moveBtn.clicked.connect()

        # Start CMD: start robot auto-exploration
        AutoExpLabel = QLabel("Start Auto-Exploration")
        AutoExpBtn = QPushButton("Start")
        AutoExpBtn.clicked.connect()

        # Move CMD: move to (x,y) chosen position
        Xlabel = QLabel("Insert X coordinate")
        self.Xinput = QLineEdit()

        Ylabel = QLabel("Insert Y coordinate")
        self.Yinput = QLineEdit()

        MoveLabel = QLabel("Move to (X,Y) Position")
        MoveBtn = QPushButton("Move")

        MoveBtn.clicked.connect()

        # layout per coordinate
        coord_layout = QHBoxLayout()
        coord_layout.addWidget(QLabel("X:"))
        coord_layout.addWidget(self.Xinput)
        coord_layout.addWidget(QLabel("Y:"))
        coord_layout.addWidget(self.Yinput)

        # aggiungi tutto al layout principale
        layout.addWidget(moveLabel)
        layout.addWidget(moveBtn)
        layout.addSpacing(10)
        layout.addWidget(AutoExpLabel)
        layout.addWidget(AutoExpBtn)
        layout.addSpacing(10)
        layout.addWidget(Xlabel)
        layout.addWidget(Ylabel)
        layout.addLayout(coord_layout)
        layout.addWidget(MoveBtn)

        self.window.setLayout(layout)
    #        
#
'''
def main():
    app = CommandApp()
    app.mainloop() 
#
if __name__ == "__main__":
    main()
'''
'''
def move_cmd(self):
        try:
            # .text() retrives text from QLineEdit
            if self.Xinput.text().isnumeric() and self.Yinput.text().isnumeric():
                msg = f"Sent Command: {SETCMD[2].format(x=self.Yinput, y=self.Yinput)}"
                return True, msg
            else:
                msg = "Invalid cooridnates."
                return False, msg
        except Exception as e:
            print(f"Error in Move Command: {e}")
    #
    def print_status(self, cmd_id):
        print(f"Sent command: {SETCMD[cmd_id]}")
    #
    def send_command(self, id):
        self.print_status(id)
        move = False
        try:    
            if id == 0:
                move = True
                return move
            elif id == 1:
                move = False
                return move
            elif id == 2:
                valid, msg = self.move_cmd()
                if valid:
                    move = valid
                    return move, msg
                else:
                    move = valid
                    return move, msg
            else:
                msg = f"Invalid command ID."
                return None, msg
        except Exception as e:
            print(f"Error sending command: {e}")
'''