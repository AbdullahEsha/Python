import random

def create_cromosome(n):
    return [random.radint(1,n) for i in range(n)]

def cross_over(p1, p2):
    plen = len(p1)
    p = random.randint(0, plen-1)
    return p1[0:p] + p2[p:plen]

def mutation(chromosome):
    clen = len(chromosome)
    rand_index = random.randint(0, clen-1)
    rand_val = random.randint(1, clen)
    chromosome[rand_index] = rand_val
    return chromosome

def fitness(chromosome):
    hc = sum([chromosome.count(q) for q in chromosome])
    dc = 0
    clen = len(chromosome)
    ld = [0] * 2*clen
    rd = [0] * 2*clen
    for i in range(clen):
        ld[i + chromosome[i]-1] += 1
        rd
    
    
c1 = create_cromosome(8)
print(c1)
fitness(c1)