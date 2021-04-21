#!/usr/bin/python
import psutil
import time
import configparser
from subprocess import call, STDOUT
import signal
import sys
import json
import os
import requests
import subprocess
from sms import send_sms
requests.packages.urllib3.disable_warnings()

if os.geteuid() == 0:
    print("Thanks for root previlages!")
else:
    print("Hey, You are not a root please enter your password.")
    subprocess.call(['sudo', 'python3'] + sys.argv)
    sys.exit()


print( "[+] Starting Process monitor")

print ("[-] Loading config file")
Config = configparser.ConfigParser()
Config.read("config.ini")
INTERVAL = int(Config.get('Other', 'Interval'))  #Check every n seconds
FNULL = open(os.devnull, 'w')

#Read service monitoring file
print ("[-] Loading Services file")
with open('services.json') as json_data:
    SERVICES = json.load(json_data)

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
          print( "[!] At least one service in your services.json is not already running. Please ensure services are already running before starting.")
          exit(1)

    while True:
      mem = int(psutil.virtual_memory().percent) #Percent mem used
      cpu = int(  
      for s in SERVICES:
        name, proc, restart = s.get("name"), s.get("proc"), s.get("restart")
        if not isRunning(proc):
          print ("[*] {} has stopped. Dispatching SMS.".format(name))
          if restart:
            msg="Dear Sir/Madam,\n{} has stopped... \n\n CPU Load: {} \n\n RAM Load: {}".format(name,cpu,mem)
           # print(msg)
            send_sms(msg)
            #time.sleep(10)
            time.sleep(30)
            r = call(restart.split(), stdout=FNULL, stderr=STDOUT)
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
            msg="Dear Human,\n\n has stopped. I will not attempt a restart{}.\n\nCPU load:{} \nRAM load: {} \n\nLove,\nYour Server".format(name,cpu,mem)
            print(msg)
            send_sms(msg)

      time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
