import numpy as np

class AntColonyOptimization:
    def __init__(self, num_ants, num_iterations, num_cities, alpha=1, beta=5, rho=0.5):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.num_cities = num_cities
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.pheromone_matrix = np.ones((num_cities, num_cities))
        self.distance_matrix = np.array([np.random.randint(1, 100, num_cities) for _ in range(num_cities)])

    def run(self):
        best_path = None
        best_distance = np.inf

        for iteration in range(self.num_iterations):
            ant_paths = self.generate_ant_paths()
            ant_distances = self.calculate_ant_distances(ant_paths)

            if np.min(ant_distances) < best_distance:
                best_distance = np.min(ant_distances)
                best_path = ant_paths[np.argmin(ant_distances)]

            self.update_pheromone_matrix(ant_paths, ant_distances)

        return best_path, best_distance

    def generate_ant_paths(self):
        ant_paths = np.zeros((self.num_ants, self.num_cities), dtype=int)

        for ant in range(self.num_ants):
            visited = np.zeros(self.num_cities, dtype=bool)
            current_city = np.random.randint(0, self.num_cities)
            ant_paths[ant, 0] = current_city
            visited[current_city] = True

            for step in range(1, self.num_cities):
                next_city = self.choose_next_city(current_city, visited)
                ant_paths[ant, step] = next_city
                visited[next_city] = True
                current_city = next_city

        return ant_paths

    def calculate_ant_distances(self, ant_paths):
        ant_distances = np.zeros(self.num_ants)

        for ant in range(self.num_ants):
            for step in range(self.num_cities - 1):
                city1 = ant_paths[ant, step]
                city2 = ant_paths[ant, step+1]
                ant_distances[ant] += self.distance_matrix[city1, city2]

            ant_distances[ant] += self.distance_matrix[ant_paths[ant, -1], ant_paths[ant, 0]]

        return ant_distances

    def choose_next_city(self, current_city, visited):
        unvisited_cities = np.where(~visited)[0]
        pheromone_values = self.pheromone_matrix[current_city, unvisited_cities]
        attractiveness_values = 1 / self.distance_matrix[current_city, unvisited_cities]**self.beta
        probabilities = pheromone_values**self.alpha * attractiveness_values
        probabilities /= np.sum(probabilities)

        next_city = np.random.choice(unvisited_cities, p=probabilities)

        return next_city

    def update_pheromone_matrix(self, ant_paths, ant_distances):
        delta_pheromone = np.zeros((self.num_cities, self.num_cities))

        for ant in range(self.num_ants):
            for step in range(self.num_cities - 1):
                city1 = ant_paths[ant, step]
                city2 = ant_paths[ant, step+1]
                delta_pheromone[city1, city2] += 1 / ant_distances[ant]

            delta_pheromone[ant_paths[ant, -1], ant_paths[ant, 0]] += 1 / ant_distances[ant]

        self.pheromone_matrix = (1 - self.rho) * self.pheromone_matrix + delta_pheromone

# Example usage
aco = AntColonyOptimization(num_ants=10, num_iterations=100, num_cities=20)
best_path, best_distance = aco.run()
print("Best path:", best_path)
print("Best distance:", best_distance)
