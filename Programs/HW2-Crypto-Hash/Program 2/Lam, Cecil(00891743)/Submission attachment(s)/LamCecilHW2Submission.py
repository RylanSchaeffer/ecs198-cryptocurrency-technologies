import hashlib
import math
import sys

with open(sys.argv[1]) as f:#read command line arg
	transactions = f.read()
hashes = transactions.split('\n') #splits based on new line
while(math.log(len(hashes),2)%1 != 0): #adds null until power of 2
	hashes.append('null')

depth = int(math.log(len(hashes),2)) #num of iterations to construct tree

for x in range(0, len(hashes)): #first hashing
	hashes[x] = hashlib.sha256(hashes[x])

for x in range(1,depth+1):
	for y in range(0, len(hashes), pow(2,x)):
		u = hashes[y].hexdigest()
		v = hashes[y+pow(2,x-1)].hexdigest()
		hashes[y] = hashlib.sha256(u+v)
print hashes[0].hexdigest()
