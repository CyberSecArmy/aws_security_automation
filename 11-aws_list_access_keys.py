#!/usr/bin/env python

import boto3.session
import sys

if len(sys.argv) != 2:
	print "\n[+] Usage: aws_list_access_keys.py <user_name>"
	sys.exit(0)

dev = boto3.session.Session(profile_name='non-production')

iam = boto3.client('iam')						# Creating IAM client

try:
	paginator = iam.get_paginator('list_access_keys')		# List access keys through the pagination interface.

	for response in paginator.paginate(UserName=sys.argv[1]):       # Pass in the IAM_USER_NAME over here
		print(response)

except Exception as error:
	print "\nSorry, You are an Unauthorized User to query this, please elevate your privileges and try again."
