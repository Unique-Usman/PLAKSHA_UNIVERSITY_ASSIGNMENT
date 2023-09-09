import numpy as np

def maxbowler(filename):
    """find max bowler in file

    Args:
        filename: the file to be read
    Raises:
        ValueError: num of bowler should match the run
    Returns:
        the bowler with max score
    """
    # name of the bowler to store the array
    name = []
    # score to store the number of run per each bowler
    score = []
    # max_t to store the name of the max run and it value
    max_t = [0, 0]

    #to keep track of the index
    count = 0

    # opening the file
    with open(filename, "r") as fd:
        for file in fd.readlines():
            file = file.strip()
            if not file:
                continue
            if file.isalpha():
                name.append(file)
            else:
                score.append(file.split(" "))
    # storing the list in numpy array
    name = np.array(name)
    score = np.array(score)

    # verifying if the num of size match the bowlers
    if score.shape[0] != len(name):
        raise ValueError

    score = np.array([[int(col) for col in row] for row in score])

    # finding the max score and storing it index
    for goals in score:
        tmp_max = np.sum(goals)
        if tmp_max > max_t[0]:
            max_t[0] = tmp_max
            max_t[1] = count
        count += 1
    return (name[max_t[1]])


print(maxbowler("runs.txt"))
