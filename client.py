#!/usr/bin/env python

import psutil
import time
import json
import urllib, urllib2
url = "http://localhost:5000/post"



while True:
		
		print(chr(27) + "[2J")
		cpu_time = vars(psutil.cpu_times())
		cpu_percent = psutil.cpu_percent(percpu=True)
		vmem = vars(psutil.virtual_memory())
		swap = vars(psutil.swap_memory())
		diskparts = []
		for a in psutil.disk_partitions():
			diskparts.append(vars(a))
		
		diskio = vars(psutil.disk_io_counters())
	
		data = json.dumps([ cpu_time, cpu_percent, vmem, swap, diskparts, diskio])
		
		req = urllib2.Request(url, data, headers={'Content-type': 'application/json'})

		response = urllib2.urlopen(req)
		print(response.read())
		
		
		time.sleep(1)		
