#!/usr/bin/env python

import psutil
import time
import json
import urllib, urllib2
url = "http://localhost:5000/post"



while True:
		
		print(chr(27) + "[2J")
		cpu_time = psutil.cpu_times()
		vmem = psutil.virtual_memory()
		swap = psutil.swap_memory()
		diskparts = psutil.disk_partitions()
		diskio = psutil.disk_partitions()

		data = json.dumps([ cpu_time, vmem, swap, diskparts, diskio])

		
		req = urllib2.Request(url, data, headers={'Content-type': 'application/json'})

		response = urllib2.urlopen(req)
		print(response.read())
		
		
		time.sleep(1)		
