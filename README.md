# SpecFinder

This is a moduralized SpecFinder made by notidom under the MIT license.

## Features

- **Multithreaded**
- **Modular Code**
- **System Info**
- **Hardware**
- **Network**
- **Cross-platform**

## Project Structure

```
specfinder/
├── main.py              # Entry  
├── requirements.txt     # Dependencies
├── src/
│   ├── __init__.py
│   ├── system_info.py   # OS and system details
│   ├── cpu_info.py      # CPU information and usage
│   ├── memory_info.py   # RAM and swap memory
│   ├── gpu_info.py      # Graphics card details
│   ├── network_info.py  # Network and internet info
│   └── misc_info.py     # Python version, user, monitors
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/umbx-dot/spec-finder.git
```

2. Navigate to the project directory:
```bash
cd spec-finder
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

## Compatibility

- ✅ Mainly for Windows 10/11
- ✅ LIMITED Linux   
- ✅ LIMITED macOS
