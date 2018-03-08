#!/usr/bin/env python

import boto3.session
import sys

dev = boto3.session.Session(profile_name='non-production')

s3 = dev.resource('s3')

for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
