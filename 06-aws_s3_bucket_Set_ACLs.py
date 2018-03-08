#!/usr/bin/env python

import boto3
import sys

if len(sys.argv) != 3:
	print "\n[+] Usage: aws_s3_bucket_Set_ACLs.py <bucket_name> <acl_name>"
	sys.exit(0)

dev = boto3.session.Session(profile_name='non-production')

s3 = dev.resource('s3')

print "\n[+] Connecting to bucket %s " %sys.argv[1]

bucket = s3.BucketAcl(sys.argv[1])

try:

	print "\n[+] Setting ACL \'%s\' on bucket \'%s\'" %(sys.argv[2],sys.argv[1])
	bucket.set_acl(sys.argv[2])
	print "[+] Fetching New Permissions for %s " %sys.argv[1]

	for grant in bucket.get_acl().acl.grants :
	  print grant.permission, grant.display_name

except Exception as error:
	print "\nERROR: Unrecognized input provided, please pass correct Bucket_Name/ACL value to be set."
