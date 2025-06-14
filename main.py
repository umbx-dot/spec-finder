import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.system_info import get_system_info
from src.cpu_info import get_cpu_info, get_cpu_usage
from src.memory_info import get_memory_info
from src.gpu_info import get_gpu_info
from src.network_info import get_network_info
from src.storage_info import get_storage_info
from src.misc_info import get_misc_info

def print_header():
    print("\nSYSTEM SPECIFICATIONS")
    print("-" * 60)

def print_section(title, data):
    print(f"\n{title}:")
    for key, value in data.items():
        print(f"  {key:<20} {value}")

def collect_data():
    results = {}
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {
            executor.submit(get_system_info): 'system',
            executor.submit(get_cpu_info): 'cpu',
            executor.submit(get_cpu_usage): 'cpu_usage',
            executor.submit(get_memory_info): 'memory',
            executor.submit(get_gpu_info): 'gpu',
            executor.submit(get_network_info): 'network',
            executor.submit(get_storage_info): 'storage',
            executor.submit(get_misc_info): 'misc'
        }
        
        for future in as_completed(futures):
            category = futures[future]
            try:
                results[category] = future.result()
            except Exception as e:
                results[category] = {'Error': str(e)}
    
    return results

def main():
    print_header()
    print("Collecting system information...")
    
    start_time = time.time()
    data = collect_data()
    collection_time = time.time() - start_time
    
    print(f"Data collected in {collection_time:.2f} seconds")
    print("=" * 60)
    
    print_section("SYSTEM", data.get('system', {}))
    
    cpu_data = data.get('cpu', {})
    cpu_data.update(data.get('cpu_usage', {}))
    print_section("PROCESSOR", cpu_data)
    
    print_section("MEMORY", data.get('memory', {}))
    print_section("GRAPHICS", data.get('gpu', {}))
    print_section("NETWORK", data.get('network', {}))
    print_section("MISCELLANEOUS", data.get('misc', {}))
    
    storage_data = data.get('storage', {})
    if storage_data:
        print("\nSTORAGE:")
        for drive, info in storage_data.items():
            print(f"  {drive:<20} {info}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()