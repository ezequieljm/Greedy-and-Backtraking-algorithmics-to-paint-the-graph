import os
from GraphColouringBacktrakingObject import BacktrakingGraph
from GraphColouringGreedyObject import GreedyGraph

clearScreen = lambda: os.system("clear") if os.name == "posix" else os.system("cls")

def main():
    clearScreen()
    graph1 = [  [0,1,0,0,0,0,0,0,0,0],
                [1,0,1,0,1,0,0,0,0,0],
                [0,1,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0],
                [0,1,0,1,0,1,0,0,0,0],
                [0,0,0,0,1,0,1,1,0,1],
                [0,0,0,1,0,1,0,1,0,0],
                [0,0,0,0,0,1,1,0,1,0],
                [0,0,0,0,0,0,0,1,0,1],
                [0,0,0,0,0,1,0,0,1,0]]


    graph2 = [  [0,1,0,0,0,0,0,0,0,0],
                [1,0,1,0,1,0,0,0,0,0],
                [0,1,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0],
                [0,1,0,1,0,1,0,0,0,0],
                [0,0,0,0,1,0,1,1,0,1],
                [0,0,0,1,0,1,0,1,0,0],
                [0,0,0,0,0,1,1,0,1,1],
                [0,0,0,0,0,0,0,1,0,1],
                [0,0,0,0,0,1,0,1,1,0]]


    graph3= [[0,1,1,1,1],
             [1,0,1,1,1],
             [1,1,0,1,1],
             [1,1,1,0,1],
             [1,1,1,1,0]]

    print (f"Greedy Algorithmic\n")

    greedyGraph = GreedyGraph(graph3)
    greedyGraph.initAdjacentVector()
    greedyGraph.greedyColoring()
    greedyGraph.printPaintedGraph()

    print (f"\nBacktraking Algorithmic\n")

    backGraph = BacktrakingGraph(graph3)
    backGraph.graphColouring()
    backGraph.printPaintedGraph()



# Driver Code
if __name__ == '__main__': 
    main()