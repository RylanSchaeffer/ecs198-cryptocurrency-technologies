import sys
from math import ceil, log
from hashlib import sha256

def main():
	hashes = []
	with open(sys.argv[1]) as file:
		for line in file:  
			hashes.append(sha256(line.rstrip()).hexdigest())
		hashes+= [sha256('null').hexdigest()] * int(pow(2, ceil(log(len(hashes), 2))) - len(hashes))
	
		end = len(hashes)
		while end != 1:
			for i in range (0, end, 2):
				hashes[int(i/2)] = sha256((hashes[i]+ hashes[i+1])).hexdigest()
			end/=2	
	
		print (sys.argv[1]+ ": " + hashes[0])