#!/usr/bin/env python

import boto3.session
import sys

if len(sys.argv) != 2:
	print "\n[+] Usage: aws_s3_bucket_Check_ACLs.py <bucket_name>"
	sys.exit(0)

dev = boto3.session.Session(profile_name='non-production')

s3 = dev.resource('s3')

print "\n[+] Connecting to bucket \"%s\" " %sys.argv[1]
print "\n[+] Connected to bucket \"%s\"" %sys.argv[1] + " successfully ..."
print "\n[+] Checking permissions on bucket \"%s\"" %sys.argv[1]

print "\n******************************** Start of Report ********************************\n"
print "\t\tBucket-Name    : " + sys.argv[1]
bucket_acl = s3.BucketAcl(sys.argv[1])

try:
	for grant in bucket_acl.grants:	
		try:
			grant_permission = grant['Permission'].lower()
			
			if grant_permission == 'read':
				print('\t\tAccess-Control : Read')
				print('\t\tPublic Access  : List Objects')
				
			elif grant_permission == 'write':
				print('\t\tAccess-Control : Write')
				print('\t\tPublic Access  : Write Objects')

			elif grant_permission == 'read_acp':
				print('\t\tAccess-Control : Write')
				print('\t\tPublic Access  : Read Bucket Permissions')

			elif grant_permission == 'write_acp':
				print('\t\tAccess-Control : Write')
				print('\t\tPublic Access  : Write Bucket Permissions')

			elif grant_permission == 'full_control':
				print('\t\tAccess-Control : Full Control')
				print('\t\tPublic Access  : Full Control')
					
		except Exception as error:
			print error
except Exception as error:
	print error	
		
print "\n******************************** End of Report **********************************\n"		
print('\n[+] The operation completed successfully...')
