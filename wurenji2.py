import math
import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

def heuristic(node, goal):
    return math.sqrt((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2)

def astar(start, goal, obstacles):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (start.f, start))
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        
        closed_set.add(current)
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                neighbor = Node(current.x + dx, current.y + dy)
                if neighbor.x < 0 or neighbor.x >= 100 or neighbor.y < 0 or neighbor.y >= 100:
                    continue
                if neighbor in closed_set:
                    continue
                if (neighbor.x, neighbor.y) in obstacles:
                    continue
                neighbor.g = current.g + 1
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current
                heapq.heappush(open_list, (neighbor.f, neighbor))
    
    return None

# 示例使用
start = Node(0, 0)
goal = Node(9, 9)
obstacles = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)]
path = astar(start, goal, obstacles)
print(path)
