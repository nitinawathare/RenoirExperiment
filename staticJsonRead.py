import json, ast
from pprint import pprint


with open('/home/ubuntu/gitRepoRenoir/.ethereum/static-nodes.json') as fopen:
	data = json.load(fopen)
print(data[0])
