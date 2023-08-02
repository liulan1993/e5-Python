import numpy as np

class AntColony:
    def __init__(self, num_ants, num_iterations, num_cities, alpha=1, beta=1, rho=0.5, Q=100):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.num_cities = num_cities
        self.alpha = alpha  # 影响信息素浓度的因子
        self.beta = beta    # 影响能见度的因子
        self.rho = rho      # 信息素残留系数
        self.Q = Q          # 信息素增加强度常数

        self.distances = np.zeros((num_cities, num_cities))
        self.pheromone = np.ones((num_cities, num_cities))
        np.fill_diagonal(self.distances, np.inf)  # 设置对角线上的距离为无穷大

    def add_distance(self, city1, city2, distance):
        self.distances[city1][city2] = distance
        self.distances[city2][city1] = distance

    def solve(self):
        global_best_path = None
        global_best_distance = np.inf

        for iteration in range(self.num_iterations):
            all_paths = []
            all_distances = []

            for ant in range(self.num_ants):
                visited = set()
                current_city = np.random.randint(self.num_cities)

                path = [current_city]
                distance = 0

                while len(visited) < self.num_cities:
                    visited.add(current_city)
                    unvisited = np.setdiff1d(range(self.num_cities), list(visited))
                    next_city = self.pick_next_city(current_city, unvisited)
                    path.append(next_city)
                    distance += self.distances[current_city][next_city]
                    current_city = next_city

                distance += self.distances[path[-1]][path[0]]  # 回到起点
                all_paths.append(path)
                all_distances.append(distance)

                if distance < global_best_distance:
                    global_best_distance = distance
                    global_best_path = path

                self.update_pheromone(path, distance)

            self.evaporate_pheromone()
            self.update_pheromone(global_best_path, global_best_distance)

            if iteration % 10 == 0:
                print("Iteration", iteration+1, "- Best distance:", global_best_distance)

        return global_best_path, global_best_distance

    def pick_next_city(self, current_city, unvisited):
        pheromone = self.pheromone[current_city][unvisited]
        visibility = 1 / self.distances[current_city][unvisited]
        probabilities = np.power(pheromone, self.alpha) * np.power(visibility, self.beta)
        probabilities = probabilities / np.sum(probabilities)
        next_city = np.random.choice(unvisited, p=probabilities)
        return next_city

    def update_pheromone(self, path, distance):
        for i in range(self.num_cities-1):
            current_city = path[i]
            next_city = path[i+1]
            self.pheromone[current_city][next_city] += self.Q / distance

        self.pheromone[path[-1]][path[0]] += self.Q / distance

    def evaporate_pheromone(self):
        self.pheromone *= (1 - self.rho)


# 示例用法
def main():
    colony = AntColony(num_ants=50, num_iterations=100, num_cities=10, alpha=1, beta=2, rho=0.1, Q=100)
    
    # 添加城市之间的距离
    colony.add_distance(0, 1, 10)
    colony.add_distance(0, 2, 20)
    colony.add_distance(0, 3, 30)
    # ...
    
    best_path, best_distance = colony.solve()
    
    print("Best path:", best_path)
    print("Best distance:", best_distance)


if __name__ == '__main__':
    main()
