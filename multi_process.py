#!/usr/bin/env python
# encoding: utf-8
# author: @xd_xd
# email: 646901834@qq.com
# blog: http://stayliv3.github.io/






from hotqueue import HotQueue
import sqlite3
import subprocess
import threading
# from IPy import IP

#配置信息

RedisServer = "127.0.0.1"

RedisPort = 6379


# sqlite3db = "/root/wydomain/pentest.sqlite3"

# tangchao = "/root/TangScan/tangscan/"
# sqlite3db = ""

def scanprocess(ipblocks,domain):
	scan_cmd = "python wyportmap_sqlite3.py " + ipblocks + scanname + str(domain)

	return scan_cmd



	



def scanrun(target):
	# cmd1 = scanprocess('mongodb_unauth',target)
	cmd1 = scanprocess('elastic',target)

	print cmd1
	subprocess.call(cmd1,shell = True)

	

queue = HotQueue("target", host=RedisServer, port=RedisPort, db=0)


class start_suifeng(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):

		while 1:
			target = queue.get(block = True)
			if target.count('/') == 1:
				for ip in IP(target):
					scanrun(ip)

			else:
				scanrun(target)

# scanrun(queue.get())

def main():
	threads = []
	threadsnum = 20
	for i in range(threadsnum):
		# prinwt i
		t_start_suifeng = start_suifeng()
		threads.append(t_start_suifeng)

	for i in range(threadsnum):
		threads[i].start()
	for i in range(threadsnum):
		threads[i].join()



main()