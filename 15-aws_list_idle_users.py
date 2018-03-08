#!/usr/bin/env python


import boto3.session
import sys
import datetime
import pytz

dev = boto3.session.Session(profile_name='non-production')

iam = dev.client('iam')

user_dict = iam.list_users()
user_list = user_dict['Users']

timeLimit=datetime.datetime.now() - datetime.timedelta(days=90)
current_time = datetime.datetime.now()

utc = pytz.UTC
utc_timeLimit = utc.localize(timeLimit)
utc_current_time = utc.localize(current_time)

utc_timeLimit_final  = utc_timeLimit.strftime("%Y-%m-%d %H:%M:%S")
utc_current_time_final = utc_current_time.strftime("%Y-%m-%d %H:%M:%S")

print "\n\t\t\t\t**************** List of Idle Users ****************"
print "\nBase Time" + "\t\t: " + utc_timeLimit_final
print "Current Time" + "\t\t: " + utc_current_time_final
print "\nUsers:"

counter = 0
while counter < len(user_list):
			uname = user_list[counter]['UserName']
			
			try:
				pwd_last_used = user_list[counter]['PasswordLastUsed']
				pwd_last_used_final  = pwd_last_used.strftime("%Y-%m-%d %H:%M:%S")
									
			except Exception as error:
				pwd_last_used_final = ""
			
			if pwd_last_used_final < utc_timeLimit_final:
					print "\t" + uname
			
			else:
					print "\tUser \'" + uname + "\' is an Active User."
							
			counter += 1

print "\n\t\t\t\t**************** End of Report *********************"	
			
			

			

			
			
			
			
