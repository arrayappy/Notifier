from unittest.mock import DEFAULT
from django.db import models

# Create your models here.


class Customer(models.Model):
	service_name = models.CharField(max_length=200, default='', verbose_name='Service Name', help_text=' ')
	service_proc = models.CharField(max_length=200, default='', verbose_name='Service Proc', help_text=' ')
	service_restart_command = models.CharField(max_length=200, default='', verbose_name='Service Restart Command', help_text=' ')
	twilio_account_sid = models.CharField(max_length=200, default='', verbose_name='Twilio Account SID', help_text=' ' )
	twilio_auth_token = models.CharField(max_length=200, default='', verbose_name='Twilio Auth Token', help_text=' ' )
	twilio_messaging_service_sid = models.CharField(max_length=200, default='', verbose_name='Twilio Messaging Service SID', help_text=' ' )
	twilio_phone_number1 = models.CharField(max_length=200, default='', verbose_name='Twilio Phone Number 1', help_text=' ' )
	twilio_phone_number2 = models.CharField(max_length=200, default='', verbose_name='Twilio Phone Number 2', help_text=' ' )
	twilio_interval = models.IntegerField(default=2, verbose_name='Twilio Interval', help_text=' ' )
	
	def clean_service_name(self):
		return self.cleaned_data['service_name']

	def clean_service_proc(self):
		return self.cleaned_data['service_proc']
	
	def clean_service_restart_command(self):
		return self.cleaned_data['service_restart_command']
	
	def clean_twilio_account_sid(self):
		return self.cleaned_data['twilio_account_sid']
	
	def clean_twilio_auth_token(self):
		return self.cleaned_data['twilio_auth_token']
	
	def clean_twilio_messaging_service_sid(self):
		return self.cleaned_data['twilio_messaging_service_sid']
	
	def clean_twilio_phone_number1(self):
		return self.cleaned_data['twilio_phone_number1']

	def clean_twilio_phone_number2(self):
		return self.cleaned_data['twilio_phone_number2']
	
	def clean_twilio_interval(self):
		return self.cleaned_data['twilio_interval']

	def __str__(self):
		return self.service_name + ' ' + self.service_restart_command + ' ' + self.twilio_account_sid + ' ' + self.twilio_auth_token + ' ' + self.twilio_messaging_service_sid + ' ' + self.twilio_phone_number1 + ' ' + self.twilio_phone_number2 + ' ' + str(self.twilio_interval)