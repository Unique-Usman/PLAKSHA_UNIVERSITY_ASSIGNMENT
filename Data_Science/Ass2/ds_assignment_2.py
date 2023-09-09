"""Datascience assignment 2"""

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

    # to keep track of the index
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


"""
The llm i used is chatgpt
Prompt:
    solve

MS Dhoni is a batsman who uses data for analyzing his performance.
After a cricket match he wants to know against which bowler he scored
the maximum. Write a function maxbowler(filename) that returns
the name of the bowler against whom he scored the maximum in a
single over. Your function should check that the number of bowler
names matches the number of rows of runs, and raise a ValueError
otherwise. It should also ignore any leading or trailing white spaces in
a line, and empty lines (lines with no character or only whitespaces).
(a) Input: Path of a text file (filename) with a list of bowlers (one in
each line) in the order in which they bowled followed by the runs
MS Dhoni scored, one row for each over in the same sequence as
the bowlers, with 6 numbers for the runs off the 6 balls in that
over (separated by space). Ignore no-balls and wides.
(b) Output: Name of the bowler against whom MS Dhoni scored the
maximum.
(c) Example 1:
• Input file: runs.txt containing the following text
Malinga
Bumrah
Chahar
Tahir
Malinga
Chahar
0 0 0 1 2 0
1 0 1 1 4 0
4 0 1 1 6 4
0 1 1 1 1 0
6 6 4 0 4 0
1 4 2 2 1 0
• Returns:
Malinga
Ans:
    def maxbowler(filename):
    try:
        # Read the file contents
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove leading and trailing whitespaces and empty lines
        lines = [line.strip() for line in lines if line.strip()]

        # Check if the number of bowlers matches the number of rows of runs
        if len(lines) % 2 != 0:
            raise ValueError("Number of bowlers and runs don't match")

        # Initialize a dictionary to store runs scored against each bowler
        bowler_runs = {}

        for i in range(0, len(lines), 2):
            bowler = lines[i]
            runs = list(map(int, lines[i + 1].split()))

            # Calculate the total runs scored in that over
            total_runs = sum(runs)

            # Update the total runs scored against the bowler
            if bowler in bowler_runs:
                bowler_runs[bowler] += total_runs
            else:
                bowler_runs[bowler] = total_runs

        # Find the bowler with the maximum runs scored against them
        max_bowler = max(bowler_runs, key=bowler_runs.get)

        return max_bowler

    except FileNotFoundError:
        return "File not found"
    except ValueError as e:
        return str(e)

# Example usage:
filename = 'runs.txt'
result = maxbowler(filename)
print("Bowler with the maximum runs scored against:", result)
Critique:
    The llm does not doc string it ut functions, though it added comment. Another thing I noticed is that it was handle all possible error which is good but, I still believe
    it is not necessary as it was not asked in the question.
"""


def binarize(im, thresh):
    """function to binarize an image

    Args:
        im: image to be binarize
        thresh: the threshhold value
    Returns:
        the result of binarize
    """
    h, w, c = im.shape
    ans = np.zeros([h, w], dtype="int32")
    for i in range(h):
        for j in range(w):
            ans[i, j] = 0 if thresh > np.sum(im[i, j]) / c else 1
    return ans

"""
Prompt:
    solve
. Ankit likes to play with digital photos. He loads an RGB photo as a
numpy array of dimensions (H x W x C) where H is the height and
W is the width of the image in pixels and C is 3, the number of
color channels. He wants to binarize the image by first converting
it into gray-scale by taking the mean of the three color values for each
pixel, and then thresholding this gray-scale image. Write a function
binarize(im, thresh) that takes an H x W x C numpy array im and
a threshold value thresh and returns a numpy array of dimension H
x W with a 0 entry for the pixels whose average value is equal or less
4
than thresh, and a 1 entry for the pixels with average value above
thresh.
(a) Example
• Input arguments
im = np.array([
[
[172, 36, 146],
[215, 122, 48]
],
[
[126, 179, 104],
[251, 133, 75]
]
])
thresh = 128.0
• Returns
np.array([
[0, 1],
[1, 1]
])

Answer:import numpy as np

def binarize(im, thresh):
     Calculate the grayscale image by taking the mean of the three color channels.
    grayscale_im = np.mean(im, axis=2)

    Apply the threshold to create the binary image.
    binary_im = (grayscale_im > thresh).astype(np.uint8)

    return binary_im

    Example usage:
im = np.array([
    [
        [172, 36, 146],
        [215, 122, 48]
    ],
    [
        [126, 179, 104],
        [251, 133, 75]
    ]
])

thresh = 128.0
binary_image = binarize(im, thresh)
print(binary_image)

Critique:
    I love whwt the answer by chatgpt, it used some numpy inbuilt function which was really great. I also added docs which chatgpt does not add
"""


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

    shortest_distance = np.linalg.norm(harry[0] - ron[0])
    time = 0

    for i in range(1, size):
        dist = np.linalg.norm(harry[i] - ron[i])
        if dist < shortest_distance:
            time = i
            shortest_distance = dist
    return shortest_distance, time
"""
Prompt:
    solve
Quidditch is a sport that witches and wizards play riding on flying
broomsticks. Harry and Ron have got new broomsticks that are connected to the IoT and log their positions relative to the tip of the
Gryffindor tower (one of the three tallest towers of the Hogwarts Castle) every second from the start of the game. Harry and Ron want to
analyze their games and find out the closest they came to each other
during a game. Help them by writing a function closest(harry,
3
ron) that takes two numpy arrays, each with 3 columns for x, y,
and z coordinates of their broomsticks, and returns (shortest_dist,
time) where shortest_dist is their shortest distance, and time the
earliest time in the game (in seconds, starting at 0 at the start of
the game) when they reached this distance from each other. Note
that they start at the same time, but there is no guarantee that they
would stay in the game for the same time, so the arrays may be of
different lengths. Also, if any of them did not participate in a match,
the position array would be empty, and your function should raise a
ValueError in such cases.
(a) Example
• Input arguments
harry = np.array([
[ 93, 7, 103],
[176, 102, 140],
[142, 156, 156],
[158, 127, 144],
[ 32, 24, 92]])
ron = np.array([
[112, 115, 189],
[106, 3, 110],
[144, 133, 34],
[ 10, 37, 189],
[165, 132, 40],
[181, 92, 45]])
• Returns
(124.16521251944927, 2)
Answer:
    import numpy as np

def closest(harry, ron):
    # Check if either Harry's or Ron's data is empty
    if len(harry) == 0 or len(ron) == 0:
        raise ValueError("Both Harry and Ron must participate in the match.")

    shortest_dist = float('inf')  # Initialize shortest distance as positive infinity
    time = 0  # Initialize time at 0

    # Loop through Harry's and Ron's positions at each time step
    for i in range(len(harry)):
        for j in range(len(ron)):
            # Calculate the Euclidean distance between their positions at the current time step
            dist = np.linalg.norm(harry[i] - ron[j])

            # If the calculated distance is shorter than the current shortest distance
            if dist < shortest_dist:
                shortest_dist = dist
                time = max(i, j)  # Update the time to the maximum of the current time steps

    return shortest_dist, time

# Example usage:
harry = np.array([
    [ 93, 7, 103],
    [176, 102, 140],
    [142, 156, 156],
    [158, 127, 144],
    [ 32, 24, 92]
])

ron = np.array([
    [112, 115, 189],
    [106, 3, 110],
    [144, 133, 34],
    [ 10, 37, 189],
    [165, 132, 40],
    [181, 92, 45]
])

shortest_distance, time = closest(harry, ron)
print("Shortest Distance:", shortest_distance)
print("Time at Closest Distance:", time)

Critique:
    Chatgpt only add comment but, i add doc string which is useful for python other developer, but,
    I would really it's answer is also looking good
"""

def getkey(filename):
    """decrypt the message

    Args:
        filename: the file to be read
    Raises:
        ValueError: if size does not match or if an element is not int
    Returns:
        key after decryption
    """
    # to store each line of the file
    nums = []

    # dimension of the file
    dim = 0

    # to keep track of the index
    count = 0

    # opening the file
    with open(filename, "r") as fd:
        for file in fd.readlines():
            if count == 0:
                dim = file.strip()
                count += 1
                if not dim.isdigit():
                    raise ValueError
                continue
            if not file.strip():
                continue
            nums.append(file.strip().split(" "))
            if not len(file.strip().split(" ")) == int(dim):
                raise ValueError
    nums = np.array(nums)
    for line in nums:
        for ele in line:
            if not ele.isdigit():
                raise ValueError
    nums = np.array([[int(col) for col in row] for row in nums])
    return np.sum(np.diag(nums))
"""
Prompt:
    SOLVE
2. Ankit created a decryption program that uses a key to decrypt security
codes. A spy organization sends the decryption key embedded in an
N x N matrix of integers, such that the sum of the diagonal elements
is the key. Ankit has dumped the data in a text file whose first line
contains the dimensions of the N x N matrix, and the lines following
it contain the elements of the matrix, one row per line, separated by
spaces. Write a function getkey(filename) that takes the path of
the file as a string, reads the file, computes the key and returns it.
If the number of rows or columns do not match the number specified
in the first line, it should raise a ValueError. It should also raise a
ValueError if any of the elements is a non-integer. Again, it should
ignore empty lines and leading or trailing white spaces.
(a) Example 1
• Input file contains
4
1 2 3 4
4 5 6 7
6 8 4 3
8 1 4 7
• Returns
17
(b) Example 2
• Input file contains
2
2 4
3 7
• Returns
9
Answer:
    def getkey(filename):
    try:
        # Read the file contents
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove leading and trailing whitespace and empty lines
        lines = [line.strip() for line in lines if line.strip()]

        # Check if the first line contains the matrix dimensions
        if len(lines) < 2:
            raise ValueError("Invalid file format: Missing matrix dimensions or data.")

        n = int(lines[0])  # Extract the matrix dimensions
        lines = lines[1:]  # Remove the first line

        # Check if the number of rows matches the specified dimensions
        if len(lines) != n:
            raise ValueError("Invalid number of rows in the matrix.")

        # Initialize the key
        key = 0

        # Parse the matrix elements and calculate the key
        for line in lines:
            elements = line.split()

            # Check if the number of columns matches the specified dimensions
            if len(elements) != n:
                raise ValueError("Invalid number of columns in the matrix.")

            for element in elements:
                try:
                    # Convert element to an integer and add it to the key
                    key += int(element)
                except ValueError:
                    raise ValueError("Non-integer element found in the matrix.")

        return key

    except FileNotFoundError:
        raise ValueError("File not found.")
    except ValueError as e:
        raise e

# Example usage:
filename = 'matrix.txt'
try:
    key = getkey(filename)
    print("Decryption Key:", key)
except ValueError as e:
    print(str(e))
Critique:
    From all what I noticed the llm just solve a question in the best way it can solve it without when no much information is given to it. It handled errror so well. I would probably say llm like chatgpt is good for generating small code.
    Also, the llm does not add doc but, I tell it do so, it add
"""



if __name__ == "__main__":
    pass

