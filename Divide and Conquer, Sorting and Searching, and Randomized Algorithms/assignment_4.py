# Download the text file here. (Right click and save link as) The file contains the adjacency list representation of a
# simple undirected graph. There are 40 vertices labeled 1 to 40. The first column in the file represents the vertex
# label, and the particular row (other entries except the first column) tells all the vertices that the vertex is
# adjacent to. So for example, the 6th row looks liks : “"6	155	56	52	120	......”. This just means that the vertex
# with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc.

# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the
# above graph to compute the min cut. (HINT: Note that you’ll have to figure out an implementation of edge
# contractions. Initially, you might want to do this naively, creating a new graph from the old every time there’s an
# edge contraction. But you also think about more efficient implementations.) (WARNING: As per the video lectures,
# please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that
# you ever find).

# Answer: 17

# Format of the file
# 1	37	79	164	155	32	87	39	113	15	18	78	175	140	200	4	160	97	191	100	91	20	69	198	196	
# 2	123	134	10	141	13	12	43	47	3	177	101	179	77	182	117	116	36	103	51	154	162	128	30	

import random
import copy
def min_cut(graph, n):
    while n > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        graph[u].extend(graph[v])
        for x in graph[v]:
            graph[x].remove(v)
            graph[x].append(u)
        while u in graph[u]:
            graph[u].remove(u)
        del graph[v]
        n -= 1
    return len(graph[list(graph.keys())[0]])

def main():
    graph = {}
    with open('kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph[int(line[0])] = [int(x) for x in line[1:]]
    n = len(graph)
    min_cuts = min_cut(copy.deepcopy(graph), n)
    for i in range(100):
        min_cuts = min(min_cuts, min_cut(copy.deepcopy(graph), n))
    print(min_cuts)
if __name__ == '__main__':
    main()