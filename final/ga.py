import random

POPULATION_SIZE = 100
GOAL = 'Midterm is over for 2020!'
GENES = 'abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!'

class GA(object):
    
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
    
    @classmethod
    def gnome(self):
        global GOAL
        gnome_len = len(GOAL)
        return [self.mutation() for _ in range(gnome_len)]
    
    @classmethod   
    def mutation(self):
        global GENES
        gene = random.choice(GENES)
        return gene
        
    def cross_over(self, other_parent):
        offspring = []
        for i,j in zip(self.chromosome, other_parent.chromosome):
            p = random.random()
            if p < 0.5:
                offspring.append(i)
            elif p < 0.9:
                offspring.append(j)
            else:
                offspring.append(self.mutation())
                
        return GA(offspring)
    
    def cal_fitness(self):
        global GOAL
        fitness = 0
        for i,j in zip(self.chromosome, GOAL):
            if i != j:
                fitness += 1
        return fitness
    


generation = 1
found = False
population = []

for _ in range(POPULATION_SIZE):
    gnome = GA.gnome()
    population.append(GA(gnome))
    
while not found:
    population = sorted(population, key= lambda a:a.fitness)
    
    if population[0].fitness <= 0:
        found = True
        break
    
    new_generation = []
    
    a = int((20*POPULATION_SIZE)/100)
    new_generation.extend(population[:a])

    a = int((80*POPULATION_SIZE)/100)
    for i in range(a):
        p1 = random.choice(population[:30])
        p2 = random.choice(population[:30])
        
        c = p1.cross_over(p2)
        new_generation.append(c)
        
    population = new_generation
    print('Generation: ', generation, 'String: ', "".join(population[0].chromosome), 'Fitness: ', population[0].fitness)
    
    generation += 1
    
    
print('Generation: ', generation, 'String: ', "".join(population[0].chromosome), 'Fitness: ', population[0].fitness)
    
    


