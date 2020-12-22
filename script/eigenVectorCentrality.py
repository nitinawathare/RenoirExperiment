import networkx as nx
import os

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

hashPowers = readHashPower('/home/user/RenoirExperiment/hashPower')
hashPowers = [x/sum(hashPowers) for x in hashPowers]


G=nx.Graph()
adjacencyListy = [(0, 38), (0, 9), (0, 12), (0, 13), (0, 22), (0, 30), (1, 34), (1, 44), (1, 29), (2, 16), (2, 43), (2, 47), (3, 31), (4, 17), (4, 20), (5, 18), (5, 21), (6, 14), (7, 40), (7, 10), (7, 14), (8, 33), (9, 30), (10, 34), (10, 37), (10, 17), (10, 21), (10, 25), (10, 30), (11, 17), (11, 43), (11, 28), (11, 30), (12, 17), (14, 36), (14, 39), (14, 17), (14, 21), (14, 27), (14, 30), (15, 18), (17, 32), (17, 43), (17, 40), (17, 44), (17, 18), (17, 20), (17, 21), (17, 46), (17, 30), (17, 31), (18, 41), (19, 26), (19, 30), (20, 30), (21, 38), (21, 39), (21, 44), (21, 23), (21, 25), (21, 42), (21, 30), (22, 45), (22, 30), (24, 30), (25, 40), (25, 27), (30, 35), (30, 37), (30, 40), (30, 44), (30, 43), (30, 47), (31, 45), (31, 41), (33, 45), (34, 44), (35, 47), (37, 40), (40, 44), (42, 48), (43, 44)]
for (a,b) in adjacencyListy:
	# print(a)
	G.add_edge(a,b,weight=hashPowers[b])

# print(G.nodes())
centrality = nx.eigenvector_centrality_numpy(G,weight='weight')
# print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
for node in centrality:
	print('%s %0.6f'%(node,centrality[node]))