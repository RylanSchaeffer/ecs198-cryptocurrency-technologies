import hashlib
import math
import sys

def main():
	n = int(sys.argv[2]) #n = num leading zeroes
	with open(sys.argv[1]) as f:#read command line arg
		transactions = f.read()
	original = transactions.split('\n') #splits based on new line
	depth = int(math.log(len(original)+1,2)) #num of iterations to construct tree
	check = "" #constructs string of leading zeroes to check
	for i in range(0,n):
		check+="0"

	result = ""
	hashes = []
	x = -1
	while not result == check:
		x+=1
		hashes = original[:] #reset merkle tree
		hashes.append( str(x) ) #adds number m
		for i in range(0, len(hashes)): # hashes first round
			hashes[i] = hashlib.sha256(hashes[i])
		for i in range(1,depth+1): #creates merkle
			for j in range(0, len(hashes), pow(2,i)):
				u = hashes[j].hexdigest()
				v = hashes[j+pow(2,i-1)].hexdigest()
				hashes[j] = hashlib.sha256(u+v)	
		result = hashes[0].hexdigest()[:n]
	return x
print main()