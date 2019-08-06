numberOfGroups = 15    # the number of nodes is (numberOfGroups+1)**2-1
numberOfLongConnections = 100   # number of completely random long edges

# network contribution #1: almost isolated communities
numberOfNodes = (numberOfGroups+1)**2 - 1
from random import choice
for i in range(1,numberOfGroups+1):
    square = i**2
    nextSquare = (i+1)**2
    print(i,';',square,sep='')
    for j in range(square,nextSquare):
        group = list(range(square,nextSquare))
        group.remove(j)
        a1 = choice(group)
        group.remove(a1)
        a2 = choice(group)
        group.remove(a2)
        print(j,';',a1,';',a2,sep='')

# network contribution #2: completely random long edges
if numberOfLongConnections > 0:
    allPoints = list(range(1,numberOfNodes))
    for i in range(numberOfLongConnections):
        a = choice(allPoints)
        allPoints.remove(a)
        b = choice(allPoints)
        allPoints.remove(b)
        print(a,';',b,sep='')




