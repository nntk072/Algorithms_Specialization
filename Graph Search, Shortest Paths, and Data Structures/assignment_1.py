# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every
# row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the
# head (recall the graph is directed, and the edges are directed from the first column vertex to the second column
# vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an
# outgoing edge to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs),
# and to run this algorithm on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
# separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500,
# 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm
# finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose
# sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes).  (Note also that
# your answer should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you
# may have to manage memory carefully. The best way to do this depends on your programming language and environment,
# and we strongly suggest that you exchange tips for doing this on the discussion forums.

# Answer
# 434821,968,459,313,211
import sys

sys.setrecursionlimit(300000)
# Coding part
# Variables part
N = 875714
explored = {}  # Nodes explored so far
leader = {}  # Current source vertex for leader
finish = {}  # Finishing times of each node


def init():
    for i in range(1, N + 1):
        explored[i] = False
        finish[i] = 0
        leader[i] = 0


# Function part
def dfs(graph, i):
    global t
    explored[i] = True
    leader[i] = s
    for j in graph[i]:
        if explored[j] == False:
            dfs(graph, j)
    t += 1
    finish[i] = t


def dfs_loop(graph):
    global t, s
    t = 0
    s = 0
    for i in range(len(graph), 0, -1):
        if explored[i] == False:
            s = i
            dfs(graph, i)


# Read the lines in the file
with open("SCC.txt") as f:
    lines = f.readlines()

# Create a dictionary with the nodes and the edges
graph = {}
graph_rev = {}


# Add all from 1 to N to graph
for i in range(1, N + 1):
    graph[i] = []
    graph_rev[i] = []

for line in lines:
    line = line.split()
    if int(line[0]) not in graph:
        graph[int(line[0])] = [int(line[1])]
    else:
        graph[int(line[0])].append(int(line[1]))

    if int(line[1]) not in graph_rev:
        graph_rev[int(line[1])] = [int(line[0])]
    else:
        graph_rev[int(line[1])].append(int(line[0]))

# Algorithm part
init()
dfs_loop(graph_rev)

newGraph = {}
# Using the same format
# for i in range(1, N + 1):
#     temp = []
#     for x in G[i]:
#         temp.append(finish[x])
#     newGraph[finish[i]] = temp

for i in range(1, N + 1):
    newGraph[finish[i]] = []
for i in range(1, N + 1):
    for x in graph[i]:
        newGraph[finish[i]].append(finish[x])

init()
dfs_loop(newGraph)

# statistics
a_list = sorted(leader.values())
# print(leader)
stat = []
pre = 0
for i in range(0, N - 1):
    if a_list[i] != a_list[i + 1]:
        stat.append(i + 1 - pre)
        pre = i + 1
stat.append(N - pre)
final_answer = sorted(stat)
final_answer.reverse()
print(final_answer[0:5])
