#!/usr/bin/python
import psutil
import time
from subprocess import call, STDOUT
import sys
import os
import requests
import subprocess
from sms.sms import send_sms
requests.packages.urllib3.disable_warnings()
from config_loader import config_loader

if os.geteuid() == 0:
    print("Thanks for root previlages!")
else:
    print("Hey, You are not a root please enter your password.")
    subprocess.call(['sudo', 'python3'] + sys.argv)
    sys.exit()
print( "[+] Starting Process monitor")
print ("[-] Loading config file")
#Read service monitoring file
listObj=config_loader()
SERVICES = [{ 'name': listObj[0]['service_name'], 'proc': listObj[0]['service_proc'] , 'restart':listObj[0]['service_restart_command'] }]
INTERVAL = int(listObj[1]['twilio_interval'])
FNULL = open(os.devnull, 'w')

def isRunning(name):
  #"Check if a process name is running"
  for proc in psutil.process_iter():
    if proc.name() == name:
      return True
  return False

def main():
    print( "[+] Monitoring services....")
    #Inital pass through file to make sure services are running
    for s in SERVICES:
        if not isRunning(s.get("proc")):
          print( "[!] At least one service in your config.json is not already running. Please ensure services are already running before starting.")
          exit(1)

    while True:
      mem = int(psutil.virtual_memory()[2]) #Percent mem used
      cpu = int(psutil.cpu_percent())
      partitions = psutil.disk_partitions()
      partition_usage = psutil.disk_usage(partitions[0].mountpoint)
      storage_percentage = 100-int(partition_usage.percent)
      for s in SERVICES:
        name, proc, restart = s.get("name"), s.get("proc"), s.get("restart")
        if not isRunning(proc):
          print ("[*] {} has stopped. Dispatching SMS.".format(name))
          # print("[+] Restarted service successfully")
          if restart:
            msg="From notifier!\n{} has stopped... \n\n CPU Percentage: {}% \n RAM Percentage: {}% \n Available Storage: {}%".format(name,cpu,mem,storage_percentage)
            # print(msg)
            send_sms(msg)
            time.sleep(10)
            call(restart.split(), stdout=FNULL, stderr=STDOUT)
            if isRunning(proc):
               msg ="Successfully restarted {}, you owe me".format(name)
               # print(msg)
               send_sms(msg)
               print ("[-] Successfully restarted {}" .format( name))
            else:
               msg="Failed to restart {}. I'm so sorry, Sir" .format(name)
               print(msg)
               send_sms(msg)
               print ("[-] Failed to restart {}".format(name))
          else:
            msg="Service has stopped. I will not attempt a restart{}.\n\nCPU load:{} \nRAM load: {} \n\nLove,\nYour Server".format(name,cpu,mem)
            print(msg)
            send_sms(msg)
      time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
