# Python program for solution of M Coloring
# problem using backtracking
 
# Approach: The idea is to assign colors one by one to different vertices, starting from the vertex 0. Before 
# assigning a color, check for safety by considering already assigned colors to the adjacent vertices i.e check 
# if the adjacent vertices have the same color or not. If there is any color assignment that does not violate 
# the conditions, mark the color assignment as part of the solution. If no assignment of color is possible 
# then backtrack and return false.

# Algorithm: 

# 1) Create a recursive function that takes the graph, current index, number of vertices, and output color array.
# 2) If the current index is equal to the number of vertices. Print the color configuration in output array.
# 3) Assign a color to a vertex (1 to m).
# 4) For every assigned color, check if the configuration is safe, (i.e. check if the adjacent vertices do not have 
#     the same color) recursively call the function with next index and number of vertices
# 5) If any recursive function returns true break the loop and return true.
# 6) If no recursive function returns true then return false.

class BacktrakingGraph():
 
    def __init__(self, adjacentMatrix):
        self.numberOfVertices = len(adjacentMatrix)
        self.graph = adjacentMatrix
        self.colour = [0] * self.numberOfVertices
 
    # A utility function to check if the current color assignment is safe for vertex v
    def isSafe(self, currentColor, vertex, colors):
        for i in range(self.numberOfVertices):
            if self.graph[vertex][i] == 1 and colors[i] == currentColor: 
                return False # is not safe assing
        return True
     
    # A recursive utility function to solve m coloring problem
    def paintTheGraph(self, totalColors, colors, vertex):
        if vertex == self.numberOfVertices: return True
 
        for color in range(1, totalColors + 1):
            if self.isSafe(color, vertex, colors):
                colors[vertex] = color
                if self.paintTheGraph(totalColors, colors, vertex + 1): return True
                colors[vertex] = 0
 
    def graphColouring(self):
        if self.paintTheGraph(self.numberOfVertices, self.colour, 0) == None: return False
 
    def printPaintedGraph(self):
        # Print the solution
        for index,c in enumerate(self.colour): print(f"Vertex {index}   --->   Color {c - 1}")
        return True
 