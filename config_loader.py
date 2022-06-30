import json
import os
from os import path

def config_loader():
#   desktop = os.path.join(os.path.expanduser("~"), "Desktop/notifier/")
#   filename = os.path.join(desktop, "config.json")
  filename = "config.json"
  listObj = []
  	
  # Check if file exists
  if path.isfile(filename) is False:
      raise Exception("File not found")

  # Read JSON file
  with open(filename) as fp:
      listObj = json.load(fp)
  return listObj
