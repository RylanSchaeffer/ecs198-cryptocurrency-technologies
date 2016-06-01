import sys
from math import ceil, log
from hashlib import sha256 

def computeRootHash(hashes):
	temp = hashes[:]
	end = len(temp)
	while end != 1:
		for i in range (0, end, 2):
			temp[int(i/2)] = sha256((temp[i]+ temp[i+1])).hexdigest()
		end/=2
	return temp[0]

def main():
	filepath = sys.argv[1]
	target = '0' * sys.argv[2]
	
	hashes = []
	with open(filepath) as file:
		for line in file:  
			hashes.append(sha256(line.rstrip()).hexdigest())
		
		nonce = 0
		hashes.append(sha256(str(nonce)).hexdigest())
		rootHash = computeRootHash(hashes)
		
		while(not rootHash.startswith(target)):
			nonce += 1
			hashes[len(hashes) - 1] = sha256(str(nonce)).hexdigest()
			rootHash = computeRootHash(hashes)
	
		return nonce