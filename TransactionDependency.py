import os.path
import os
from pathlib import Path


def main():

	p = 40
	adjList = []
	blockfile = "/home/shashi/RenoirExperiment/gitRepoRenoir/Block1/"
	# with open(blockfile) as bf:
	for block in os.listdir(blockfile):
		# for block in bf and i in range(10):
		
		blockInfo = []
		# Reading block one by one.....
		file = '/home/shashi/RenoirExperiment/gitRepoRenoir/Block1/'+block
		# print(file)
		blockRead = []
		blockWrite = []

		if Path(file).exists():
			with open(file) as f:
				for txnum, tl in enumerate(f):
					tl = tl.rstrip('\n')
					# txrw = block+"_"
					# print(txrw)
					rwfile = str( '/home/shashi/RenoirExperiment/gitRepoRenoir/transactionsRW/'+str(block)+'_'+str(tl) )
					# print(rwfile)
					trRead = []
					trWrite = []
					
					if not Path(rwfile).exists():
						print("file not exists")
					else:
						# print("file not exists")


						with open(rwfile) as rw:
							for data in rw:
								mystring = data.split("_")
								value = mystring[2].rstrip('\n')
								if mystring[0] == "RD":
									
									trRead.append((mystring[1], value))
								else:
									trWrite.append((mystring[1], value))
						# for j in trRead:
						# 	print(j)
						# for k in trWrite:
						# 	print(k)


						check = 0
						for i, e in reversed(list(enumerate(blockWrite))):
							for j in trRead:
							# 	print(j)
								if j in e:
									blockInfo.append((txnum, i))
									check = 1
									break

							if check == 1:
								break
						if check == 0:
							blockInfo.append((txnum, "_" ))
					blockWrite.append(trWrite)
			# for j in blockWrit:
			# 	print(j)
			# 	print("\n")		
			adjList.append(blockInfo)
			blockInfo.clear()
			
		else:
			continue
		p = p+1
		print("block done..........................")
		if(p == 50):
			break
	for s in adjList:
		print(*s) 





				

if __name__ == "__main__":
    main()
