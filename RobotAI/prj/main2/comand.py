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
    0: 'stop',
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
        moveLabel = QLabel("Stop Command")
        moveBtn = QPushButton("Stop")
        moveBtn.clicked.connect(lambda: self.check_command(0))

        # Start CMD: start robot auto-exploration
        AutoExpLabel = QLabel("Start Auto-Exploration")
        AutoExpBtn = QPushButton("Start")
        AutoExpBtn.clicked.connect(lambda: self.check_command(1))

        # Move CMD: move to (x,y) chosen position
        Xlabel = QLabel("Insert X coordinate")
        self.Xinput = QLineEdit()

        Ylabel = QLabel("Insert Y coordinate")
        self.Yinput = QLineEdit()

        MoveLabel = QLabel("Move to (X,Y) Position")
        MoveBtn = QPushButton("Move")

        MoveBtn.clicked.connect(lambda: self.check_command(2))

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
    def check_command(self, id):
        try:
            self.last_cmd_id = id
            print(f"[GUI] Ultimo comando: [{SETCMD.get(id, 'Unknown')}]")
        except Exception as e:
            print(f"Error: Catch Exception in check_command: {e}")
    #
    def send_command(self):
        if self.last_cmd_id is None:
            return None, "None Command Inserted", None
        #
        cmd_id = self.last_cmd_id
        # return Move, msg, point(x, y)
        try:
            if cmd_id == 0:
                # STOP
                msg = f"Command: {SETCMD[cmd_id]}"
                return False, msg, False
            elif cmd_id == 1:
                # START-AUTO
                msg = f"Command: {SETCMD[cmd_id]}"
                return True, msg, None
            elif cmd_id == 2:
                # MOVE (X, Y)
                x = self.Xinput.text()
                y = self.Yinput.text()
                
                if x.isnumeric() and y.isnumeric():
                    msg = SETCMD[cmd_id].format(x=x, y=y)
                    point = (x, y)
                    return True, msg, point
                else:
                    msg = "Invalid Coordinates"
                    return None, msg, None
            else:
                msg = "Invalid Command ID"
                return None, msg, None
        except Exception as e:
            msg = f"Error Sending Command: {e}"
            print(msg)
            return None, msg, None
#
'''
def main():
    app = CommandApp()
    app.mainloop() 
#
if __name__ == "__main__":
    main()

def check_command(self, id):
    try:
        self.last_cmd_id = id
        print(f"[GUI] Ultimo comando: [{SETCMD.get(id, 'Unknown')}]")

        if id == 1:  # start auto-exploration
            from agent import Agent, Simulation, TrainingThread
            self.agent = Agent()
            self.game = Simulation()
            self.training_thread = TrainingThread(self.agent, self.game, self)
            self.training_thread.update_signal.connect(self.show_log)
            self.training_thread.start()

    except Exception as e:
        print(f"Error: Catch Exception in check_command: {e}")

'''
