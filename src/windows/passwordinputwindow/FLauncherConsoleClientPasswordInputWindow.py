from PySide6.QtWidgets import QWidget

from src.windows.WindowManager import WindowManager
from src.windows.passwordinputwindow.Window import Ui_Form


class FLauncherConsoleClientPasswordInputWindow(QWidget):
    finished_password: str = ""

    def __init__(self):
        super(FLauncherConsoleClientPasswordInputWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._setup_connections()
        self._setup_ui()

    def _setup_ui(self):
        self.ui.inputPassword.setFocus()
        self.ui.btnOk.setEnabled(False)
    def _setup_connections(self):
        self.ui.inputPassword.textChanged.connect(self._on_password_change)
        self.ui.btnOk.clicked.connect(self._on_button_ok_clicked)

    def _on_password_change(self):
        text = self.ui.inputPassword.text()
        if text: self.ui.btnOk.setEnabled(True)
        else: self.ui.btnOk.setEnabled(False)
    def _on_button_ok_clicked(self):
        self.finished_password = self.ui.inputPassword.text()
        self.close()
        WindowManager().create_main_window().show()

