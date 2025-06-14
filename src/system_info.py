import platform
import psutil
import datetime

def get_system_info():
    try:
        uptime_seconds = psutil.boot_time()
        uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(uptime_seconds)
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        uptime_str = f"{days}d {hours}h {minutes}m"
        
        return {
            "Operating System": f"{platform.system()} {platform.release()}",
            "Version": platform.version(),
            "Architecture": platform.architecture()[0],
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Uptime": uptime_str
        }
    except Exception as e:
        return {"Error": f"Failed to get system info: {str(e)}"}