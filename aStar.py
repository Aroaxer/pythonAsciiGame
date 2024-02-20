

# A* Algorithm
# All points are (x, y) tuples

# Supporting functions
def reconstPath(route, current):
    fullPath = [current]
    while current in route.keys():
        current = route[current]
        fullPath.append(current)
    return fullPath

def heurDist(start, end):
    return (abs(start[0] - end[0]) + abs(start[1] - end[1]))

def getNeighbors(node, gridX, gridY, game):
    neighbors = []
    if node[0] < gridX and not isSpotOccupied(game, node[0] + 1, node[1]):
        neighbors.append((node[0] + 1, node[1]))
    if node[1] < gridY and not isSpotOccupied(game, node[0], node[1] + 1):
        neighbors.append((node[0], node[1] + 1))
    if node[0] > 1 and not isSpotOccupied(game, node[0] - 1, node[1]):
        neighbors.append((node[0] - 1, node[1]))
    if node[1] > 1 and not isSpotOccupied(game, node[0], node[1] - 1):
        neighbors.append((node[0], node[1] - 1))
    return neighbors

def isSpotOccupied(game, x, y):
    isOccupied = False
    for object in game.allObjects:
        if object.x == x and object.y == y:
            isOccupied = True
            break
    return isOccupied

    
# The main algorithm
# 'entity' is the one using the route, for stopping when in range
# 'grid' is for not pathing off the grid, (width, height) tuple
def getRoute(start, goal, entity, game):
    openSet = [start]
    route = {}
    gScore = {start : 0}
    fScore = {start : heurDist(start, goal)}

    while len(openSet) > 0:

        current = openSet[0]
        for node in openSet:
            try:
                if fScore[node] < fScore[current]:
                    current = node
            except Exception:
                pass
        if max(abs(current[0] - goal[0]), abs(current[1] - goal[1])) <= entity.preferredDist:
            return reconstPath(route, current)
        
        
        openSet.remove(current)
        for neighbor in getNeighbors(current, game.encounter.width, game.encounter.height, game):
            tentaGScore = gScore[current] + 1
            try:
                if tentaGScore < gScore[neighbor]:
                    route[neighbor] = current
                    gScore[neighbor] = tentaGScore
                    fScore[neighbor] = tentaGScore + heurDist(neighbor, goal)
                    if not neighbor in openSet:
                        openSet.append(neighbor)
            except Exception:
                route[neighbor] = current
                gScore[neighbor] = tentaGScore
                fScore[neighbor] = tentaGScore + heurDist(neighbor, goal)
                if not (neighbor in openSet):
                    openSet.append(neighbor)

    return "No Path"

