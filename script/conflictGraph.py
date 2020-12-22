#!/usr/bin/python

import sys

transactionList = []

def main(path):
	print(path)
	filename = path+"/blockInfo"  
	txPath = path+"/transactionInfo"
	txReceivedFp = open(txPath, "r")
	# print("path*****"+txPath)
	with open(filename) as f:
		for line in f:
			# print(line)
			count = 0
			transactionCount = 0
			data = line.split(' ')
			# print("block : "+data[1])
			# print("*************************")
			
			while(1):
				last_pos = txReceivedFp.tell()
				tx = txReceivedFp.readline()
				if tx == '':
					break
				# print("tx**"+tx+"::::"+data[2])
				if tx.split(" ")[1]<= data[2]:
					# print("received transaction : "+tx.split(" ")[0])
					transactionList.append(tx.split(" ")[0])
				else:
					txReceivedFp.seek(last_pos)
					break



			# print("content : ")
			# print(transactionList)
			blockPath = path+"/blocks/"+data[1]
			# print(blockPath)
			with open(blockPath) as fBlock:
				for tx in fBlock:
					# print("transaction : "+tx)
					transactionCount = transactionCount+1
					if tx.rstrip() in transactionList:
						# print(tx.rstrip())
						# print(tx1)
						# if tx.rstrip() == tx1:
						count = count + 1
			# print("*************************")
			print(data[1]+" : "+str(count)+" : "+str(transactionCount))
			if transactionCount !=0:
				print(str(count/transactionCount*100)+"% skipped")
			else:
				print("0% skipped")
			
if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])