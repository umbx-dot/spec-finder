import platform
import subprocess
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        return response.json().get('ip', 'Unknown')
    except:
        return "Unknown"

def get_country(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json', timeout=10)
        data = response.json()
        country = data.get('country', 'Unknown')
        city = data.get('city', '')
        region = data.get('region', '')
        location = f"{city}, {region}" if city and region else country
        return location
    except:
        return "Unknown"

def get_ping():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["ping", "-n", "1", "8.8.8.8"], 
                capture_output=True, 
                timeout=10,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            if result.returncode == 0 and result.stdout:
                output = result.stdout.decode('cp1252', errors='ignore')
                lines = output.split('\n')
                for line in lines:
                    if "Zeit=" in line or "time=" in line:
                        try:
                            if "Zeit=" in line:
                                time_part = line.split("Zeit=")[1].split("ms")[0].strip()
                            else:
                                time_part = line.split("time=")[1].split("ms")[0].strip()
                            return time_part + "ms"
                        except:
                            continue
        else:
            result = subprocess.run(
                ["ping", "-c", "1", "8.8.8.8"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0 and result.stdout and "time=" in result.stdout:
                try:
                    time_part = result.stdout.split("time=")[1].split(" ms")[0]
                    return time_part + "ms"
                except:
                    pass
        return "No response"
    except subprocess.TimeoutExpired:
        return "Timeout"
    except Exception:
        return "Failed"

def get_network_info():
    try:
        public_ip = get_public_ip()
        
        return {
            "Public IP": public_ip,
            "Location": get_country(public_ip),
            "Ping (Google DNS)": get_ping()
        }
    except Exception as e:
        return {"Error": f"Failed to get network info: {str(e)}"}