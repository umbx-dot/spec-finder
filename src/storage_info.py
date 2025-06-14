import psutil

def get_storage_info():
    try:
        storage_info = {}
        
        for partition in psutil.disk_partitions():
            if 'cdrom' in partition.opts or partition.fstype == '':
                continue
            
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                total_gb = usage.total / (1024**3)
                used_gb = usage.used / (1024**3)
                free_gb = usage.free / (1024**3)
                percent = (used_gb / total_gb) * 100
                
                device_name = partition.device.replace('\\', '') if partition.device else partition.mountpoint
                storage_info[device_name] = f"{used_gb:.1f}/{total_gb:.1f} GB ({percent:.1f}% used)"
                
            except PermissionError:
                storage_info[partition.device] = "Access denied"
            except Exception as e:
                storage_info[partition.device] = f"Error: {str(e)}"
        
        return storage_info
    except Exception as e:
        return {"Error": f"Failed to get storage info: {str(e)}"}