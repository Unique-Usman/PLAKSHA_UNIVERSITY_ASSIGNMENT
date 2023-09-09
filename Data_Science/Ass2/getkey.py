import numpy as np

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

    #to keep track of the index
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
print(getkey("file.txt"))
