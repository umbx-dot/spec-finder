import platform
import subprocess
import requests
import speedtest

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

def get_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        return f"Down: {download_speed:.1f} Mbps, Up: {upload_speed:.1f} Mbps"
    except Exception as e:
        return f"Test failed: {str(e)}"

def get_ping():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["ping", "-n", "1", "8.8.8.8"], 
                capture_output=True, 
                text=True, 
                timeout=10,
                encoding='utf-8',
                errors='replace'
            )
            if result.returncode == 0 and "time=" in result.stdout:
                return result.stdout.split("time=")[1].split("ms")[0] + "ms"
        else:
            result = subprocess.run(
                ["ping", "-c", "1", "8.8.8.8"], 
                capture_output=True, 
                text=True, 
                timeout=10,
                encoding='utf-8',
                errors='replace'
            )
            if result.returncode == 0 and "time=" in result.stdout:
                return result.stdout.split("time=")[1].split(" ms")[0] + "ms"
        return "Timeout"
    except Exception as e:
        return f"Failed: {str(e)}"

def get_network_info():
    try:
        public_ip = get_public_ip()
        
        return {
            "Public IP": public_ip,
            "Location": get_country(public_ip),
            "Internet Speed": get_internet_speed(),
            "Ping (Google DNS)": get_ping()
        }
    except Exception as e:
        return {"Error": f"Failed to get network info: {str(e)}"}