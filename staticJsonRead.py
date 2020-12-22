import json, ast
from pprint import pprint
import sys

# print(sys.argv[1])
with open(sys.argv[2]+'/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum'+sys.argv[1]+'/static-nodes.json') as fopen:
	data = json.load(fopen)
print(data[0])
