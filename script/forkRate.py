'''
'''

import math
import time
import numpy as np
import matplotlib.pyplot as plt
import os 
import sys
from collections import defaultdict
import datetime

skipFailDict = {
	1:[26,36,23,27,39],
	2:[48,36,27,32,46],
	4:[48,26,28,36,23,32]
}
skipFailAll = [23,26,27,28,32,36,39,48]

noSkipFailDict = {
	1:[16,48,32],
	2:[24,32,36,39,46,48],
	4:[24,28,46]
}
noSkipAll = [16,24,28,32,36,39,46,48]


# Compute the address of the first miner
def firstMinerAddress(inputFilePath, evd = True):
	fileName = inputFilePath+'Mi/0.dat'
	firstMiner = ""
	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()
		if evd:
			firstMiner = data[0].rstrip().split(' ')[8]
		else:
			firstMiner = data[0].split(' ')[5]
	return firstMiner

def computeFirstHashPower(inputFilePath, startBlk, endBlk):
	hashPowerAtBlock = {}
	blockHashes = {}
	fileName = inputFilePath+'Mc/0.dat'
	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()

		for dataItem in data:
			info = dataItem.split(',')
			blkNum = int(info[0])
			if blkNum < startBlk:
				continue
			elif blkNum > endBlk:
				break
			else:
				blkHash = info[1]
				blockHashes[blkNum] = blkHash
				hashPowerAtBlock[blkNum] = hashPowers[0]
	else:
		print("Error", fileName, "file not found")
	return hashPowerAtBlock

def mainChainHashes(inputFilePath, startBlk, endBlk):
	blockHashes = {}
	fileName = inputFilePath+'Mc/0.dat'
	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()

		for dataItem in data:
			info = dataItem.split(',')
			blkNum = int(info[0])
			if blkNum < startBlk:
				continue
			elif blkNum > endBlk:
				break
			else:
				blkHash = info[1]
				blockHashes[blkNum] = blkHash
	else:
		print("Error", fileName, "file not found")
	return blockHashes

def computeNumMinedBlocks(inputFilePath, startBlk, endBlk):
	minedBlocks = {}
	fileName = inputFilePath+'Mc/0.dat'
	global totalBlkCount

	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()

		for dataItem in data:
			info = dataItem.split(',')
			blkNum = int(info[0])
			if blkNum < startBlk:
				continue
			elif blkNum > endBlk:
				break
			else:
				totalBlkCount= totalBlkCount + 1
				miner = info[2]
				if minedBlocks.get(miner):
					minedBlocks[miner] = minedBlocks[miner] + 1
				else:
					minedBlocks[miner] = 1
	else:
		print("Error", fileName, "file not found")
	return minedBlocks

# Evd files
# 0xfc125a8af0a01e0e18c34816ce0b6fcf208c762861df1bca9d463662abd8c452 601 166 3500000 3486000 500000000 485867636 485701636 0xbd611E337D54dfdbe9A052Fe689a7486cB59156c

# Eth files
# 0x42c195850143eb25243719fae3a2eb2df1de093520e27bdd7097c64494d3b4e2 456 67 12000000 4707183 0xbd611E337D54dfdbe9A052Fe689a7486cB59156c 1.124s

def computeForkRate(inputFilePath, outputFile, startBlk, endBlk, strategy, delay, evd=True):
	global totalMinedBlocks, chunkMinedBlocks
	minedBlocks = computeNumMinedBlocks(inputFilePath, startBlk, endBlk)
	blockHashes = mainChainHashes(inputFilePath, startBlk, endBlk)
	mainChainRatio = {}

	chunkMinedBlocks = 0
	for i in range(0,47):
		mainChainRatio[i] = 0.0
		# if i in noSkipFailDict[delay]:
		# 	continue

		fileName = inputFilePath+"Mi/"+str(i)+".dat"
		minerBlocks = 0

		if os.path.exists(fileName):
			file = open(fileName, "r")
			data = file.readlines()
			if len(data) == 0:
				# print(fileName, " no data found!!")
				continue
			# print(fileName)
			minerId = ""
			if evd:
				minerId = data[0].rstrip().split(' ')[8]
			else:
				minerId = data[0].rstrip().split(' ')[5]

			# print(i,":", end=" ")
			numForkedBlocks = 0 	
			for dataItem in data:
				info = dataItem.split(' ')
				blkNum = int(info[1])
				blockHash = info[0]
				if blkNum < startBlk:
					continue
				elif blkNum > endBlk:
					break
				else:
					totalMinedBlocks = totalMinedBlocks + 1
					chunkMinedBlocks = chunkMinedBlocks + 1
					minerBlocks = minerBlocks + 1
					if blockHashes[blkNum] != blockHash:
						numForkedBlocks = numForkedBlocks + 1
						# print(blkNum, end=" ")
			if minerId in minedBlocks.keys():
				# print(i, minerBlocks, minedBlocks[minerId])
				if minerBlocks != 0:
					mainChainRatio[i] = minedBlocks[minerId]/minerBlocks

					# print(str(i)+" : "+str(minedBlocks[minerId])+" : "+str(minerBlocks)+" : "+str(minedBlocks[minerId]/minerBlocks)+" : "+str(minedBlocks[minerId]/951)+" : "+str(hashPowers[i])+" : "+str(minerBlocks/1383))
			# if i <= 2:
			# 	print("(",i,minerBlocks,")", end=" ")

		else:
			print("Error", fileName, "file not found")
		# if minerBlocks != 0:
		# 	print("\n",numForkedBlocks, minerBlocks, 1-numForkedBlocks/minerBlocks,"\n\n")
	# print()
	# print(delay, totalMinedBlocks)
	return mainChainRatio
	
def forkRateDelay(strategy="", numChunk=1):
	global totalMinedBlocks, chunkMinedBlocks

	dirPath = '/home/sourav/EVD-Segate1/EVD500M-'	
	delays = [1, 4, 2]
	gasUsage = 500
	chunkResults = {}
	outputFilePath = os.environ["HOME"]+"/EVD/writeup-EVD/data/evd-minefrac-delay"+str(strategy)+".csv"

	outputFile = open(outputFilePath,"w+")
	outputFile.write("delay,gasUsage,totalMainChain,totalMined,forkRate,cfiFork,frac1,cfi1,frac2,cfi2,frac3,cfi3\n")

	totalBlocks = 950
	for delay in delays:

		if delay == 2 and strategy=='':
			dirPath = '/home/sourav/EVD-Segate1/EVD-Short/EVD500M-'
			numChunk = 2
			totalBlocks = 150

		totalMinedBlocks = 0
		chunkResults[delay] = {}
		chunkResults[delay][0] = []
		chunkResults[delay][1] = []
		chunkResults[delay][2] = []

		forkRates = []
		meanFrac = {}
		cfiFrac = {}

		inputFilePath =  dirPath+str(delay)+"x"+str(strategy)+"/"
		
		startBlk = 50
		endBlk = startBlk+totalBlocks/numChunk
		for j in range(0,numChunk):
			mainChainRatio = computeForkRate(inputFilePath, outputFile, startBlk, endBlk, strategy, delay)
			# print(strategy, delay, mainChainRatio,"\n")
			startBlk = endBlk+1
			chunkSize = totalBlocks/numChunk
			endBlk = startBlk+chunkSize

			print(delay, chunkMinedBlocks)
			forkRates.append(100*chunkSize/chunkMinedBlocks)
			for k in range(0,3):
				chunkResults[delay][k].append(100*mainChainRatio[k])
		


		meanForkRate = np.mean(forkRates)
		stdDevForkRate = np.std(forkRates)
		cfiForkRate = 1.984*stdDevForkRate/math.sqrt(10)

		for j in range(0,3):
			meanFrac[j] = np.mean(chunkResults[delay][j])
			stdDev = np.std(chunkResults[delay][j])
			cfiFrac[j] = 2.262*stdDev/math.sqrt(10)

		outputFile.write(str(delay*1.0)+","+str(gasUsage)+","+str(totalBlocks)+","+str(totalMinedBlocks)+","+str(meanForkRate)+","+str(cfiForkRate))
		for j in range(0,3):
			outputFile.write(","+str(meanFrac[j])+","+str(cfiFrac[j]))
		outputFile.write("\n")
		# avgLateBlock = np.mean(blockFractList)
		# stdDev = np.std(blockFractList)
		# confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		# print(avgLateBlock, stdDev, confidenceInterVal)
		# outputFile.write(str(confidenceInterVal)+"\n")
		# print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	

def computeGasUsedBlocks(strategy="",ethorReno=""):
	# print("inside method**")
	minedBlocks = {}
	# fileName = inputFilePath+'Mc/0.dat'
	global totalBlkCount
	gasUsages = [12,120,240]
	if ethorReno=="eth":
		ration = [0.011,0.122,0.205]
	if ethorReno=="renoir":
		ration = [0.011,0.139,0.253]
	# gasUsages = [12,120,240]
	# gasUsages=[40]
	dirPath = os.environ["HOME"]+'/Ph.D./Project/RenoirProject/RenoirEthereumData/'	
	sumTx = 0
	throughputList = []
	if ethorReno=="eth":
		outputFilePath = os.environ["HOME"]+"/Ph.D./Project/RenoirProject/RenoirExperiment/data/eth-throughput"+str(strategy)+".csv"
	if ethorReno=="renoir":
		outputFilePath = os.environ["HOME"]+"/Ph.D./Project/RenoirProject/RenoirExperiment/data/renoir-throughput"+str(strategy)+".csv"
	outputFile = open(outputFilePath,"w")
	outputFile.write("ratio,totalTx,TotalTime,throughputoverall,throughput,cfi\n")
	index = 0
	for gasUsage in gasUsages:
		print("************************************")
		sumTx = 0
		throughputList = []
		if ethorReno=="renoir":
			inputFilePath = dirPath+"Renoir-"+str(gasUsage)+"M"+str(strategy)+"-1x-"+"normal-"+"noSkip"+"/"
		if ethorReno=="eth":
			inputFilePath =  dirPath+"ETH"+str(gasUsage)+"M"+str(strategy)+"/"

		fileName = inputFilePath+'Mc/0.dat'
		if os.path.exists(fileName):
			file = open(fileName, "r")
			data = file.readlines()
		
		for dataItem in data:
				info = dataItem.split(',')
				# print(info[5].rstrip())i
				sumTx = sumTx + int(info[3])

		# print(sumTx)
		minTimeStamp = 0
		maxTimeStamp = 0
		# for i in range(0,47):
		fileName = inputFilePath+'Ti/'+str(0)+'.txt'
		# print(fileName)
		if os.path.exists(fileName):
			file = open(fileName, "r")
			data = file.readlines()
		for dataItem in data:
			info = dataItem.split(',')
			if len(info)>1:
				date_time_str = info[1].rstrip()
				# print(date_time_str)	
				date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
				timestm = datetime.datetime.timestamp(date_time_obj)
				# print(timestm)
				if minTimeStamp == 0 and maxTimeStamp == 0:
					minTimeStamp = timestm
					maxTimeStamp = timestm
					# print("inside")
				if minTimeStamp > timestm:
					minTimeStamp = timestm
				if maxTimeStamp < timestm:
					maxTimeStamp = timestm
# **************************************************************************
		fileName = inputFilePath+'Ti/'+str(0)+'.txt'
		if os.path.exists(fileName):
			file = open(fileName, "r")
			data = file.readlines()				
		lineCount = 0
		sumTx = 0
		totalTx = 0
		startTimestamp = ""
		for dataItem in data:
			info = dataItem.split(',')

			if len(info)>1:
				if int(info[0]) < 40:
					continue
				# if int(info[0]) > 40 and startTimestamp =="":
				# 	startTimestamp = info[1]
				if startTimestamp == "":
					# startTimestamp = info[1]
					date_time_str = info[1].rstrip()
					# print(date_time_str)	
					date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
					startTimestamp = datetime.datetime.timestamp(date_time_obj)
					startBlock = info[0]
				if lineCount == 50:
					lineCount = 0
					# endTimeStamp = info[1]
					date_time_str = info[1].rstrip()
					# print(date_time_str)	
					date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
					endTimeStamp = datetime.datetime.timestamp(date_time_obj)

					# print(startBlock+"***"+info[0]+"***"+str(startTimestamp).rstrip()+"***"+str(endTimeStamp))
					sumTx = 0
					fileNameBlock = inputFilePath+'Mc/0.dat'
					if os.path.exists(fileNameBlock):
						file = open(fileNameBlock, "r")
						dataBlock = file.readlines()
						for dataItemBlock in dataBlock:
							infoBlock = dataItemBlock.split(',')
							# print(info[5].rstrip())i
							if int(infoBlock[0]) > int(startBlock) and int(infoBlock[0] < info[0]) :
								sumTx = sumTx + int(infoBlock[3])
								totalTx = totalTx+int(infoBlock[3])
					# print(sumTx/(endTimeStamp - startTimestamp))
					if ethorReno=="renoir":
						if sumTx/(endTimeStamp - startTimestamp) > 10:
							throughputList.append(sumTx/(endTimeStamp - startTimestamp))
					else:
						throughputList.append(sumTx/(endTimeStamp - startTimestamp))

					startTimestamp = ""
				else:
					lineCount = lineCount+1
				# 	lineCount = 0
				# 	sumTx = 0
				# 	fileNameBlock = inputFilePath+'Mc/0.dat'
				# 	if os.path.exists(fileNameBlock):
				# 		file = open(fileNameBlock, "r")
				# 		dataBlock = file.readlines()
					
				# 	for dataItemBlock in dataBlock:
				# 			info = dataItemBlock.split(',')
				# 			# print(info[5].rstrip())i
				# 			sumTx = sumTx + int(info[3])
				# 			if 
		# print(throughputList)
		meanthroughput = np.mean(throughputList)
		stdthroughput = np.std(throughputList)
		cfithroughput = 2.262*stdthroughput/math.sqrt(len(throughputList)+1)		
		print(str(meanthroughput*3600)+":"+str(cfithroughput))
# **************************************************************************
		# print(maxTimeStamp-minTimeStamp)
		# print(throughputList)
		# print(totalTx/(maxTimeStamp-minTimeStamp))
		outputFile.write(str(ration[index])+","+str(sumTx)+","+str(maxTimeStamp-minTimeStamp)+","+str(sumTx/(maxTimeStamp-minTimeStamp)*3600)+","+str(meanthroughput*3600)+","+str(cfithroughput)+"\n")
		index = index + 1
		# print("************************************")

def forkRateGas(strategy="", numChunk=1, evd=True, ethorReno=""):
	global totalMinedBlocks, chunkMinedBlocks, totalBlkCount
	delay = 1
	gasUsages = [12,120,240]
	similarity = ["normal","75","50"]
	# gasUsages = [40,400,800]
	# gasUsages = [40]
	if ethorReno=="eth":
		tauRatio = [0.011,0.122,0.205]
	elif ethorReno=="renoir":
		tauRatio = [0.011,0.139,0.253]
	else:
		tauRatio = [93,75,50]

	indexCount = 0
	# gasUsages = [1,2,4]

	# gasUsages = ["normal",75,50]

	chunkResults = {}

	dirPath = ""
	outputFilePath = ""
	if evd:
		dirPath = '/home/sourav/EVD-Segate1/EVD'	
		outputFilePath = os.environ["HOME"]+"/EVD/writeup-EVD/data/evd-minefrac"+str(strategy)+".csv"
	else:	
		dirPath = os.environ["HOME"]+'/Ph.D./Project/RenoirProject/RenoirEthereumData/'	
		outputFilePath = os.environ["HOME"]+"/Ph.D./Project/RenoirProject/RenoirExperiment/data/"+str(ethorReno)+"-minefrac"+str(strategy)+".csv"
	outputFile = open(outputFilePath,"w+")
	outputFile.write("delay,gasUsage,totalMainChain,totalMined,forkRate,cfiFork,frac1,cfi1,frac2,cfi2,frac3,cfi3,frac4,cfi4,frac5,cfi5,frac6,cfi6,frac7,cfi7,frac8,cfi8,frac9,cfi9\n")

	totalBlocks = 950
	for gasUsage in gasUsages:
		totalMinedBlocks = 0
		totalBlkCount = 0
		chunkResults[gasUsage] = {}
		
		for index in range(0,49):
			chunkResults[gasUsage][index] = []

		forkRates = []
		meanFrac = {}
		cfiFrac = {}

		if ethorReno=="eth":
			inputFilePath =  dirPath+"ETH"+str(gasUsage)+"M"+"/"
		elif ethorReno=="renoir":
			inputFilePath =  dirPath+"Renoir-"+str(gasUsage)+"M"+"-1x-"+"normal-"+"noSkip"+"/"
		else:
			inputFilePath =  dirPath+"Renoir-"+str(240)+"M"+"-1x-"+str(similarity[indexCount])+"-"+"noSkip"+"/"

		# inputFilePath =  dirPath+"Renoir-"+str(800)+"M"+str(strategy)+"-"+str(gasUsage)+"x-"+"normal-"+"noSkip"+"/"


		print(inputFilePath)
		startBlk = 50
		chunkSize = totalBlocks/numChunk
		endBlk = startBlk+chunkSize
		for j in range(0,numChunk):
			mainChainRatio = computeForkRate(inputFilePath, outputFile, startBlk, endBlk, strategy, delay, evd)
			# print(strategy, delay, mainChainRatio,"\n")
			startBlk = endBlk+1
			endBlk = startBlk+totalBlocks/numChunk

			forkRates.append(100*chunkSize/chunkMinedBlocks)
			for k in range(0,47):
				chunkResults[gasUsage][k].append(100*mainChainRatio[k])
		
		meanForkRate = np.mean(forkRates)
		stdDevForkRate = np.std(forkRates)
		cfiForkRate = 2.262*stdDevForkRate/math.sqrt(10)

		for j in range(0,47):
			meanFrac[j] = np.mean(chunkResults[gasUsage][j])
			stdDev = np.std(chunkResults[gasUsage][j])
			cfiFrac[j] = 2.262*stdDev/math.sqrt(10)
			# print(chunkResults[gasUsage][j])

		# print(meanFrac)
		sumFract = 0
		for j in range(0,47):
			sumFract = sumFract + meanFrac[j]*hashPowers[j]
		print(sumFract)
		print("***************************************")
		outputFile.write(str(delay)+","+str(tauRatio[indexCount])+","+str(totalBlocks)+","+str(totalMinedBlocks)+","+str(meanForkRate)+","+str(cfiForkRate))
		# for j in range(0,9):
		outputFile.write(","+str(meanFrac[0])+","+str(cfiFrac[0]))
		outputFile.write(","+str(meanFrac[1])+","+str(cfiFrac[1]))
		outputFile.write(","+str(meanFrac[2])+","+str(cfiFrac[2]))
		outputFile.write(","+str(meanFrac[3])+","+str(cfiFrac[3]))
		outputFile.write(","+str(meanFrac[4])+","+str(cfiFrac[4]))
		outputFile.write(","+str(meanFrac[5])+","+str(cfiFrac[5]))
		outputFile.write(","+str(meanFrac[6])+","+str(cfiFrac[6]))
		outputFile.write(","+str(meanFrac[7])+","+str(cfiFrac[7]))
		outputFile.write(","+str(meanFrac[8])+","+str(cfiFrac[8]))
		# outputFile.write(","+str(meanFrac[9])+","+str(cfiFrac[9]))

		outputFile.write(","+str(totalBlkCount)+","+str(totalBlkCount/totalMinedBlocks))
		outputFile.write("\n")
		# print(gasUsage, meanFrac, cfiFrac)
		indexCount = indexCount +1

# forkRateDelay("-skip")
totalMinedBlocks = 0
chunkMinedBlocks = 0
totalBlkCount = 0

def readHashPower(fileName):
	hashPowers = []
	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()

		for dataItem in data:
			hashPower = float(dataItem.rstrip())
			hashPowers.append(hashPower)
	else:
		print("Error! File ",fileName," not found")

	return hashPowers


hashPowers = readHashPower(os.environ["HOME"]+'/Ph.D./Project/RenoirProject/RenoirExperiment/hashPower')
hashPowers = [x/sum(hashPowers) for x in hashPowers]


if len(sys.argv) <3:
	print("[eth], numChunk")
	exit()
numChunk = int(sys.argv[2])
if sys.argv[1] == 'eth':
	
	# forkRateGas("-renoir", numChunk, False,"renoir")
	# forkRateGas("-renoir", numChunk, False,"eth")
	# forkRateGas("-renoir", numChunk, False,"similarity")
	computeGasUsedBlocks("","eth")
	computeGasUsedBlocks("","renoir")
