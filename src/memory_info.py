import psutil

def get_memory_info():
    try:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        total_gb = memory.total / (1024**3)
        used_gb = memory.used / (1024**3)
        available_gb = memory.available / (1024**3)
        
        swap_total_gb = swap.total / (1024**3)
        swap_used_gb = swap.used / (1024**3)
        
        return {
            "Total RAM": f"{total_gb:.1f} GB",
            "Used RAM": f"{used_gb:.1f} GB ({memory.percent}%)",
            "Available RAM": f"{available_gb:.1f} GB",
            "Total Swap": f"{swap_total_gb:.1f} GB" if swap_total_gb > 0 else "None",
            "Used Swap": f"{swap_used_gb:.1f} GB ({swap.percent}%)" if swap_total_gb > 0 else "None"
        }
    except Exception as e:
        return {"Error": f"Failed to get memory info: {str(e)}"}