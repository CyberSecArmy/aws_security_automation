#!/usr/bin/env python

import boto3.session

dev = boto3.session.Session(profile_name='non-production')

s3 = dev.resource('s3')

print "\n[+] Listing all the buckets ...\n"
print "----------------------------------------------------------------"
print "Bucket-Names: " + "\n"

for bucket in s3.buckets.all():
	print "\t" + bucket.name

print "\n----------------------------------------------------------------"		
print('\n[+] The operation completed successfully...')


