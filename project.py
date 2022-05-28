from mimetypes import init

import collections

#check comment

# BFS algorithm
def bfs(graph, root, value):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        it = vertex.get_items()
        
        if it != 0:
            if value in it:
                print("Shop found")
                vertex.show_all()
        # print(vertex.show_all() , "\n")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

class node():
    
    def __init__(self,shopname,cost, items):
        self.shopname = shopname
        self.cost = cost
        self.items = items
    
    def show_all(self):
        print(self.shopname)
        print(self.cost)
        print(self.items)
    
    def get_items(self):
        return self.items
    
    def get_cost(self):
        return self.cost
    def get_shopname(self):
        return self.shopname

n1 = node("Source",0,0)
n2 = node("Croma",12,["mobile","IPAD"],)
n5 = node("Vasanth & Co",22,["Television","Washing machine"])
n3 = node("Decathlon",52,["Sports Shoe","Football"])
n4 = node("Reliance Trends",32,["Shirt","Pants"])

graph = {n1:[n2,n5],n2:[n1,n3],n3:[n2],n4:[n5],n5:[n1,n4]}
v = "Football"
bfs(graph,n1,v)
