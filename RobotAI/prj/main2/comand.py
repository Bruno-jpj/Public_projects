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
import manager as c
import sys

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
    QHBoxLayout,
    QGridLayout
)
from PySide6.QtCore import (
    QSize,
    Qt
)

SET_CMD = {
    0: 'Stop',
    1: 'Auto-Exploration',
    2: 'Move to ({x}, {y}) position'
}

class CommandApp():
    def __init__(self, width=720, height=640):
        #self.w = width
        #self.h = height

        self.x = None
        self.y = None

        # App Instance
        self.app = QApplication(sys.argv)

        # Main Window
        self.window = QWidget()

        # Window Settings
        self.window.setWindowTitle(c.APP_NAME)

        # Window size
        self.window.setFixedSize(QSize(width, height))
    #
    def mainloop(self):

        # setupUI
        self.setupUI()

        # show the window
        self.window.show()

        # start the app loop
        self.app.exec()
    #
    def setupUI(self):
        main_layout = QVBoxLayout()

        # --- Auto-Move: Train ---
        auto_move_layout = QHBoxLayout()

        moveTrainLabel = QLabel("Auto-Move: Train")
        moveTrainBtn = QPushButton("Move")

        moveTrainBtn.clicked.connect(lambda: None)

        auto_move_layout.addWidget(moveTrainLabel)
        auto_move_layout.addSpacing(10)
        auto_move_layout.addWidget(moveTrainBtn)

        main_layout.addLayout(auto_move_layout)

        # --- Stop-Move: Train ---
        stop_train_layout = QHBoxLayout()

        stopTrainLabel = QLabel("Stop-Move: Train")
        stopTrainBtn = QPushButton("Stop")

        stopTrainBtn.clicked.connect(lambda: None)

        stop_train_layout.addWidget(stopTrainLabel)
        stop_train_layout.addSpacing(10)
        stop_train_layout.addWidget(stopTrainBtn)

        main_layout.addLayout(stop_train_layout)

        # --- Stop Command ---
        stop_layout = QHBoxLayout()

        stopLabel = QLabel("Stop Command")
        stopBtn = QPushButton("Stop")

        stopBtn.clicked.connect(lambda: None)

        stop_layout.addWidget(stopLabel)
        stop_layout.addSpacing(10)
        stop_layout.addWidget(stopBtn)

        main_layout.addLayout(stop_layout)

        # --- Move (x, y) ---
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        x_layout = QVBoxLayout()
        y_layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        moveLabel = QLabel("Move to (x, y)")
        vertical_layout.addWidget(moveLabel)

        # --- X ---
        Xlabel = QLabel("Insert X coordinate:")
        self.Xinput = QLineEdit()
        x_layout.addWidget(Xlabel)
        x_layout.addWidget(self.Xinput)

        # --- Y ---
        Ylabel = QLabel("Insert Y coordinate:")
        self.Yinput = QLineEdit()
        y_layout.addWidget(Ylabel)
        y_layout.addWidget(self.Yinput)

        # Aggiungo X e Y affiancati
        horizontal_layout.addLayout(x_layout)
        horizontal_layout.addSpacing(10)
        horizontal_layout.addLayout(y_layout)

        # --- Move Button ---
        moveBtn = QPushButton("Move")
        moveBtn.clicked.connect(lambda: None)
        btn_layout.addWidget(moveBtn)

        # Composizione finale
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addLayout(btn_layout)

        main_layout.addLayout(vertical_layout)

        # --- Final Layout ---
        self.window.setLayout(main_layout)
    #
    def check_command(self, id):
        try:
            self.last_cmd_id = id
            print(f"[GUI] Ultimo comando: [{SET_CMD.get(id, 'Unknown')}]")
        except Exception as e:
            print(f"Error: Catch Exception in check_command: {e}")
    #
    def check_xy(self):
        try:
            x = self.Xinput.text()
            y = self.Yinput.text()
            if x.isnumeric() and y.isnumeric():
                msg = SET_CMD[2].format(x=x, y=y)
                point = (x, y)
                return msg, point
            else:
                msg = "Invalid Coordinates"
                return msg, None
        except Exception as e:
            msg = f"X/Y Input <Unexpected Error: [{e}]"
            print(msg)
    #
    def send_command(self):
        if self.last_cmd_id is None:
            raise ValueError("Value cannot be None")
        #
        cmd_id = self.last_cmd_id

        
#
'''
def main():
    app = CommandApp()
    app.mainloop() 
#
if __name__ == "__main__":
    main()
'''