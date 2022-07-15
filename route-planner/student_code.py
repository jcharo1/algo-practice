
class Intersections:
    def __init__(self,name,coordinates,roads):
        self.name  = name
        self.coordinates = coordinates
        self.x_coordinates = coordinates[0]
        self.y_coordinates = coordinates[1]


class Map_10:
    def __init__(self,instersections,roads):
        self.intersections = intersections
        self.roads = roads

from math import sqrt
#Helper function to find Euclidean Distance Between Two Points on the map
def dist(a,b):

    x = b[0]-a[0]
    y = b[1]-a[1]
    return sqrt(x*x + y*y)

def shortest_path(map,start,goal):
    print("shortest path called")
    #  # Sets are faster for lookups
    openset = set()

    camefrom = set()# Set to keep track of visited nodes.
    gscore= {}
    gscore[start]= 0

    fscore={}

    fscore[start]= dist(start,goal)




    while openset:

        current_node = openset[start]
        # if current_node == goal:
        #     return reconstruct_path(cameFrom, current)
        for neighbors in map.roads[current_node]:
            print(neighbors)
    
    return



intersections={0: [0.7798606835438107, 0.6922727646627362],
 1: [0.7647837074641568, 0.3252670836724646],
 2: [0.7155217893995438, 0.20026498027300055],
 3: [0.7076566826610747, 0.3278339270610988],
 4: [0.8325506249953353, 0.02310946309985762],
 5: [0.49016747075266875, 0.5464878695400415],
 6: [0.8820353070895344, 0.6791919587749445],
 7: [0.46247219371675075, 0.6258061621642713],
 8: [0.11622158839385677, 0.11236327488812581],
 9: [0.1285377678230034, 0.3285840695698353]}

roads=[[7, 6, 5],
 [4, 3, 2],
 [4, 3, 1],
 [5, 4, 1, 2],
 [1, 2, 3],
 [7, 0, 3],
 [0],
 [0, 5],
 [9],
 [8]]


map = Map_10(intersections,roads)

print(map.intersections)
print(map.roads)


for name , coordinates in map.intersections.items():
    








