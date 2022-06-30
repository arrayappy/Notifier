# import socket            
import platform
from datetime import datetime
import cpuinfo
import socket
import uuid
import re
import psutil
from subprocess import call, STDOUT
import json
import os
from os import path
import requests
import time

desktop = os.path.join(os.path.expanduser("~"), "Desktop/notifier/")
filename = os.path.join(desktop, "info.json")
listObj = []

# Check if file exists
if path.isfile(filename) is False:
    raise Exception("File not found")

# Read JSON file
with open(filename) as fp:
    listObj = json.load(fp)

listObj.clear()

def services_information():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop/notifier/")
    filename = os.path.join(desktop, "config.json")
    listObj = []
	
	# Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
	
	# Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)

    def isRunning(name):
        for proc in psutil.process_iter():
            if proc.name() == name:
                return 'Running'
        return 'Stopped'
    return {
        'status':isRunning(listObj[0]['service_proc']), 'name': listObj[0]['service_name'], 'proc': listObj[0]['service_proc'], 'restart':listObj[0]['service_restart_command'] 
    }

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_information():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    boot_time = f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    return {
        'system': uname.system,
        'node_name': uname.node,
        'release': uname.release,
        'version': uname.version,
        'machine': uname.machine,
        'processor': uname.processor,
        'processor_brand': cpuinfo.get_cpu_info()['brand_raw'],
        'boot_time': boot_time,
    }

def cpu_usage():
    return {
        'cpu_usage': psutil.cpu_percent(),
        'physical_cores': psutil.cpu_count(logical=False),
        'total_cores': psutil.cpu_count(logical=True),
        'memory_usage': psutil.virtual_memory()[2],
    }

def memory():
    svmem = psutil.virtual_memory()
    return {
        'total': get_size(svmem.total),
        'available': get_size(svmem.available),
        'used': get_size(svmem.used),
        'percentage': svmem.percent,
    }

def network():
    net_io = psutil.net_io_counters()
    return {
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'mac_address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
        'total_bytes_sent': get_size(net_io.bytes_sent),
        'total_bytes_received': get_size(net_io.bytes_recv),
    }

def disk():
    partitions = psutil.disk_partitions()
    partition_usage = psutil.disk_usage(partitions[0].mountpoint)
    storage_percentage = int(partition_usage.percent)
    return {
        'total': get_size(partition_usage.total),
        'used': get_size(partition_usage.used),
        'free': get_size(partition_usage.free),
        'percentage': storage_percentage,
    }

while(True):
  time.sleep(1)
  context = {'context':{'services': services_information(), 'system': system_information(), 'cpu': cpu_usage(), 'memory': memory(), 'network': network(), 'disk': disk()}}
  listObj = context
  with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))