import hashlib 
import sys
import numpy as np

def main():

	#Initial_Hash
	hashes = []
	with open(str(sys.argv[1]),'rb') as fin:
    		for line in fin:
			hashes = np.append(hashes, hashlib.sha256(line).hexdigest().encode('utf-8'))
			
	#Append_Power_2
	while np.log(np.size(hashes)) % np.log(2) != 0:
		hashes = np.append(hashes, hashlib.sha256(str('null')).hexdigest().encode('utf-8') )

	#Iterative_Hash
	j = 0
	while j < np.log(np.size(hashes)) / np.log(2):
		i = 0
		while (i+1) < (np.size(hashes)): 
			hashes[i] = hashlib.sha256(hashes[i] + hashes[i+1] ).hexdigest().encode('utf-8')
			i = i + 2

		times = (np.log( np.size(hashes) / 2 ) / np.log(2)) + 2
		d = 1
		while d < times:
			hashes = np.delete(hashes, d)
			d = d + 1
		j = j + 1

	return hashlib.sha256(hashes[0] + hashes[1]).hexdigest().encode('utf-8')
	#return hashes[0].hexdigest()

print main()
