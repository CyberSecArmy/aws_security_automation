#!/usr/bin/env python

import boto3									# Required packages/modules to import
import boto3.session
import datetime
import sys

dev = boto3.session.Session(profile_name='production')	                        # creating session and credential validation

'''
NOTE: In the above code line, 'production' is the name of the profile being mentioned in the 'credentials' file under which,
      user credentials are mentioned to validate against aws.

Path to 'credentials' file: The location where 'aws' folder is created during installation. (Ex: C:\users\aws\ --> 'credentials' and 'config' files would be present)

'''

client = dev.client('waf')							# creating variable for the client method and calling waf component

end = datetime.datetime.utcnow()						# end time
start = end - datetime.timedelta(hours=2)				        # start time

response = client.get_sampled_requests(					        # making api call to 'get_sampled_requests' method to get the required results
    WebAclId='a517abcd-2aa6-12d7-9c1d-123f31447abc7',	                        # WebAclId in question
    RuleId='123ad85c-edf3-1b19-b955-548f84e401zz',		                # RuleId in question
    TimeWindow={
		'StartTime': start,						# Start Time
        'EndTime': end								# End Time
    },
    MaxItems=500								# Max Items to retrieve
)
print response

# File I/O operation being performed... dumping all the response results to a file.

sys.stdout=open("aws_waf_prod_logs.txt","a")
print ("**************************************************************")
print datetime.datetime.utcnow()
print ("**************************************************************")
print (response)
sys.stdout.close()
