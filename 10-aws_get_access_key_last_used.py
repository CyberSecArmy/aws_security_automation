#!/usr/bin/env python

import boto3.session
import sys

if len(sys.argv) != 2:
	print "\n[+] Usage: aws_get_access_key_last_used.py <access_key-id>"
	sys.exit(0)

dev = boto3.session.Session(profile_name='non-production')

iam = dev.client('iam')						# Creating IAM client

try:

	response = iam.get_access_key_last_used(		# Get last use of access key
		AccessKeyId = sys.argv[1]			# Remove the Key after testing
	)

	print(response['AccessKeyLastUsed'])
except Exception as error:
	print "\nSorry, You are an Unauthorized User to query this, please elevate your privileges and try again."
