#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime

def main(path):
	print(path)
	filename = path+"/blockInfo" 
	with open(filename) as f:
		for line in f:
			data = line.split(' ')
			if len(data) < 3:
				continue
			#if isinstance(float(data[3][:-3]), float):
			#	print("**********************")
			#	continue
			#if data[0]:
			#	print(data[0],end='')
			#if data[1]:
                        #        print(data[1],end='')
			#print(str(data[0]+" : "+data[2])+" "+data[3])
			if "+" in data[0] or "+" in data[1] or "+" in data[2] or "+" in data[3]:
				print("**********************")
				continue
			if "x" in data[0] or "x" in data[2] or "x" in data[3]:
				continue
			
			if data[0]=="" or data[1]=="" or data[2]=="" or data[3]=="":
                                continue
			if  not data[2].startswith("2019"):
				continue
			#try:
			utc_time = datetime.strptime(data[2]+" "+data[3][:-3], "%Y-%m-%d %H:%M:%S.%f")
			epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
			print(data[0],end='')
			print(" ",end='')
			print(epoch_time)
			#except:
			#    raise ValueError("Something went wrong")
			#else:
			#	print("oh yay no exception")
			#finally:
			#	print("leaving the try block")
				#continue
			#if len(data) < 2:
			#	print(len(data))
			#print("")

if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])
