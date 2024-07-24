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
        
        info_str = (
            "System Information:\n"
            f"Hostname : {hostname}\n"
            f"Internal IP: {internalIP}\n"
            f"External IP: {externalIP}\n"
            f"Processor : {processor}\n"
            f"OS: {operatingSystem}\n"
            f"OS Version: {OSversion}\n"
            f"Machine Name: {machine}\n"
            f"CPU Count: {cpu_count}\n"
            f"CPU Frequency: {cpu_freq.current} MHz\n"
            f"CPU Usage: {cpu_usage}%\n"
            f"Total Memory: {virtual_memory.total / (1024 ** 3):.2f} GB\n"
            f"Available Memory: {virtual_memory.available / (1024 ** 3):.2f} GB\n"
            f"Used Memory: {virtual_memory.used / (1024 ** 3):.2f} GB\n"
            f"Memory Usage: {virtual_memory.percent}%\n"
            f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB\n"
            f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB\n"
            f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB\n"
            f"Disk Usage: {disk_usage.percent}%\n"
            f"Boot Time: {boot_time}\n"
            f"Current Directory: {current_directory}\n"
        )
        
        for key, value in user_environment.items():
            info_str += f"{key}: {value}\n"
        
        # write all details to a file
        with open('systemInfo.txt', 'w') as f:           
            f.write(info_str)
            
            
# get_System_Information()