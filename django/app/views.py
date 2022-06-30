from django.shortcuts import render
from .forms import CustomerForm
import json
import os
from os import path

def index(request):
	desktop = os.path.join(os.path.expanduser("~"), "Desktop/notifier/")
	filename = os.path.join(desktop, "config.json")
	listObj = []
	
	# Check if file exists
	if path.isfile(filename) is False:
		raise Exception("File not found")
	
	# Read JSON file
	with open(filename) as fp:
		listObj = json.load(fp)
	# print(listObj)
	listObj.clear()
	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			listObj = [{'service_name': form.cleaned_data['service_name'], 'service_proc':form.cleaned_data['service_proc'], 'service_restart_command': form.cleaned_data['service_restart_command']}, {'accountSid': form.cleaned_data['twilio_account_sid'], 'authToken': form.cleaned_data['twilio_auth_token'], 'messagingServiceSid': form.cleaned_data['twilio_messaging_service_sid'], 'twilio_phone_number1': form.cleaned_data['twilio_phone_number1'], 'twilio_phone_number2': form.cleaned_data['twilio_phone_number2'], 'twilio_interval': form.cleaned_data['twilio_interval']}]
			with open(filename, 'w') as json_file:
					json.dump(listObj, json_file, 
															indent=4,  
															separators=(',',': '))
			form.save()
	context = {'form':form}
	return render(request, 'app/index.html', context)