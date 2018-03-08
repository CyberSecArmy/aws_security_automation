#!/usr/bin/env python


import boto3.session
import sys
import datetime
import dateutil
from dateutil import parser

dev = boto3.session.Session(profile_name='non-production')

iam = dev.client('iam')

user_dict = iam.list_users()
user_list = user_dict['Users']

print "\n\t\t\t\t**************** Start of Report ****************"

print "\n----------------------------------------------------------------------------------------------------------------"
print "User Name" + "\t\t\t\t\t\t\t\t" + "Password Last Used"
print "----------------------------------------------------------------------------------------------------------------"

counter = 0
while counter < len(user_list):
			uname = user_list[counter]['UserName']
			
			try:
				plu = user_list[counter]['PasswordLastUsed']
					
			except Exception as error:
				plu = " "
			
			print uname + "\t\t\t\t\t\t\t\t" + str(plu)
			counter += 1

print "\n\t\t\t\t**************** End of Report ****************"	
			
			

			

			
			
			
			
