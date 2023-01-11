class Vertex():
  
    def __init__(self, key):
        self.id = key
        self.visited = False
        self.adj_list = []
    
    def get_id(self):
        return self.id
    
    def set_id(self, newkey):
        self.id = newkey
        
    def addNeighbor(self, new_vert):
        (self.adj_list).append(new_vert)
        
    def __str__(self):
        return f"{str(self.id)} connected to: {str([x.id for x in self.adj_list])}"
      
    def get_adj_list(self):
        return self.adj_list()
    
      
class Graph:
  
    def __init__(self):
        self.Node_List= []
        self.numVertices = 0
        
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.Node_List.append(newVertex)
        return newVertex  
    
    def removeVertex(self, key):
        
        self.numVertices -= 1
        self.vertList[key] = []
    
    def getVertex(self, key):
              
        return self.vertList.get(key)
        
    def getVertices(self):
       for i in range(self.numVertices) :     
        return (self.Node_List)[i].id
      
A=Vertex("Karwar")
B=Vertex("Udupi")
C=Vertex("Mangalore")
D=Vertex("Shimoga")
E=Vertex("Chikmaglur")

print(A.get_id())
print(B.get_id())
print(C.get_id())
print(D.get_id())
print(E.get_id())

mainG = Graph()
mainG.addVertex("Karwar")
mainG.addVertex("Udupi")
mainG.addVertex("Mangalore")
mainG.addVertex("Shimoga")
mainG.addVertex("Chikmaglur")

print(mainG.getVertices())