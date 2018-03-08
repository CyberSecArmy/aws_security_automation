#!/usr/bin/env python

import boto3.session
import sys

dev = boto3.session.Session(profile_name='non-production')

ec2 = dev.resource('ec2')

for instance in ec2.instances.all():
    print instance.id + "\t\t" , instance.state
