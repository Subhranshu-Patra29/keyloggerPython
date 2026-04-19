# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

# Importing modules for getting system information
import socket
import platform
import requests
import psutil
import os
from datetime import datetime

# --------------------------------------------------------------------------------------------------------

# Source : Youtube - Grant Collins

# Gathering computer information

def get_System_Information():
    
        hostname = socket.gethostname()
        internalIP = socket.gethostbyname(hostname)
        processor = platform.processor()
        operatingSystem = platform.system()
        OSversion = platform.version()
        machine = platform.machine()
        
        try:
            externalIP = requests.get('https://checkip.amazonaws.com').text.strip()
        except Exception:
            externalIP = "Couldn't get public IP address!"

        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        cpu_usage = psutil.cpu_percent(interval=1)
        virtual_memory = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        current_directory = os.getcwd()
        user_environment = os.environ
        
        details = {
            "Hostname": hostname,
            "Internal IP": internalIP,
            "External IP": externalIP,
            "Processor": processor,
            "OS": operatingSystem,
            "OS Version": OSversion,
            "Machine Name": machine,
            "CPU Count": cpu_count,
            "CPU Frequency": f"{cpu_freq.current} MHz",
            "CPU Usage": f"{cpu_usage}%",
            "Total Memory": f"{virtual_memory.total / (1024 ** 3):.2f} GB",
            "Available Memory": f"{virtual_memory.available / (1024 ** 3):.2f} GB",
            "Used Memory": f"{virtual_memory.used / (1024 ** 3):.2f} GB",
            "Memory Usage": f"{virtual_memory.percent}%",
            "Total Disk Space": f"{disk_usage.total / (1024 ** 3):.2f} GB",
            "Used Disk Space": f"{disk_usage.used / (1024 ** 3):.2f} GB",
            "Free Disk Space": f"{disk_usage.free / (1024 ** 3):.2f} GB",
            "Disk Usage": f"{disk_usage.percent}%",
            "Boot Time": boot_time,
            "Current Directory": current_directory
        }
        
        info_str = ''
        for key, value in details.items():
            info_str += f"{key}: {value}\n"
            
        info_str1 = ''
        for key, value in user_environment.items():
            info_str1 += f"{key}: {value}\n"
        
        # write all details to a file
        with open('systemInfo.txt', 'w') as f:   
            f.write("System Information:\n\n")        
            f.write(info_str)
            f.write("\nEnvironment Path Variables and Other Details:\n\n")
            f.write(info_str1)
            
        return details
            
            
# get_System_Information()