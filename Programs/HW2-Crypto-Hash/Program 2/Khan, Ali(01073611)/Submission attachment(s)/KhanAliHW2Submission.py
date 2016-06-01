import sys
import math
import hashlib


def main():

	transactions = 0
	lines = list()
	evens = list()
	odds = list()

	f = open(sys.argv[1],"rb")

	for aline in f:
    		m = hashlib.sha256(aline)
    		lines.append(m)
    		transactions = transactions + 1

	f.close()

	nextpow = pow(2, math.ceil ( math.log( len( lines ), 2 ) ) )
	dif = int(nextpow - transactions)


	for i in range (0, dif):
		m = hashlib.sha256()
		m.update("null")
		lines.append(m)

	for i in range (0, len(lines)):
		if i%2 != 0:
			odds.append(i)

	for j in range (0, len(lines)):
		if j%2 == 0:
			evens.append(j)

	length = len(lines)

	while (length != 1):
		length = length / 2
		for i in range (0, (length)):
			h = lines[evens[i]].hexdigest() + lines[odds[i]].hexdigest()
			m = hashlib.sha256(h)

			lines[i] = m
		

#print m.hexdigest()


	print lines[0].hexdigest()
	return lines[0].hexdigest()

if __name__ == '__main__':
    main()



