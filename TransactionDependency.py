
import os
from pathlib import Path


def main():

	p = 1
	adjList = []
	blockfile = "/home/shashi/RenoirExperiment/gitRepoRenoir/blocks/"
	# with open(blockfile) as bf:
	for block in os.listdir(blockfile):
		# for block in bf and i in range(10):
		
		blockInfo = []
		file = Path("/home/shashi/RenoirExperiment/gitRepoRenoir/blocks/"+block)
		# print(file)
		blockRead = []
		blockWrite = []
		if file.is_file():
			
			with open(file) as f:
				for txnum, tl in enumerate(f):
					txrw = block+"_"
					# print(txrw)
					rwfile = Path("/home/shashi/RenoirExperiment/gitRepoRenoir/transactionsRW/" + block+"_"+tl)
					print(rwfile)
					trRead = []
					trWrite = []
					if rwfile.is_file():
						with open(rwfile) as rw:
							for data in rw:
								mystring = data.split("_")
								if mystring[0] == "RD":
									trRead.append((mystring[1], mystring[2]))
								else:
									trWrite.append((mystring[1], mystring[2]))

						check = 0
						for i, e in reversed(list(enumerate(blockWrite))):
							for j in trRead:
								if j in i:
									blockInfo.append((txnum, i))
									check = 1
									break

							if check == 1:
								break
						if check == 0:
							blockInfo.append((txnum, "_" ))
					# else:
					# 	continue
			adjList.append(blockInfo)
			blockInfo.clear()
			
		# else:
		# 	continue
		p = p+1
		if(p == 10):
			break
	for s in adjList:
		print(*s) 





				

if __name__ == "__main__":
    main()
