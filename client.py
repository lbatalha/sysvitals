#!/usr/bin/env python

import psutil
import time
import json
import urllib, urllib2
import socket
url = "http://localhost:5000/post"



while True:
		print(chr(27) + "[2J")
		
		cpu, disks, host_info, memory, network, processes, other = [],[],[],[],[],[],[] 
		
		host_info.append(socket.gethostname())
		#host_info.append(
		cpu.append(vars(psutil.cpu_times()))
		cpu.append(psutil.cpu_percent(percpu=True))
		
		memory.append(vars(psutil.virtual_memory()))
		memory.append( vars(psutil.swap_memory()))
		
		disks.append(vars(psutil.disk_io_counters()))
		
	
		if_addr = {}
		for k, v in psutil.net_if_addrs().iteritems():
			if_addr[k] = v
		
		netio = {}
		for k, v in psutil.net_io_counters(pernic=True).iteritems():
			netio[k] = vars(v)

		network.append(if_addr)
		network.append(netio)
		
		diskparts = []
		for i in psutil.disk_partitions():
			diskparts.append(vars(i))
		
	
		data = json.dumps([ host_info, cpu, memory, disks, network, processes, other])
		
		req = urllib2.Request(url, data, headers={'Content-type': 'application/json'})

		response = urllib2.urlopen(req)
		print(response.read())
		
		
		time.sleep(1)		
