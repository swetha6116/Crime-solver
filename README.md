# Crime-solver
To solve a crime scenario using graph algorithms.

Problem Statement:

There are n number of suspects. Each suspects either blames one of the other suspects or says "it's not me". But only m among the n are telling the truth. Who is the criminal?

Solution:

This is solved using a graph algorithm. Draw a directed graph for the scenario directing a suspect to the suspect he blames. Now count the number of incoming edges of each suspect. A node can have m number of edges incoming to it only if m people are telling truth hence that node which has m incoming edges is the criminal.

Example 1:
![image](https://user-images.githubusercontent.com/89096691/193455248-022f6a69-39b8-43a4-9b1e-fafb82b91a61.png)

Give the inputs:
![image](https://user-images.githubusercontent.com/89096691/193455530-77862227-8677-44af-bc63-b4a91930424c.png)

If there are 3 suspects and they make these respective claims. But only 1 is telling the truth among them.
The graph would look like this.
<img width="639" alt="Screenshot 2022-10-02 at 6 29 24 PM" src="https://user-images.githubusercontent.com/89096691/193455323-aaf5a351-d59e-409b-bec6-d9fce5c281a9.png">

Since person 3 has exactly 1 incoming edge and this is possible only if only 1 suspect is telling the truth, 3 is the criminal.

Example 2:
![image](https://user-images.githubusercontent.com/89096691/193455398-1b19f046-4094-4de2-9608-8cc45695ffb2.png)

Give the inputs:

<img width="666" alt="Screenshot 2022-10-02 at 6 20 34 PM" src="https://user-images.githubusercontent.com/89096691/193455556-13e743b8-9f10-4389-bfb7-9bc1f54ebfa0.png">

If there are 4 suspects and they make these respective claims. But only 3 are telling the truth among them.
The graph would look like this.

<img width="638" alt="Screenshot 2022-10-02 at 6 20 07 PM" src="https://user-images.githubusercontent.com/89096691/193455412-4fa0d91c-a278-4649-a356-b499ab104c23.png">

Since person 2 has exactly 3 incoming edges and this is possible only if 3 suspects are telling the truth, 2 is the criminal.

Modules used to display the graph in python are networkx and matplotlib.pyplot
