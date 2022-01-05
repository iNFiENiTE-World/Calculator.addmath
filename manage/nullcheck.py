from manage import input

def ColumnVecInput (column_vec:tuple) -> tuple:    # Handle null column vector tuple input
    column_vec = column_vec if len(column_vec) != 0 else input.InputColumnVector()
    return column_vec

def CoordinatesXYInput(coordinates:list) -> list:    # Handle null list of tuples of xy coordinate input
    coordinates = coordinates if len(coordinates) != 0 else input.InputXYCoordinates()
    return coordinates

def CoordinateXYInput (coordinate:tuple, coord_name:str) -> tuple:    # Handle null xy coordinate tuple input and take a name as reference to handler
    coordinate = coordinate if len(coordinate) != 0 else input.InputXYCoordinate(coord_name)
    return coordinate

def RatioMNInput (ratio:tuple) -> tuple:    # Handle null ratio mn tuple input
    ratio = ratio if len(ratio) != 0 else input.InputRatioMN()
    return ratio