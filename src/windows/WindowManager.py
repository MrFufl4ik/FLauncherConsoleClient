class WindowManager:
    _instance = None

    def __init__(self):
        if hasattr(self, '_initialized'): return
        self._initialized = True
        self.password_input_window = None
        self.main_window = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_main_window(self) -> 'FLauncherConsoleClientMainWindow':
        if self.has_main_window(): return self.get_main_window()
        from src.windows.mainwindow.FLauncherConsoleClientMainWindow import FLauncherConsoleClientMainWindow
        self.main_window = FLauncherConsoleClientMainWindow()
        return self.get_main_window()
    def has_main_window(self) -> bool:
        return self.get_main_window() is not None
    def get_main_window(self) -> 'FLauncherConsoleClientMainWindow':
        return self.main_window

    def create_password_input_window(self) -> 'FLauncherConsoleClientPasswordInputWindow':
        if self.has_password_input_window(): return self.get_password_input_window()
        from src.windows.passwordinputwindow.FLauncherConsoleClientPasswordInputWindow import FLauncherConsoleClientPasswordInputWindow
        self.password_input_window = FLauncherConsoleClientPasswordInputWindow()
        return self.get_password_input_window()
    def has_password_input_window(self):
        return self.get_password_input_window() is not None
    def get_password_input_window(self) -> 'FLauncherConsoleClientPasswordInputWindow':
        return self.password_input_window