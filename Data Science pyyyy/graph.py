
graph={}

def add_edge(graph,n1,n2):
    if n1 in graph:
        graph[n1].append(n2)
    else:
        graph[n1]=[n2]
    if n2 in graph:
        graph[n2].append(n1)
    else:
        graph[n2]=[n1]
        
n=int(input("Enter Number of edges vertices : "))
for i in range(n):
    print(f"Edge {n} : ")
    add_edge(graph,input("Enter node1 : "),input("Enter node2 : "))
    
print(graph)