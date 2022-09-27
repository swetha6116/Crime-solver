n = int(input("Enter the number of suspects: "))
suspects = [i for i in range(1, n + 1)]
# for i in range(n):
#     suspects.append(input("Enter the name of suspect {}: ".format(i + 1)))
print(suspects)
in_edges = [0 for i in range(n)]
# enter 0 if he is saying not me
for i in range(n):
    temp = int(input(f"Who is {suspects[i]} blamming: "))
    if temp == 0:
        for j in range(n):
            if j == i:
                continue
            in_edges[j] += 1
        continue
    in_edges[temp - 1] += 1

t = int(input("How many people are telling the truth: "))
print(in_edges)
for i in range(len(in_edges)):
    if in_edges[i] == t:
        print(f"{i + 1} is the theif")
