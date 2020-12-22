import os

#adjacencyListy = [(0, 1), (0, 2), (0, 4), (1, 2), (3, 4)]
# adjacencyListy = [(0, 12), (0, 6), (0, 14), (1, 28), (1, 9), (1, 12), (1, 25), (1, 31), (2, 8), (2, 3), (2, 12), (2, 29), (2, 30), (3, 28), (3, 10), (3, 23), (4, 28), (4, 15), (5, 9), (5, 17), (6, 14), (7, 15), (8, 25), (8, 28), (9, 12), (9, 28), (9, 23), (10, 26), (10, 30), (11, 12), (11, 29), (12, 34), (12, 17), (12, 26), (12, 28), (12, 30), (13, 18), (13, 28), (15, 22), (16, 32), (16, 35), (16, 30), (19, 30), (20, 21), (21, 26), (21, 27), (22, 29), (23, 28), (24, 30), (25, 28), (26, 28), (26, 29), (28, 32), (28, 29), (28, 30), (30, 36), (30, 31), (33, 36)]
adjacencyListy=[(0, 1)]
# adjacencyListy=[(0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 4), (1, 5), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 9), (4, 5), (4, 6), (5, 6), (5, 7), (5, 8), (5, 9), (6, 7), (7, 8), (7, 9)]
# adjacencyListy = [(0, 38), (0, 9), (0, 12), (0, 13), (0, 22), (0, 30), (1, 34), (1, 44), (1, 29), (2, 16), (2, 43), (2, 47), (3, 31), (4, 17), (4, 20), (5, 18), (5, 21), (6, 14), (7, 40), (7, 10), (7, 14), (8, 33), (9, 30), (10, 34), (10, 37), (10, 17), (10, 21), (10, 25), (10, 30), (11, 17), (11, 43), (11, 28), (11, 30), (12, 17), (14, 36), (14, 39), (14, 17), (14, 21), (14, 27), (14, 30), (15, 18), (17, 32), (17, 43), (17, 40), (17, 44), (17, 18), (17, 20), (17, 21), (17, 46), (17, 30), (17, 31), (18, 41), (19, 26), (19, 30), (20, 30), (21, 38), (21, 39), (21, 44), (21, 23), (21, 25), (21, 42), (21, 30), (22, 45), (22, 30), (24, 30), (25, 40), (25, 27), (30, 35), (30, 37), (30, 40), (30, 44), (30, 43), (30, 47), (31, 45), (31, 41), (33, 45), (34, 44), (35, 47), (37, 40), (40, 44), (42, 48), (43, 44)]


enodeDir = []
#i=0
with open('static.txt') as fp:
    for line in fp:
    	#print line
    	enodeDir.append(line)

length = len(enodeDir)
for i in range(length): 
    file1 = open("staticJsonFiles/static.json"+str(i),"w") 
    file1.write("["+"\n")
    file1.close()
    print(enodeDir[i])

for pair in adjacencyListy:  
	file1 = open("staticJsonFiles/static.json"+str(pair[0]),"a")
	file2 = open("staticJsonFiles/static.json"+str(pair[1]),"a")
	file1.write('"'+enodeDir[pair[1]].strip('\n')+'"'+","+"\n")
	file2.write('"'+enodeDir[pair[0]].strip('\n')+'"'+","+"\n")
	file1.close()
	file2.close()

for i in range(length): 
	file1 = open("staticJsonFiles/static.json"+str(i),"a") 
	file1.seek(0, os.SEEK_END)
	file1.seek(file1.tell() - 2, os.SEEK_SET)
	file1.truncate()
	file1.write("\n"+"]"+"\n")
