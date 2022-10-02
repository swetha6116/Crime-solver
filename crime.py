import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter the number of suspects: "))
suspects = [i for i in range(1, n + 1)]
print(f"The suspects' names are : {suspects}")
in_edges = [0 for i in range(n)]
G = nx.DiGraph()

# enter 0 if he is saying "not me"
print("Enter who each suspect is blamming, enter 0 if he says \"not me\" ")
for i in range(n):
    temp = int(input(f"Who is {suspects[i]} blamming: "))
    if temp == 0:
        for j in range(n):
            if j == i:
                continue
            G.add_edges_from([(i+1, j+1)])
            in_edges[j] += 1
        continue
    G.add_edges_from([(i+1, temp)])
    in_edges[temp - 1] += 1

t = int(input("How many people are telling the truth: "))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()

for i in range(len(in_edges)):
    if in_edges[i] == t:
        print(f"{i + 1} is the theif")
