import os
from src.operatingsystem import OperatingSystemManager


def main():
    current_directory = os.getcwd()
    compile_cmds_linux = [
        f"pyside6-uic main_window.ui -o {current_directory}/../src/windows/mainwindow/Window.py",
        f"pyside6-uic password_input_window.ui -o {current_directory}/../src/windows/passwordinputwindow/Window.py",
    ]
    if OperatingSystemManager.is_linux():
        for cmd in compile_cmds_linux:
            print("Use:",cmd)
            os.system(cmd)
    else:
        print("Not is linux!")


if __name__ == "__main__": main()