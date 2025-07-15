import os
import hashlib

from src.logs.LogManager import LogManager


def is_windows():
    if os.name == "nt": return True
    return False

def is_linux():
    if os.name == "posix": return True
    return False

def get_link_real_path(file_path: str) -> str:
    if file_path.endswith('.lnk'):
        try:
            import win32com.client
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(file_path)
            real_path = shortcut.Targetpath
            return real_path
        except ImportError:
            LogManager().send_error_log("Win32 com import error, platform not support .lnk files")
            return ""
        except Exception as e:
            LogManager().send_error_log(f"Reading lnk error: {str(e)}")
            return ""
    elif os.path.islink(file_path):
        try:
            real_path = os.path.realpath(file_path)
            return real_path
        except Exception as e:
            LogManager().send_error_log(f"Reading symlink error: {str(e)}")
            return ""
    return file_path

def sha256_hash(text: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()