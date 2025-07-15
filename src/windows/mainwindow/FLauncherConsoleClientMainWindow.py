import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from src.logs.LogManager import LogManager
from src.operatingsystem import OperatingSystemManager
from src.rcon.RconConnectionManager import RconConnectionManager, RconConnectionData
from src.secure.StealthCipher import decrypt_file
from src.windows.WindowManager import WindowManager
from src.windows.mainwindow.Window import Ui_Form


class FLauncherConsoleClientMainWindow(QMainWindow):
    _logger = LogManager()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._qt_ui_setup()
        self._qt_setup_connections()

    def _qt_ui_setup(self):
        self.setAcceptDrops(True)
        self.ui.inputConsoleCommand.setFocus()
    def _qt_setup_connections(self):
        self.ui.btnSendConsoleCommand.clicked.connect(self._on_send_console_button_clicked)

    def _on_send_console_button_clicked(self):
        command: str = self.ui.inputConsoleCommand.text()
        if not command: return
        if RconConnectionManager().is_connected():
            command_result: str = RconConnectionManager().execute_command(command)
            self.console_command_execute(command, command_result)
            self._logger.send_info_log(f"Execute command: {command} | Command result: {command_result}")
            self.ui.inputConsoleCommand.setText("")
        else: pass

    def dragEnterEvent(self, event, /):
        if event.mimeData().hasUrls(): event.accept()
        else: event.ignore()
    def dragMoveEvent(self, event, /):
        if event.mimeData().hasUrls(): event.accept()
        else: event.ignore()
    def dropEvent(self, event, /):
        if event.mimeData().hasUrls():
            file_path: str = event.mimeData().urls()[0].toLocalFile()
            real_path = OperatingSystemManager.get_link_real_path(file_path)
            if real_path and real_path.endswith('.server'):
                event.setDropAction(Qt.DropAction.CopyAction)
                self._on_config_drop(real_path)
    def _on_config_drop(self, file_path: str):
        data = decrypt_file(file_path, WindowManager().get_password_input_window().finished_password)
        if data:
            json_data = None
            try:
                json_data = json.loads(data)
            except Exception as e: self._logger.send_error_log(f"Json read error: {str(e)}")
            if json_data is None: return
            connection_data = RconConnectionManager().convert_json_data_to_rcon_connection_data(json_data)
            if connection_data is None: return
            if RconConnectionManager().is_connected(): RconConnectionManager().disconnect_to_rcon()
            RconConnectionManager().connect_to_rcon(connection_data)
            if RconConnectionManager().is_connected():
                self.setWindowTitle(
                    "FLauncherConsole | " +
                    OperatingSystemManager.sha256_hash(f"{connection_data.get("ip")}:{connection_data.get("port")}")
                )
                self.console_server_connect(connection_data)

    def console_clear(self): self.ui.textEditConsoleLog.setPlainText("")
    def console_text(self, text: str): self.ui.textEditConsoleLog.append(text)
    def console_command_execute(self, command: str, command_result: str):
        self.console_text(f"> {command}\n{command_result}")
    def console_server_connect(self, connection_data: RconConnectionData):
        self.console_text(
            "> Connected to server: " +
            OperatingSystemManager.sha256_hash(f"{connection_data.get("ip")}:{connection_data.get("port")}")
        )