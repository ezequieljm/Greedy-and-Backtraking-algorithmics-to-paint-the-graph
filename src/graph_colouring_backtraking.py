# Python program for solution of M Coloring
# problem using backtracking
 
class Graph():
 
    def __init__(self, number_of_vertices):
        self.vertices = number_of_vertices
        self.graph = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
 
    # A utility function to check if the current color assignment is safe for vertex v
    def is_safe(self, current_color, vertex, colors):
        for i in range(self.vertices):
            if self.graph[vertex][i] == 1 and colors[i] == current_color: return False # is not safe assing
        return True
     
    # A recursive utility function to solve m coloring problem
    def paint_the_graph(self, total_colors, colors, vertex):
        if vertex == self.vertices: return True
 
        for color in range(1, total_colors + 1):
            if self.is_safe(color, vertex, colors):
                colors[vertex] = color
                if self.paint_the_graph(total_colors, colors, vertex + 1): return True
                colors[vertex] = 0
 
    def graph_colouring(self, number_of_colors):
        colour = [0] * self.vertices
        if self.paint_the_graph(number_of_colors, colour, 0) == None: return False
 
        # Print the solution
        print ("Solution exist and Following are the assigned colours:")
        for index,c in enumerate(colour): print(f"Vertex {index} ---> Color {c - 1}")
        return True
 
# Driver Code
g = Graph(10)
# g.graph = [ [0, 1, 1, 0, 0],
#             [1, 0, 1, 1, 0], 
#             [1, 1, 0, 1, 0], 
#             [0, 1, 1, 0, 1],
#             [0, 0, 0, 1, 0]]

g.graph = [ [0,1,0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0,0,0,0],
            [0,1,0,1,0,0,0,0,0,0],
            [0,0,1,0,1,0,1,0,0,0],
            [0,1,0,1,0,1,0,0,0,0],
            [0,0,0,0,1,0,1,1,0,1],
            [0,0,0,1,0,1,0,1,0,0],
            [0,0,0,0,0,1,1,0,1,0],
            [0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,1,0,0,1,0]]

m = len(g.graph)
g.graph_colouring(m)
 
# This code is contributed by Divyanshu Mehta

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