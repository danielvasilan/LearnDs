import numpy as np
import matplotlib.pyplot as plt

# plot the relationship between the items weight and items value

f = open("ex1.txt", "r")
items_nm = []
items_wt = []
items_val = []
for line in f:
	values = line.split(";")
	items_nm.append(values[0])
	items_wt.append(int(values[1]))
	items_val.append(int(values[2]))

fig, ax = plt.subplots()
ax.scatter(items_wt, items_val)

for i,name in enumerate(items_nm):
	ax.annotate(name, (items_wt[i], items_val[i]))

plt.show()



