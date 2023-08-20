# Luiza Santos - Data Engineer - Intern
# Problem 1.b: Write a function that, given a Polygon's path of points, 
# returns a reduced list that defines the same Polygon. 
# (Notice that all the points in the set are adjacent). 
# Choose the language you want to answer this question, 
# and comment on the code explaining each step. 
# Don’t worry about syntaxes.


def reduced_polygon(points_list):
    """
    Find the points that don't change the polygon which are the ones in the same line that another 2 points could make,
    aka, useless points and return a clean list
    A point will be in the same line as another line if either:
        the x values of the points before and after are the same as itself
        the y values of the points before and after are the same as itself

    Parameters: 
    points: list of tuples, where the first value of each tuple is the x value and the second value of each tuple is the y values

    Returns: 
    list of tuples without the useless points

    Examples:
    sample_points_1 = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 3), (3,2), (2,2), (2,1), (1,1)] 
    # useless points (1,2), (3,3)
    # reduced_polygon(sample_points_1) = [(1, 1), (1, 3), (2, 3), (2, 4), (3, 4), (3,2), (2,2), (2,1), (1,1)] 
    sample_points_2 = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4,4), (4, 3), (4,2), (3,2), (2,2), (2,1), (1,1)] 
    # useless points (1, 2), (3, 4), (4, 3), (3, 2)
    # reduced_polygon(sample_points_2) = [(1, 1), (1, 3), (2, 3), (2, 4), (4, 4), (4, 2), (2, 2), (2, 1), (1, 1)]
    """
    # create an empty list to store useless_points
    useless_points = []
    # loop over all items except for first and last since polygons start and end in the same place to close the polygon
    for i in range(1,len(points_list)-1):
        # check x [0] and y [1] values
        for j in range(2):
            # check if both the point before and the point after are the same as itself
            if (points_list[i][j] == points_list[i-1][j]) and (points_list[i][j] == points_list[i+1][j]):
                # if that's true, then it's a useless point, so append to the useless_points list
                useless_points.append(points_list[i])
    # filter points_list to contain only the ones that are not useless
    return [point for point in points_list if point not in useless_points]

sample_points_1 = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 3), (3,2), (2,2), (2,1), (1,1)] # answer (1,2), (3,3)
sample_points_2 = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4,4), (4, 3), (4,2), (3,2), (2,2), (2,1), (1,1)] # answer (1, 2), (3, 4), (4, 3), (3, 2)

print(reduced_polygon(sample_points_1))
print(reduced_polygon(sample_points_2))