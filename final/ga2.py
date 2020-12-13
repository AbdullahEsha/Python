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
        
    def cross_over(self, other_parent, c_type):
        offspring = []
        c_type = input("\nSelect your cross over operator:\n"
                       "0 - Single Crossover\n"
                       "1 - Two Points Crossover\n"
                       "2 - Uniform Crossover\n"
                       "\nEnter your input (enter ! to exit):")
        if crossover_type == "!":
            exit()        
        return GA(offspring)
    
    def cal_fitness(self):
        global GOAL
        fitness = 0
        for i,j in zip(self.chromosome, GOAL):
            if i != j:
                fitness += 1
        return fitness

#single point
    def single_point_cross_over(problem, population):
    crossover_population = []
    parent_male, parent_female = select_parents(population)
    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)
        
        crossover_point = randint(1, 5)
      
        male[crossover_point:], female[crossover_point:] = \
            female[crossover_point:], male[crossover_point:]
        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))
    crossover_population = mut(problem, crossover_population)
    return crossover_population

#two point
    def two_point_cross_over(problem, population):
        crossover_population = []
       
        crossover_points = [randint(1, 7)]
        second_point = randint(1, 7)
        while second_point == crossover_points[0]:
            second_point = randint(1, 7)
        crossover_points.append(second_point)
     
        parent_male, parent_female = select_parents(population)
        for female in parent_female:
            male = copy(list(parent_male))
            female = list(female)
            male[:crossover_points[0]], female[:crossover_points[0]] = \
                female[:crossover_points[0]], male[:crossover_points[0]]
            male[crossover_points[1]:], female[crossover_points[1]:] = \
                female[crossover_points[1]:], male[crossover_points[1]:]
            crossover_population.append(''.join(str(item) for item in male))
            crossover_population.append(''.join(str(item) for item in female))
        crossover_population = mut(problem, crossover_population)
        return crossover_population

#uniform-point
    def uniform_point_cross_over(problem, population):
        crossover_population = []
       
        parent_male, parent_female = select_parents(population)
        
        for female in parent_female:
            male = copy(list(parent_male))
            female = list(female)
            
            for gene in male:
                probability_of_swap = 0.5
                if random() > probability_of_swap:
                    index = male.index(gene)
                    male[index], female[index] = female[index], male[index]
                    crossover_population.append(''.join(str(item) for item in male))
                    crossover_population.append(''.join(str(item) for item in female))
        crossover_population = mut(problem, crossover_population)
        return crossover_population

#---------------------------------------------------
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