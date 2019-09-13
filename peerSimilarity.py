#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime


transactionList = []
peerTransListDict = defaultdict(list)
peerSimilarityValues = defaultdict(list)
#blockSkipCount = 0
def main(path):
	print(path)
	filename = path+"/blockInfo"  
	txPath = path+"/abc.txt"
	txReceivedFp = open(txPath, "r")
	blockCount = 0
	previousBlockNumber = 1
	blockSkipCount = 0
	# print("path*****"+txPath)
	with open(filename) as f:
		for line in f:
			#print(line)
			count = 0
			transactionCount = 0
			peerSimilarityCount ={}
			data = line.split(' ')
			if len(data) < 3:
                                continue
			if "+" in data[0] or "+" in data[1] or "+" in data[2] or "+" in data[3]:
				#print("1**********************")
				continue
			if "x" in data[0] or "x" in data[2] or "x" in data[3]:
				continue
			if data[0]=="" or data[1]=="" or data[2]=="" or data[3]=="":
				continue
			if  not data[2].startswith("2019"):
				continue

			# print("block : "+data[1])
			# print("*************************")

			#if int(data[0]) < 8502514:
				#print("continue ",end='')
				#print(data[0])
			#	continue
			#else:
			#	blockSkipCount = blockSkipCount+1
			#if blockSkipCount>4:
				#print("break",end='')
				#print(data[0])
			#	break
			
			if int(data[0]) not in range(8502515, 8502535):
				continue
			if previousBlockNumber == data[0]:
                                continue

			previousBlockNumber = data[0]
			#print(line)
			utc_time = datetime.strptime(data[2]+" "+data[3][:-3], "%Y-%m-%d %H:%M:%S.%f")
			epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
			while(1):
				last_pos = txReceivedFp.tell()
				tx = txReceivedFp.readline()
				if tx == '':
					break
				#print("tx : "+tx)
				data1 = tx.split(' ')
				#print("tx : "+tx)
				#print("21**********************"+data1[0]+" "+data1[1]+" "+data1[2])
				
				if len(data1) < 7:
                                	continue
				#print("21**********************"+data1[0]+" "+data1[1]+" "+data1[2])
				if "+" in data1[0] or "+" in data1[1] or "+" in data1[2]:
        	                        #print("2**********************"+data1[0]+" "+data1[1]+" "+data1[2])
	                                continue
				if "x" in data1[1] or "x" in data1[2]:
					continue
				if data1[0]=="" or data1[1]=="" or data1[2]=="":
					continue
				if  not data1[1].startswith("2019"):
					continue
				#try:
				if len(data1[2].split('.')[1])>6:
					data1[2] = data1[2][:-3]
				utc_time1 = datetime.strptime(data1[1]+" "+data1[2], "%Y-%m-%d %H:%M:%S.%f")
				epoch_time1 = (utc_time1 - datetime(1970, 1, 1)).total_seconds()
				#print(data1[6])
				#print(data1[0],end='')
				#print(" ",end='')
				#if tx.split(" ")[1]<= data[2]:
				#print(epoch_time1, end='')
				#print(" ",end='')
				#print(epoch_time)
				if epoch_time1 <= epoch_time:
					#print("received transaction : "+tx.split(" ")[0])
					# if data[3] in peerTransListDict.keys():
						# peerTransListDict[data[3]] = []
					peerTransListDict[data1[6]].append(tx.split(" ")[0])
				else:
					txReceivedFp.seek(last_pos)
					break



			# print("content : ")
			# print(transactionList)
			#print(peerTransListDict.keys())
			blockPath = path+"/blocks/"+data[1]
			# print(blockPath)
			with open(blockPath) as fBlock:
				for tx in fBlock:
					#print("transaction : "+tx)
					transactionCount = transactionCount+1
					for peer in peerTransListDict.keys():
						if tx.rstrip() in peerTransListDict[peer]:
							# print(tx.rstrip())
							# print(tx1)
							# if tx.rstrip() == tx1:
							count = count + 1
							if peer not in peerSimilarityCount.keys():
								peerSimilarityCount[peer] = 0	
							peerSimilarityCount[peer] = peerSimilarityCount[peer]+1
			# print("*************************")
			
			for p, smlr in peerSimilarityCount.items():	
				#print(data[0]+" : "+data[1]+" : "+str(smlr)+" : "+str(transactionCount)+": "+p)
				#print(p[:-50],end='')
				#print(" : ",end='')
				if smlr !=0:
					#print(str(smlr/transactionCount*100)+"% skipped")
					peerSimilarityValues[p].append(smlr/transactionCount*100)
				else:
					print("0% skipped")
					peerSimilarityValues[p].append(0)
			
			#print("end**************************")
		for p, smlr in peerSimilarityValues.items():
			if len(smlr)>15:
				print(p, end='')
				print(" : ",end='')
				print(smlr)
if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])
