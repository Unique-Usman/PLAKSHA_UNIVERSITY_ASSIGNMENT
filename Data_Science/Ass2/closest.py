import numpy as np
def closest(harry, ron):
    """find the shorted distance and the time

    Args:
        harry: the first numoy array
        ron: the second numpy array
    Raises:
        ValueError: the numpy array must not be empty
    Returns:
       shortest distance and time
    """

    if harry.size == 0 or ron.size == 0:
        raise ValueError

    size = len(ron) if len(harry) > len(ron) else len(harry)

    shortest_distance =  np.linalg.norm(harry[0] - ron[0])
    time = 0

    for i in range(1, size):
        dist = np.linalg.norm(harry[i] - ron[i])
        if dist < shortest_distance:
            time = i
            shortest_distance = dist
    return shortest_distance, time
