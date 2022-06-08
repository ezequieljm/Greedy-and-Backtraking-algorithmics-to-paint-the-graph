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
        for c in colour: print (c,end=' ')
        return True
 
# Driver Code
g = Graph(5)
g.graph = [ [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0], 
            [1, 1, 0, 1, 0], 
            [0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0],]

m = len(g.graph)
g.graph_colouring(m)
 
# This code is contributed by Divyanshu Mehta