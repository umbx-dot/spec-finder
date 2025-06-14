import platform
import psutil
import cpuinfo

def get_cpu_info():
    try:
        info = cpuinfo.get_cpu_info()
        cpu_name = info.get('brand_raw', 'Unknown')
        
        temp = get_cpu_temperature()
        
        return {
            "Name": cpu_name,
            "Physical Cores": psutil.cpu_count(logical=False),
            "Logical Cores": psutil.cpu_count(logical=True),
            "Max Frequency": f"{psutil.cpu_freq().max:.0f} MHz" if psutil.cpu_freq() else "Unknown",
            "Temperature": temp
        }
    except Exception as e:
        return {"Error": f"Failed to get CPU info: {str(e)}"}

def get_cpu_usage():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()
        current_freq = f"{cpu_freq.current:.0f} MHz" if cpu_freq else "Unknown"
        
        return {
            "Usage": f"{cpu_percent}%",
            "Current Frequency": current_freq
        }
    except Exception as e:
        return {"Usage": "Unknown", "Current Frequency": "Unknown"}

def get_cpu_temperature():
    try:
        if platform.system() == "Linux":
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                return f"{temps['coretemp'][0].current}°C"
            elif 'cpu_thermal' in temps:
                return f"{temps['cpu_thermal'][0].current}°C"
        return "Not available"
    except:
        return "Unknown"