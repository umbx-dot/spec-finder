import GPUtil

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"GPU": "No GPU detected"}
        
        gpu_info = {}
        for i, gpu in enumerate(gpus):
            prefix = f"GPU {i+1}" if len(gpus) > 1 else "GPU"
            gpu_info[f"{prefix} Name"] = gpu.name
            gpu_info[f"{prefix} Memory"] = f"{gpu.memoryUsed:.0f}/{gpu.memoryTotal:.0f} MB ({gpu.memoryUtil*100:.1f}%)"
            gpu_info[f"{prefix} Usage"] = f"{gpu.load*100:.1f}%"
            
            if gpu.temperature and gpu.temperature > 0:
                gpu_info[f"{prefix} Temperature"] = f"{gpu.temperature}°C"
            else:
                gpu_info[f"{prefix} Temperature"] = "Not available"
        
        return gpu_info
    except Exception as e:
        return {"Error": f"Failed to get GPU info: {str(e)}"}