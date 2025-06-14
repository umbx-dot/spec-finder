import platform
import getpass
from screeninfo import get_monitors

def get_python_version():
    try:
        return platform.python_version()
    except:
        return "Unknown"

def get_current_user():
    try:
        return getpass.getuser()
    except:
        return "Unknown"

def get_monitor_count():
    try:
        monitors = get_monitors()
        if monitors:
            return f"{len(monitors)} monitor(s)"
        return "Unknown"
    except:
        return "Unknown"

def get_misc_info():
    try:
        return {
            "Python Version": get_python_version(),
            "Current User": get_current_user(),
            "Monitors": get_monitor_count()
        }
    except Exception as e:
        return {"Error": f"Failed to get misc info: {str(e)}"}