import numpy as np
"""
La población está formada por N individuos.
Cada individuo tiene dos cromosomas, que contienen alelo "A" o "a", con probabilidad p o 1-p, respectivamente.
La población es una lista.
"""
def build_population(N, p):
    population = []
    for i in range(N):
        allele1 = "A"
        if np.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if np.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

""" 
Contar los genotipos.
Devuelve un diccionario de frecuencias genotípicas.
"""

def compute_frequencies(population):
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

""" 
Crear nueva generación a través de la reproducción para cada uno de N nuevos descendientes:
- elegir a los padres al azar
- la descendencia recibe un cromosoma de cada uno de los padres.
"""
def reproduce_population(population):
    new_generation = []
    N = len(population)
    for i in range(N):
        dad = np.random.randint(N)
        mom = np.random.randint(N)
        chr_mom = np.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        new_generation.append(offspring)
    return new_generation

"""
Esta funcion abarca todas las funciones anteriores:
- Construye una lista de la población
- Devuelve las frecuencias genotipicas
- Si el numero de AA y aa genotipipos es igual a la cantidad de los indivuduos los allelos alcanzan una fijación en la generación
- imprime el conteo de los genotipos
- devuelve el numero de generaciones y el conteo de genotipos
"""
def simulate_drift(N, p):
    my_pop = build_population(N, p)
    fixation = False
    num_generations = 0
    while fixation == False:
        genotype_counts = compute_frequencies(my_pop)
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N):
            print("An allele reached fixation at generation", num_generations)
            print("The genotype counts are")
            print(genotype_counts)
            fixation == True
            break
        my_pop = reproduce_population(my_pop)
        num_generations += 1
    return num_generations, genotype_counts