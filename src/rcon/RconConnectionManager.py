from logging import exception
from typing import TypedDict

from mcrcon import MCRcon

from src.logs.LogManager import LogManager


class RconConnectionData(TypedDict):
    ip: str
    port: int
    password: str


class RconConnectionManager:
    _instance = None
    _logger = LogManager()

    def __init__(self):
        if hasattr(self, '_initialized'): return
        self._initialized = True
        self.current_server_data: RconConnectionData | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_mcrcon(self) -> MCRcon:
        return MCRcon(
            host=self.current_server_data.get("ip"),
            port=self.current_server_data.get("port"),
            password=self.current_server_data.get("password")
        )

    def validate_connect(self, connection_data: RconConnectionData) -> bool:
        mcr = MCRcon(
            host=connection_data.get("ip"),
            port=connection_data.get("port"),
            password=connection_data.get("password")
        )
        try:
            mcr.connect()
            welcome_msg: str = mcr.command("list").strip()
            mcr.disconnect()
            self._logger.send_success_log(f"Get welcome message of rcon connection: /list -> {welcome_msg}")
            return True
        except Exception as e:
            self._on_validation_error(str(e))
            return False

    def _on_validation_error(self, err: str):
        self._logger.send_error_log(f"Error on rcon connection: {err}")

    def connect_to_rcon(self, connection_data: RconConnectionData):
        validation_result: bool = self.validate_connect(connection_data)
        if validation_result:
            self._logger.send_success_log(
                f"Success rcon connection." + " "
                f"Connected to | {connection_data.get("ip")}:{connection_data.get("port")}"
            )
            self.current_server_data = connection_data
        else:
            self._logger.send_error_log(
                f"Connection failed to | {connection_data.get("ip")}:{connection_data.get("port")}"
            )

    def disconnect_to_rcon(self):
        self.current_server_data = None

    def is_connected(self) -> bool:
        return self.current_server_data is not None

    def execute_command(self, command: str) -> str:
        validation_result: bool = self.validate_connect(self.current_server_data)
        if validation_result:
            mcrcon = self.create_mcrcon()
            mcrcon.connect()
            result = mcrcon.command(command)
            mcrcon.disconnect()
            return result.strip()
        return ""

    def convert_json_data_to_rcon_connection_data(self, json: dict) -> RconConnectionData | None:
        if "ip" in json and "port" in json and "password" in json:
            return RconConnectionData(ip=json["ip"],port=int(json["port"]), password=json["password"])
        return None