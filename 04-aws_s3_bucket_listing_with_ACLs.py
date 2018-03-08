#!/usr/bin/env python

import boto3.session

dev = boto3.session.Session(profile_name='non-production')

s3 = dev.resource('s3')

print "\n[+] Listing all the buckets with ACLs...\n"
print "----------------------------------------------------------------"

for bucket in s3.buckets.all():	
	print "Bucket-Name: " + bucket.name
	bucket_acl = bucket.Acl()
	
	try:
		for grant in bucket_acl.grants:	
			try:
				grant_permission = grant['Permission'].lower()
				
				if grant_permission == 'read':
					print('Access-Control: Read ; Public Access: List Objects')

				elif grant_permission == 'write':
					print('Access-Control: Write ; Public Access: Write Objects')

				elif grant_permission == 'read_acp':
					print('Access-Control: Write ; Public Access: Read Bucket Permissions')

				elif grant_permission == 'write_acp':
					print('Access-Control: Write ; Public Access: Write Bucket Permissions')

				elif grant_permission == 'full_control':
					print('Access-Control: Full Control ; Public Access: Full Control')
			except Exception as error:
				print error
	except Exception as error:
				print error	
	
	print "\n----------------------------------------------------------------\n"
		
print('\n[+] The operation completed successfully...')	


