def LCS(S, T):
	m = len(S)
	n = len(T)
	L = [ [0] * (n + 1) for i in xrange(m + 1)]
	LCS_set = set()
	longest = 0
	for i, x in enumerate(S):
		for j, y in enumerate(T):
			if(x == y):
				v = L[i][j] + 1
				L[i + 1][j + 1] = v
				if v > longest:
					longest = v
					LCS_set = set()
				if v == longest:
					LCS_set.add(S[i-v+1 : i + 1])
	print LCS_set
	
LCS("asdfasdfasdfasjdfuahsedasndjknfs", "asdhufrhqwasdfeahbsjdfjksjfdkas")					