def InputXYCoordinates (coordinates:list=[]) -> list:    # Prompt float inputs from user, return a list of tuples containing xy coordinates, [(x1,y1),(x2,y2),...]

    item_count = len(coordinates)
        
    x = input(f"Point {item_count+1} x: ")
    y = input(f"Point {item_count+1} y: ")
        
    if (x and y) is not "q":
        coordinate = (float(x),float(y))
        coordinates.append(coordinate)
        InputXYCoordinates(coordinates)

    return coordinates

def InputXYCoordinate (ref_name) -> tuple:    # Return a tuple containing xy coordinate, (x,y)
    get = Input_TwoSingle(f"Point {ref_name} x", f"Point {ref_name} y")
    return (get[0],get[1])

def InputColumnVector() -> tuple:    # Return a tuple containing column vector, (x-vector,y-vector)
    get = Input_TwoSingle("x-vector", "y-vector")
    return (get[0],get[1])

def InputRatioMN () -> tuple:    # Return a tuple containing ratio mn, (m,n)
    get = Input_TwoSingle("m", "n")
    return (get[0],get[1])

def Input_TwoSingle (keyword1, keyword2) -> list:    # Prompt two float inputs from user, return a list containing the two input value, (val1,val2)
    x = float(input(f"{keyword1}: "))
    y = float(input(f"{keyword2}: "))
    return [x,y]
