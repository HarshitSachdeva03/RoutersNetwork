def swap(index1, index2, HeapStorage): #to swap values in the heap used
    HeapStorage[index1], HeapStorage[index2] = HeapStorage[index2], HeapStorage[index1]


def heapup(index, HeapStorage): #element inserted at the last is heaped up to restore heap property
    if (index < len(HeapStorage)):
        while (index > 0):
            parent = (index-1)//2
            if (parent >= 0):
                if (HeapStorage[index][1] > HeapStorage[parent][1]):
                    swap(parent, index, HeapStorage)
                    index = parent
                else:
                    return
        return
    return


def maxHeapify(index, HeapStorage): #after removing the top(maximum) element, heap property has to be restored
    size = len(HeapStorage)
    while (index < size):
        u = index
        left1 = 2*index+1
        right1 = 2*index+2
        if (left1 < size and (HeapStorage[left1][1] > HeapStorage[index][1])):
            index = left1
        if (right1 < size and (HeapStorage[right1][1] > HeapStorage[index][1])):
            index = right1
        if (index != u):
            swap(u, index, HeapStorage)
        else:
            return

def extractMax(HeapStorage): #returns and removes the topmost element of heap
    data = HeapStorage[0]
    HeapStorage[0] = HeapStorage[-1]
    HeapStorage.pop()
    maxHeapify(0, HeapStorage)
    return data

path=[] #stores the route for a path
def getroute(parent, vertex, target): #to get the route of the suitable path.
    if (vertex == -1):
        return  #if we encounter default value of vertex
    getroute(parent, parent[vertex], target)
    path.append(vertex)

def findMaxCapacity(n, links, s, t):  #required function
    path.clear() 
    HeapStorage = [] #my heap list
    capacities = [] #to store the max capacity for a path from source to any other kth vertex at capacities[k]
    adjacent = [] #stores the adjacent vertices for kth point at adjacent[k] as a 2-D list along with the capacity of the edge in between
    parent = [] 
    for i in range(n):
        adjacent.append([])
        capacities.append(float('-inf'))
        parent.append(-1)
    for i in range(len(links)):
        u = links[i][0]
        v = links[i][1]
        c = links[i][2]
        adjacent[u].append([v, c])
        adjacent[v].append([u, c])
    
    HeapStorage.append([s, float('-inf')])
    capacities[s] = float('inf')

    while (HeapStorage[0][0]!=t and len(HeapStorage) > 0): #insert adjacent vertices in a heap and then go along the path havinh max capacity
        new_src = extractMax(HeapStorage)

        for element in adjacent[new_src[0]]:
            packet = max(min(capacities[new_src[0]], element[1]), capacities[element[0]]) #this is the main condition for updation of the capacity of a vertex

            if (packet > capacities[element[0]]):
                capacities[element[0]]=packet
                parent[element[0]]=new_src[0]
                HeapStorage.append([element[0],packet])
                heapup(len(HeapStorage)-1,HeapStorage)
    
    getroute(parent,t,t)
    
    return([capacities[t],path])

#time complexity is O(mlogm) as we are adding elements equal to the number of edges in the heap(actually about twice of that) and
#extracting one by one which takes O(logm) time.