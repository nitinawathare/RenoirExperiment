import os.path
import os
from pathlib import Path


def main():

	p = 20
	adjList = []
	blockfile = "/home/shashi/RenoirExperiment/gitRepoRenoir/Block1/"
	for block in os.listdir(blockfile):	
		blockInfo = []
		# Reading block one by one.....
		file = '/home/shashi/RenoirExperiment/gitRepoRenoir/Block1/'+block
		blockRead = []
		blockWrite = []

		if Path(file).exists():
			with open(file) as f:
				# Reading trx. one by one in block.....
				for txnum, tl in enumerate(f):
					tl = tl.rstrip('\n')
					rwfile = str( '/home/shashi/RenoirExperiment/gitRepoRenoir/transactionsRW/'+str(block)+'_'+str(tl) )
					trRead = []
					trWrite = []
					
					if  Path(rwfile).exists():
						with open(rwfile) as rw:
							for data in rw:
								mystring = data.split("_")
								value = mystring[2].rstrip('\n')
								if mystring[0] == "RD":
									
									trRead.append((mystring[1], value))
								else:
									trWrite.append((mystring[1], value))
						check = 0
						
						# checking for readset present in writeset of previously executed transaction.............
						# checking readset of Tx(N) in executed transactions Tx(1.....N-1) in reverse manner , if readset present in writeset of Tx(1...N-1) then Tx(N) is dependent on TX(M).
						for i, e in reversed(list(enumerate(blockWrite))):
							for j in trRead:
								if j in e:
									blockInfo.append((txnum, i))
									check = 1
									break

							if check == 1:
								break
						if check == 0:
							blockInfo.append((txnum, "_" ))
					else:
						blockInfo.append((txnum,"file not exist"))		
					blockWrite.append(trWrite)
			a=blockInfo[:]	
			adjList.append(a)
			blockInfo.clear()
		
		p = p+1
		# print("block done..........................")
		if(p == 40):
			break
	for s in adjList:
		print(s) 



if __name__ == "__main__":
    main()
