import pandas as pd
import numpy as np
from pathlib import Path
from collections import defaultdict

def main():
    # File to read block information, time and peers
	prev="0x00000"
	file = pd.read_csv("testData/blocks/data.csv",sep=',', header=None)
	filedata = file.iloc[1:, :].values
	arr = defaultdict(int)
	peerList = ["0x623063b05b70da4cad6c153516dd9b7aebec42b503a7505ab4305cbea2d8f8d48029aaf65ca534a78c619a4105cd07201b7d75bd2f12dfce90bf7a1fc2840d1b","0x4faf867a2e5e740f9b874e7c7355afee58a2d1ace79f7b692f1d553a1134eddbeb5f9210dd14dc1b774a46fd5f063a8bc1fa90579e13d9d18d1f59bac4a4b16b", "0x95fdbe6b389bdc40eac8b56b39e28937723688e6c55d527b8aadd0e10d3a5d347724c99f780cd805d17fd7142210fc41e9a964079a3fd7040c360d08133ba366", "0x4afb3a9137a88267c02651052cf6fb217931b8c78ee058bb86643542a4e2e0a8d24d47d871654e1b78a276c363f3c1bc89254a973b00adc359c9e9a48f140686"]
	for i in range(800, 850):
		blockhash = str(filedata[i][2])
		# print(blockhash)
		if prev==blockhash:
		    continue
		else:
		    print(blockhash)
		    prev = blockhash
		
		j = Path("testData/blockdata/" + "\""+blockhash+"\"" + ".csv")

		if j.is_file():
			block = pd.read_csv(j, sep=',', header=None)
			block = block.iloc[:,0].values.T
		else:
			continue

		transCount=np.zeros(len(block))

		# p = filedata[i]
		# for peer in range(4, len(p)):
		# 	if str(p[peer]) != 'nan':
		# 		# print(p[peer])
		# 		if p[peer] in arr:
		# 			arr[p[peer]] = arr[p[peer]] +1
		# 		else:
		# 			arr[p[peer]] = 1

		for peer in peerList:
			if str(peer) != 'nan':
			# Taking individual peer transactions list
				trxPath = Path("testData/transactions/" + "\"" + str(peer)+"\"" + ".csv")
				if trxPath.is_file():
					trx = pd.read_csv(trxPath,sep=',',header=None)
					trx1 = trx.iloc[:,0].values.T
					for t in range(len(block)):
						if block[t] in trx1:
							transCount[t] += 1
				

		print(transCount)							
	# for key in arr:
	# 	if arr[key] >= 9600:
	# 		print(str(key)+" : "+str(arr[key]))

if __name__ == "__main__":
	main()

