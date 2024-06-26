import transform_matrix


class Evaluation:
    def __init__(self, problem):
        self.distance_matrix = transform_matrix.transform_low_diag_matrix_to_block_matrix(problem)

    def get_fitness_for_individual(self, individual):
        """
        Als Teil der Evaluation benötigen wir die Fitness.
        :return:
        Fitnesswert des Individuals
        """
        weight = 0
        for i in range(len(individual)):
            weight += self.distance_matrix[individual[i - 1]][individual[i]]
        return 1.0 / (1.0 + weight)

    def get_weight_for_individual(self, individual):
        weight = 0
        for i in range(len(individual)):
            weight += self.distance_matrix[individual[i - 1]][individual[i]]
        return weight

    def get_fitness_for_population(self, population):
        """
        Kleine Helperfunction, überwiegend für debug zwecke
        :param population:
        :return:
        """
        fitness = 0
        for individual in population:
            fitness += self.get_fitness_for_individual(individual)
        return fitness

    def get_fittest_individual_for_population(self, population):
        max_fitness = self.get_fitness_for_individual(population[0])
        index_of_fittest_individual = 0
        for i in range(len(population)):
            fitness_of_individual = self.get_fitness_for_individual(population[i])
            if max_fitness < fitness_of_individual:
                max_fitness = fitness_of_individual
                index_of_fittest_individual = i
        return population[index_of_fittest_individual], index_of_fittest_individual

    def get_x_fittest_individuals_for_population(self, population, x):
        fittest_individuals = []
        temp_population = population.copy()
        for i in range(x):
            fittest_individual, index_of_fittest_individual = self.get_fittest_individual_for_population(temp_population)
            fittest_individuals.append(fittest_individual)
            del temp_population[index_of_fittest_individual]
        return fittest_individuals
