''' 
Note : Here you may have to rename the data folder accordingly 
This script calculates the fraction of blocks mined by miner 
in the main chain and expected number of block mined by 
a miner present in the main chain based on his mining power
ETH-NS-D-HET:
ETH-400-NoSkip-1x-Het
ETH-NS-D-HOMO:
ETH-40-NoSkip-1x-Homo
ETH-NS-ND-HET:
ETH-40-NoSkip-1x-Het  ETH-800-NoSkip-1x-Het
ETH-NS-ND-HOMO:
ETH-40-NoSkip-XX-Homo
ETH-S-ND:
ETH-120-Skip-1x  ETH-12-Skip-1x  ETH-240-Skip-1x
EVD-NS-D:
EVD800_1xDelay  EVD800_2xDelay  EVD800_4xDelay
EVD-NS-ND:
EVD-400-NoSkip-1x-Het  EVD-40-NoSkip-1x-Het  EVD-800-NoSkip-1x-Het
EVD-S-D:
EVD120_1xDelay_With_skip  EVD12_1xDelay_With_skip  EVD240_1xDelay_With_skip
'''

import time
import math
import numpy as np
import matplotlib.pyplot as plt
import os 
import sys
import subprocess as sp

filePath = '/home/nitin14/EVD-Segate/'

ethDir = [
	'ETH-NS-D-HET',
	'ETH-NS-D-HOMO',
	'ETH-NS-ND-HET',
	'ETH-NS-ND-HOMO',
	'ETH-S-ND'
]

evdDir = [
	'EVD-NS-D',
	'EVD-NS-ND',
	'EVD-S-D'
]
#computeFairness(inputFilePath, outputFile, 50, 1000, 0, False, 1)
blockFractList = []#np.zeros(10)

def computeFairness(inputFilePath, outputFile, startBlk, endBlk, exIndex, evd, delay,isWrite, similairty="95"):
	#print(evd)
	# 0xdb719d2e7cc1390e46f141a2e4978e9f49f16d63242c5d66f99aa33fef2e5300 15 282 400000000 396576869 0xbd611E337D54dfdbe9A052Fe689a7486cB59156c 664.650ms
	#blockFractList.clear()
	# Extracting address of the first node
	fileName = inputFilePath+'Mi/0.dat'
	firstMiner = ""
	if os.path.exists(fileName):
		file = open(fileName, "r")
		data = file.readlines()
		if evd:
			firstMiner = data[0].rstrip().split(' ')[8]
		else:
			firstMiner = data[0].split(' ')[5]

	# Blocks in the main chain of the first miner.
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

	# Compute the effective active hash power at every block.
	for j in range(1,48):
		fileName = inputFilePath+'Mc/'+str(j)+'.dat'
		if fileName == str("/home/nitin14/EVD-Scripts/statsData/EVD500M-2x/Mc/34.dat"):
			continue
		if os.path.exists(fileName):
			file =  open(fileName, "r")
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
					if blkHash == blockHashes[blkNum]:
						hashPowerAtBlock[blkNum] = hashPowerAtBlock[blkNum] + hashPowers[j]
		else:
			print("Error", fileName, "file not found")
			break

	exptBlkCount = 0.0
	for k in range(startBlk, endBlk):
		exptBlkCount = exptBlkCount + hashPowers[0]/hashPowerAtBlock[k]

		# if k%50 == 0:
		# 	print(hashPowerAtBlock[k], hashPowers[0]/hashPowerAtBlock[k])

	# 14,0x79068e34c77770f599afe5bf18f70326e7c4744b712a28d9ccba282eee91c65c,0xbd611E337D54dfdbe9A052Fe689a7486cB59156c,283,400000000,398949296
	# Compute the number of blocks mined by a miner in 
	miningFrac = {}
	fileName = inputFilePath+'Mc/0.dat'
	totalBlkCount =  0

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
				if miningFrac.get(miner):
					miningFrac[miner] = miningFrac[miner] + 1
				else:
					miningFrac[miner] = 1

	if not evd:
		exTimes = computeEthExecutionTime(inputFilePath, outputFile, startBlk, endBlk, exIndex)
	else:
		exTimes = computeEVDExecutionTime(inputFilePath, outputFile, startBlk, endBlk, exIndex)

	trueMiningPower = exptBlkCount/totalBlkCount
	exptBlkCount = (exptBlkCount*hashPowers[0])/trueMiningPower
	blocksMined = (miningFrac[firstMiner]/totalBlkCount)*hashPowers[0]/trueMiningPower



	print(inputFilePath)	
	# print(exptBlkCount, exptBlkCount/totalBlkCount, miningFrac[firstMiner], miningFrac[firstMiner]/totalBlkCount, totalBlkCount)
	print(exptBlkCount, exptBlkCount/totalBlkCount, miningFrac[firstMiner], blocksMined, totalBlkCount)
	print(exTimes)
	print()

	expFraction = exptBlkCount/totalBlkCount
	actFraction = (miningFrac[firstMiner]/totalBlkCount)*hashPowers[0]/trueMiningPower
	
	blockFractList.append(actFraction)

	avgAdvExtTime = exTimes[0][0]
	avgAdvProcTime = exTimes[0][1]
	if isWrite:
		if evd:
			avgHonestExTime = exTimes[2]
			avgHonestProcTime = exTimes[3]
			avgAdvExtTime = exTimes[0][0]
			avgAdvProcTime = exTimes[0][1]
			
			avgHonestPrevTime = exTimes[4]
			avgAdvPrevTime = exTimes[1]

			if exIndex == 1: # Adversary Skips processing
				outputFile.write(str(totalBlkCount)+","+str(delay)+","+str(avgHonestExTime)+","+str(avgHonestProcTime)+","+str(avgHonestPrevTime)+","+str(avgAdvExtTime)+","+str(avgAdvProcTime)+","+str(avgAdvPrevTime)+","+str(expFraction)+","+str( actFraction)+",")
			
			elif exIndex == 0:
				outputFile.write(str(totalBlkCount)+","+str(delay)+","+str(avgHonestExTime)+","+str(avgHonestProcTime)+","+str(avgHonestPrevTime)+","+str(expFraction)+","+str( actFraction)+",")
		else:
			avgHonestExTime = exTimes[1]
			avgHonestProcTime = exTimes[2]
			if exIndex == 1:
				outputFile.write(str(totalBlkCount)+","+str(delay)+","+str(avgHonestExTime)+","+str(avgHonestProcTime)+","+str(avgAdvExtTime)+","+str(avgAdvProcTime)+","+str(expFraction)+","+str( actFraction)+",")
			elif exIndex == 0:
				print(avgAdvExtTime,avgAdvExtTime)
				outputFile.write(str(totalBlkCount)+","+str(delay)+","+str(avgHonestExTime)+","+str(avgHonestProcTime)+","+str(expFraction)+","+str( actFraction)+",")
			print("*****************************")

def computeEthExecutionTime(inputFilePath, outputFile, startBlk, endBlk, exIndex):
	# 0x8414b5ad8f95e31473f5ab3372729317a07567edd2d9501ad8908105dda110bb 13 0 400000000 0 0x6F75AeB2465dAac2B630667efF18481BE2dEfabd false 0.21846 1.32698
	# Compute the average Execution time:
	avgExTime = {}
	
	globalBlks = 0.0
	globalExTime = 0.0
	globalProcTime = 0.0

	for j in range(0,48):
		fileName = inputFilePath+'Ex/'+str(j)+'.txt'
		if os.path.exists(fileName):
			file = open(fileName, "r")
			data = file.readlines()

			totalExTime = 0.0
			totalProcTime =  0.0
			totalBlks = 0
			for dataItem in data:
				info = dataItem.rstrip().split(' ')
				blkNum = int(info[1])
				if blkNum < startBlk:
					continue
				elif blkNum > endBlk:
					continue
				else:

					if j > exIndex:
						globalBlks = globalBlks + 1
						globalExTime = globalExTime + float(info[7])
						if "normal" in inputFilePath:
							if "Renoir-800M-2x-normal-noSkip" not in inputFilePath and "Renoir-800M-4x-normal-noSkip" not in inputFilePath and "Renoir-800M-4x-normal-Skip" not in inputFilePath and "Renoir-12M-1x-normal-noSkip" not in inputFilePath:
								globalProcTime = globalProcTime + float(info[9])
							else:
								globalProcTime = globalProcTime + float(info[8])	
						else:
							globalProcTime = globalProcTime + float(info[8])
					totalExTime = totalExTime + float(info[7])
					# print(inputFilePath)
					# if "Renoir-800M-2x-normal-noSkip" not in inputFilePath:
						# print("************************fuck")

					if "normal" in inputFilePath:
						# print(inputFilePath)
						if "Renoir-800M-2x-normal-noSkip" not in inputFilePath and "Renoir-800M-4x-normal-noSkip" not in inputFilePath and "Renoir-800M-4x-normal-Skip" not in inputFilePath and "Renoir-12M-1x-normal-noSkip" not in inputFilePath:
							totalProcTime = totalProcTime + float(info[9])
						else: 
							totalProcTime = totalProcTime + float(info[8])
					else:
						totalProcTime = totalProcTime + float(info[8])
					totalBlks = totalBlks + 1
			if totalBlks > 0:
				avgExTime[j] = [totalExTime/totalBlks, totalProcTime/totalBlks]
				# print(j, totalExTime/totalBlks, totalProcTime/totalBlks, totalBlks)
			else:
				avgExTime[j] = [0.0, 0.0]
				# print(j, 0.0, 0.0, totalBlks)

	# print(globalExTime/globalBlks)
	# print(globalProcTime/globalBlks)
	# print()
	return(avgExTime[0], globalExTime/globalBlks, globalProcTime/globalBlks)
	
def computeRenoirSkipSimilarity():
	dirPath = '/home/nitin14/EVD-Scripts/statsData/ETH'
	gasList = [50, 75, 95]
	fileNames =[
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-50-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-75-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-normal-Skip/'
	]
	# fileNames =[
	# 	'ETH-240-Skip-1x/'
	# ]

	lenFileNames = len(gasList)
	outputFilePath = '/media/user/WD_1TB/RenoirExperimentDataNew/data/RenoirSkipSimilarity.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,avgAdvExtTime,avgAdvProcTime,expFraction,actFraction,meanActFract,cfi,similairty\n")


	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95

		for j in range(0,10):
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 1, False, 1,False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 1, False, 1,True)
		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(confidenceInterVal)+",")

		if "normal" in inputFilePath:
			outputFile.write(computeSimilarity(inputFilePath)+"\n")
		else:
			outputFile.write(str(gasList[i])+"\n")	

		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()

def computeSimilarity(inputFilePath):
	# !/usr/bin/env python

	args = ["awk", r'{ sum += $9; n++ } END { if (n > 0) print sum / n *100; }', inputFilePath+"/Ex/0.txt"]
	p = sp.Popen(args, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE )
	return p.stdout.readline().strip().decode('utf-8') # will give you the first line of the awk output
	# print("dfasbjhcsbv : "+str(similairty))
	

def computeRenoirNoSkipSimilarity():
	dirPath = '/home/nitin14/EVD-Scripts/statsData/ETH'
	#dirPath = ''
	gasList = [50, 75, 95]
	fileNames =[
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-50-noSkip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-75-noSkip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-normal-noSkip/'
	]


	lenFileNames = len(gasList)
	outputFilePath = '/media/user/WD_1TB/RenoirExperimentDataNew/data/RenoirNoSkipSimilarity.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,expFraction,actFraction,meanActFract,cfi,similairty\n")

	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95
		for j in range(0,10):
			
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 0, False, 1,False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 0, False, 1,True)

		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(avgLateBlock)+","+str(confidenceInterVal)+",")
		if "normal" in inputFilePath:
			outputFile.write(computeSimilarity(inputFilePath)+"\n")
		else:
			outputFile.write(str(gasList[i])+"\n")	
		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()


def computeRenoirSkipDelay():
	dirPath = '/home/nitin14/EVD-Scripts/statsData/ETH'
	gasList = [1, 2, 4]
	fileNames =[
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-normal-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-2x-normal-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-4x-normal-Skip/'
	]
	# fileNames =[
	# 	'ETH-240-Skip-1x/'
	# ]

	lenFileNames = len(gasList)
	outputFilePath = '/media/user/WD_1TB/RenoirExperimentDataNew/data/RenoirSkipDelay.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,avgAdvExtTime,avgAdvProcTime,expFraction,actFraction,cfi\n")


	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95

		for j in range(0,10):
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 1, False, gasList[i],False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 1, False, gasList[i],True)
		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(confidenceInterVal)+"\n")

		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()

def computeRenoirNoSkipDelay():
	dirPath = '/home/nitin14/EVD-Scripts/statsData/ETH'
	gasList = [1, 2, 4]
	fileNames =[
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-normal-noSkip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-2x-normal-noSkip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-4x-normal-noSkip/'
	]
	# fileNames =[
	# 	'ETH-240-Skip-1x/'
	# ]

	lenFileNames = len(gasList)
	outputFilePath = '/media/user/WD_1TB/RenoirExperimentDataNew/data/RenoirNoSkipDelay.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,expFraction,actFraction,cfi\n")



	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95

		for j in range(0,10):
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 0, False, gasList[i],False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 0, False, gasList[i],True)
		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(confidenceInterVal)+"\n")

		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()

def computeRenoirSkip():
	dirPath = '/home/nitin14/EVD-Scripts/statsData/ETH'
	gasList = [1, 2, 4]
	fileNames =[
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-40M-1x-normal-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-400M-1x-normal-Skip/',
		'/media/user/WD_1TB/RenoirExperimentDataNew/Renoir-800M-1x-normal-Skip/'
	]
	# fileNames =[
	# 	'ETH-240-Skip-1x/'
	# ]

	lenFileNames = len(gasList)
	outputFilePath = '/media/user/WD_1TB/RenoirExperimentDataNew/data/RenoirSkip.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,avgAdvExtTime,avgAdvProcTime,expFraction,actFraction,cfi\n")


	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95

		for j in range(0,10):
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 1, False, 1,False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 1, False, 1,True)
		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(confidenceInterVal)+"\n")

		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()

def computeRenoirNoSkip(ethorReno=""):
	dirPath = os.environ["HOME"]+'/Ph.D./Project/RenoirProject/RenoirEthereumData/'
	gasList = [1, 2, 4]
	if ethorReno=="renoir":
		ration = [0.011,0.139,0.253]
	if ethorReno=="eth":
		ration = [0.011,0.122,0.205]

	if ethorReno=="renoir":
		fileNames =[
			dirPath+'Renoir-12M-1x-normal-noSkip/',
			dirPath+'Renoir-120M-1x-normal-noSkip/',
			dirPath+'Renoir-240M-1x-normal-noSkip/'
		]
	if ethorReno=="eth":
		fileNames =[
			dirPath+'ETH12M/',
			dirPath+'ETH120M/',
			dirPath+'ETH240M/'
		]
	# fileNames =[
	# 	'ETH-240-Skip-1x/'
	# ]

	lenFileNames = len(gasList)
	if ethorReno=="renoir":
		outputFilePath = dirPath+'../RenoirExperiment/data/RenoirNoSkip.csv'
	if ethorReno=="eth":
		outputFilePath = dirPath+'../RenoirExperiment/data/ethNoSkip.csv'
	outputFile = open(outputFilePath,"w+")
	outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,expFraction,actFraction,cfi\n")


	for i in range(0,lenFileNames):
		inputFilePath =  fileNames[i]
		startBlk = 50
		endBlk = startBlk+95

		for j in range(0,10):
			computeFairness(inputFilePath, outputFile, startBlk, endBlk, 0, False, ration[i],False)
			startBlk = endBlk+1
			endBlk = startBlk+95

		avgLateBlock = np.mean(blockFractList)
		stdDev = np.std(blockFractList)
		confidenceInterVal = 1.984*stdDev/math.sqrt(10)

		computeFairness(inputFilePath, outputFile, 50, 1000, 0, False, ration[i],True)
		print(avgLateBlock, stdDev, confidenceInterVal)
		outputFile.write(str(confidenceInterVal)+"\n")

		print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")	
		blockFractList.clear()






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


hashPowers = readHashPower('/media/user/WD_1TB/RenoirExperiment/hashPower')
hashPowers = [x/sum(hashPowers) for x in hashPowers]


# dirPath = '/home/nitin14/EVD-Segate/ETH-S-D-15/'
# gasList = [12, 120, 240]
# fileNames =[
# 	'ETH-240-Skip-1x/'
# ]
# # fileNames =[
# # 	'ETH-240-Skip-1x/'
# # ]

# lenFileNames = len(fileNames)
# outputFilePath = '/home/nitin14/EVD-Expt/data/ethSkip1.csv'
# outputFile = open(outputFilePath,"w+")
# outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,avgAdvExtTime,avgAdvProcTime,expFraction,actFraction\n")


# for i in range(0,lenFileNames):
# 	inputFilePath =  dirPath+fileNames[i]
# 	computeFairness(inputFilePath, outputFile, 50, 1000, 1, False, 1)


# dirPath = '/home/nitin14/EVD-Segate/ETH-NS-D-15/'
# gasList = [12, 120, 240]
# fileNames =[
# 	'ETH-800-NoSkip-1x-15/'
# ]
# # fileNames =[
# # 	'ETH-240-Skip-1x/'
# # ]

# lenFileNames = len(fileNames)
# outputFilePath = '/home/nitin14/EVD-Expt/data/ethSkip1.csv'
# outputFile = open(outputFilePath,"w+")
# outputFile.write("totalBlocks,delay,avgHonestExTime,avgHonestProcTime,avgAdvExtTime,avgAdvProcTime,expFraction,actFraction\n")


# for i in range(0,lenFileNames):
# 	inputFilePath =  dirPath+fileNames[i]
# 	computeFairness(inputFilePath, outputFile, 50, 1000, 0, False, 1)

# computeRenoirNoSkipSimilarity()
# computeRenoirSkipSimilarity()
# computeRenoirNoSkipDelay()
# computeRenoirSkipDelay()
computeRenoirNoSkip("eth")
computeRenoirNoSkip("renoir")
# computeRenoirSkip()
