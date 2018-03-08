#!/usr/bin/env python

import boto3.session
import sys

dev = boto3.session.Session(profile_name='non-production')

# Create IAM client
iam = dev.client('iam')

# List server certificates through the pagination interface
paginator = iam.get_paginator('list_server_certificates')
for response in paginator.paginate():
    
	if len(response['ServerCertificateMetadataList']) == 0 :
		print "\nNo Server Certificates found, so cannot retrieve their Expiration Date."
		print "Please ensure server certificate(s) exists."
	
	else :
		print "Server Expiration Date is: " + (response['ServerCertificateMetadataList']['Expiration'])
		
