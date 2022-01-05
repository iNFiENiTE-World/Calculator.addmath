from manage import nullcheck

def ShoelaceAlgorithm(coordinates:list=[]) -> float:    # Find area of shape using coordinates of its vertices, return float area, A
    
    # Manage null input
    coordinates = nullcheck.CoordinatesXYInput(coordinates)
    
    # Completing the lace node
    coordinates.append(coordinates[0])
    
    ITEM_COUNT = len(coordinates)

    def NodeProduct (X_index:int, Y_index:int) -> float:    # Calculate product of two nodes
        x = coordinates[X_index][0]
        y = coordinates[Y_index][1]
        print(f"X: {x}, Y: {y}, XY: {x*y}")
        return x*y
    
    first = 0
    second = 0 
    
    # Tying the shoelace
    for j in range(0, ITEM_COUNT - 1):
        first += NodeProduct(j, j + 1) # First lace
        second += NodeProduct(j + 1, j) # Second lace
    
    print(f"First lace: {first}, Second lace: {second}")
    
    # Shoelace result
    area = abs(first - second) / 2
    
    return area


def DivisorOfLineSegment (pointA:tuple=(), pointB:tuple=(), ratioMN:tuple=()) -> tuple:    # Find point that divides a line segment using coordinates of two connecting points and ratio of divider, return a tuple of xy coordinate, (x,y)
    
    # Manage null input
    pointA = nullcheck.CoordinateXYInput(pointA, "A")
    pointB = nullcheck.CoordinateXYInput(pointB, "B")
    ratioMN = nullcheck.RatioMNInput(ratioMN)
    
    # Variable assignment
    m = ratioMN[0]; n = ratioMN[1]; x1 = pointA[0]; x2 = pointB[0]; y1 = pointA[1]; y2 = pointB[1]
    
    # Calculation
    x = (m * x2 + n * x1) / (m + n)
    y = (m * y2 + n * y1) / (m + n)
    
    # Output
    return (x,y)
