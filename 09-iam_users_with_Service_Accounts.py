#!/usr/bin/env python

import boto3.session
import sys

dev = boto3.session.Session(profile_name='non-production')

iam = dev.resource('iam')

for user in iam.users.all():
    # Nothing is initially loaded
    profile = user.LoginProfile()
    try:
       profile.load();
        
    except Exception as error:
        if 'NoSuchEntity' in error.response['Error']['Code']:
            name = user.name
