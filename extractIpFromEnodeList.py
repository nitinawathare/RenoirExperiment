#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime

import re
import json
# from urllib2 import urlopen
from urllib.request import urlopen


def main():

	filename = "enodeIds"  

	uniqueIpList = []
	with open(filename) as f:
		for line in f:
			data = line.split(' ')
			if len(data) < 4:
				continue
			if "+" in data[0] or "+" in data[1] or "+" in data[2] or "+" in data[3]:
				continue
			if "x" in data[0] or "x" in data[2] or "x" in data[3]:
				continue
			if data[0]=="" or data[1]=="" or data[2]=="" or data[3]=="":
				continue
			# print(data[3])
			enodeSplit = data[3].split(':')
			if len(enodeSplit) < 3:
				continue
			IP = enodeSplit[1].split("@")[1]
			if IP not in uniqueIpList:
				uniqueIpList.append(IP)
			# print(IP)
	print(uniqueIpList)	
	for ip in uniqueIpList:
		url = 'http://ipinfo.io/'+ip+'/json'
		response = urlopen(url)
		data = json.load(response)
		country=data['country']
		print(url,end='')
		print(" : ",end='')
		print(country,)
if __name__ == "__main__":
    # print(sys.argv[1])
    main()