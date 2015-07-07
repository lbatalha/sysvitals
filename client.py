#!/usr/bin/env python

import psutil
import time

while True:
		
		print(chr(27) + "[2J")
		cpu_time = psutil.cpu_times()
		vmem = psutil.virtual_memory()
		swap = psutil.swap_memory()
		diskparts = psutil.disk_partitions()
		diskio = psutil.disk_partitions()

		print(cpu_time) 
		print(vmem + swap)  
		print(diskparts + diskio)
		time.sleep(1)		
