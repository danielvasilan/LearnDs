from scipy.stats import expon

ar = []
for idx in range (0, 100):
	ar.append(idx)

rr = (100 - expon.rvs(scale = 100, size=5)).astype(int)

rrr = rr[rr >= 0]

rrr.sort()




print (rrr)

print (set(ar) & set(rr))