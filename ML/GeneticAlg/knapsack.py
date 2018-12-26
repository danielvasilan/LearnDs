from random import randint

print("Hello, World!")

# input data

max_generations = 20
num_generations = 1
population_size = 10
knapsack_capacity = 30

items_nm = ["A","B","C","D","E","F","G"]
items_wt = [2,3,6,7,5,9,4]
items_ct = [6,5,8,9,6,7,3]

genome_sz = len(items_nm)

# Logic
class Individual:

	def __init__(self, indiv_id):
		new_genome = []
		for x in range(1, genome_sz + 1):
			new_genome.append(randint(0, 1))
		self.genome = new_genome
		self.id = indiv_id
		
		self.weight = 0
		self.cost = 0
		self.evaluate()

	def printString(self):
		print(str(self.id) + str(" ") + str(self.genome) + str(" w=") + str(self.weight) + " c=" + str(self.cost))
	
	def evaluate(self):
		new_cost = 0
		new_weight = 0
		for idx in range(0, genome_sz):
			new_cost += items_ct[idx] * self.genome[idx]
			new_weight += items_wt[idx] * self.genome[idx]
		self.weight = new_weight
		self.cost = new_cost
	
class Population:
	individuals = []
	
	def __init__(self, size):
		for x in range(1, size + 1):
			new_individual = Individual(x)
			self.individuals.append(new_individual)
	
	def printString(self):
		s = " "
		for x in self.individuals:
			s += str(x.cost) + " "
		print (s)
	
	def selection(self):
		print("selection")
		
	def mutation(self):
		print("mutation")
		
### main program

# initialize
population = Population(population_size)
population.printString()
for g in range(1, max_generations):
	num_generations += 1
	population.selection()

print("Generations: " + str(num_generations))
