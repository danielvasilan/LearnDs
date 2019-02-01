from random import randint
from scipy.stats import expon


print("Knapsack Problem - solution")

# input data

max_generations = 10
population_size = 100
knapsack_capacity = 400
mutation_rate = 0.01
replacement_rate = 0.2

f = open("ex1.txt", "r")
items_nm = []
items_wt = []
items_val = []
for line in f:
	values = line.split(";")
	items_nm.append(values[0])
	items_wt.append(int(values[1]))
	items_val.append(int(values[2]))

genome_sz = len(items_nm)

# Logic

def newGenome():
	new_genome = [] 
	for x in range(1, genome_sz + 1):
		new_genome.append(randint(0, 1))
	return new_genome

def newGenome_opt():
	new_genome = [0] * genome_sz
	tot_weight = 0
	while tot_weight < knapsack_capacity:
		# randomly pick one of the genom positions
		idx = randint(0, genome_sz - 1)
		if new_genome[idx] == 0:
			if items_wt[idx] + tot_weight <= knapsack_capacity :
				new_genome[idx] = 1
				tot_weight += items_wt[idx]
			else:
				break
			
	return new_genome	
	
class Individual:

	def __init__(self, indiv_id, new_genome):
		if len(new_genome) == 0:
			self.genome = newGenome_opt()
		else:
			self.genome = new_genome
		self.id = indiv_id
		self.status = " "
		
		self.weight = 0
		self.val = 0
		self.evaluate()

	def printString(self):
		print(str(self.id) + str(" ") + str(self.genome) + str(" w=") + str(self.weight) + " c=" + str(self.val))
	
	def evaluate(self):
		new_val = 0
		new_weight = 0
		for idx in range(0, genome_sz):
			new_val += items_val[idx] * self.genome[idx]
			new_weight += items_wt[idx] * self.genome[idx]
		self.weight = new_weight
		self.val = new_val
		if self.weight > knapsack_capacity:
			self.status = "_"

def combinedGenome(genome1, genome2):
	# will take the first part of the first genome + the last part of the second genome 
	new_genome = []
	crossover_point = int(len(genome1) / 2) + 1
	for idx in range(0, crossover_point):
		new_genome.append(genome1[idx])
	for idx in range(crossover_point, len(genome2)):
		new_genome.append(genome2[idx])
	return new_genome
			
class Population:
	individuals = []
	bestIndividualId = 0
	
	def __init__(self, size):
		self.generation_no = 0
		for x in range(1, size + 1):
			new_individual = Individual(x, [])
			self.individuals.append(new_individual)
	
	def printString(self):
		s = "G=" + str(self.generation_no).ljust(3,' ') + " "
		for x in self.individuals:
			s += str(x.val).ljust(3,' ') + "(" + str(x.weight).ljust(3, ' ') + x.status + " "
		s += " b=" + str(self.bestIndividualId)
		print (s)
	
	def selection(self):
		# update the status of all the individuals to " "
		for x in self.individuals:
			x.status = " "
		ordIndividuals = self.individuals.copy()
		ordIndividuals.sort(key = lambda x: x.val if x.weight <= knapsack_capacity else 0, reverse=True)
		self.bestIndividualId = ordIndividuals[0].id
		# replace the worst individuals
		replace_num = int(population_size * replacement_rate)
		for idx in range(population_size - replace_num, population_size):
			replace_id = ordIndividuals[idx].id
			new_individual = Individual(replace_id, [])
			new_individual.status = "+"
			self.individuals[replace_id - 1] = new_individual
		# combine the best individuals and replace 
		combine_num = int(replace_num / 2)
		for idx in range(0, combine_num):
			parent1 = ordIndividuals[idx]
			parent2 = ordIndividuals[idx + 1]
			replace_id1 = ordIndividuals[population_size - replace_num - (2 * idx)].id
			replace_id2 = replace_id1 - 1
			new_indiv1 = Individual(replace_id1, combinedGenome(parent1.genome, parent2.genome))
			new_indiv1.status = "#"
			new_indiv2 = Individual(replace_id2, combinedGenome(parent2.genome, parent1.genome))
			new_indiv2.status = "#"
			# determine the individuals to be replaced
			print (str(idx) + " - " + str(replace_id1))
			# replace the 
			self.individuals[replace_id1-1] = new_indiv1
			self.individuals[replace_id2-1] = new_indiv2
		
		
	def mutation(self):
		max_mutations = int(population_size*mutation_rate)
		mutation_ids = (population_size - expon.rvs(scale = population_size, size = max_mutations)).astype(int)
		for rand_individual_id in mutation_ids[mutation_ids > 0]:
	
		#for m in range(1, population_size + 1):
		#	rand_individual_id = randint(1, (population_size / mutation_rate))
		#	if rand_individual_id <= population_size:
			new_individual = Individual(rand_individual_id, [])
			new_individual.status = "!"
			self.individuals[rand_individual_id - 1] = new_individual
	
	def evaluate(self):
		for x in self.individuals:
			x.evaluate()
	
	def printBest(self):
		bestIndividual = self.individuals[self.bestIndividualId-1]
		print("Best: Id=" + str(self.bestIndividualId) + " V=" + str(bestIndividual.val) + " W=" + str(bestIndividual.weight))
		msg = "	"
		for idx in range(0, len(bestIndividual.genome)):
			if bestIndividual.genome[idx] == 1:
				msg += " " + items_nm[idx]
		print(msg)
	
	def storeContent(self, storage):
		for m in self.individuals :
			histRecord = [self.generation_no, m.id, m.weight, m.val, m.status]
			histRecord += m.genome
			storage.content.append(histRecord)

	
class Storage:
	#definition = Generation;IndividId;Weight;Value;Genome[]
	content = []
	
	def __init__(self):
		self.content = []
	
	def writeInFile (self, fileName):
		f = open(fileName, "w")
		for rec in self.content:
			f.write(str(rec)+"\n")
		f.close()
	
### main program

# initialize
history = Storage()
population = Population(population_size)
# population.printString()
for g in range(1, max_generations + 1):
	population.generation_no += 1
	population.selection()
	population.mutation()
	population.evaluate()
#	population.printString()
	population.storeContent(history)

history.writeInFile("ex1_run.csv")

print("Generations: " + str(population.generation_no))
population.printBest()
