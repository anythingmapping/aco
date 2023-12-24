import random

class Ant:
    def __init__(self, colony, start_node):
        """
        Initialize the ant.

        :param colony: Reference to the AntColony instance.
        :param start_node: The starting node for the ant.
        """
        self.colony = colony
        self.current_node = start_node
        self.visited_nodes = [start_node]
        self.unvisited_nodes = set(self.colony.graph.nodes) - {start_node}

    def move(self):
        """
        Make a move based on the probability of choosing the next node.
        """
        probabilities = self.calculate_probabilities()
        next_node = self.select_next_node(probabilities)
        self.visited_nodes.append(next_node)
        self.unvisited_nodes.remove(next_node)
        self.current_node = next_node

    def calculate_probabilities(self):
        """
        Calculate the probabilities of moving to each unvisited neighbor node.
        """
        probabilities = {}
        total_pheromone = sum(self.colony.graph.get_pheromone(self.current_node, neighbor) for neighbor in self.unvisited_nodes)
        
        for neighbor in self.unvisited_nodes:
            pheromone = self.colony.graph.get_pheromone(self.current_node, neighbor)
            if pheromone == 0:
                probabilities[neighbor] = 0
            else:
                probabilities[neighbor] = pheromone / total_pheromone
                
        return probabilities

    def select_next_node(self, probabilities):
        """
        Select the next node based on the given probabilities.
        """
        return random.choices(list(probabilities.keys()), weights=list(probabilities.values()), k=1)[0]

    def update_pheromone(self, delta_pheromone):
        """
        Update the pheromone trail for the edges traversed by the ant.
        """
        for i in range(len(self.visited_nodes) - 1):
            current_node = self.visited_nodes[i]
            next_node = self.visited_nodes[i + 1]
            self.colony.graph.update_pheromone(current_node, next_node, delta_pheromone)

class AntColony:
    def __init__(self, graph, num_ants, evaporation_rate=0.5, initial_pheromone=1.0):
        """
        Initialize the ant colony.

        :param graph: Graph representing the problem.
        :param num_ants: Number of ants in the colony.
        :param evaporation_rate: Rate at which pheromone evaporates.
        :param initial_pheromone: Initial pheromone value for edges.
        """
        self.graph = graph
        self.num_ants = num_ants
        self.evaporation_rate = evaporation_rate
        self.initial_pheromone = initial_pheromone
        self.ants = [Ant(self, start_node=random.choice(list(graph.nodes))) for _ in range(num_ants)]

    def simulate(self, num_iterations):
        """
        Simulate the ant colony optimization algorithm for a given number of iterations.

        :param num_iterations: Number of iterations.
        """
        for _ in range(num_iterations):
            for ant in self.ants:
                while ant.unvisited_nodes:
                    ant.move()
                ant.update_pheromone(self.evaporation_rate)
                ant.visited_nodes = [ant.visited_nodes[0]]  # Reset to the starting node
                ant.unvisited_nodes = set(self.graph.nodes) - {ant.visited_nodes[0]}
