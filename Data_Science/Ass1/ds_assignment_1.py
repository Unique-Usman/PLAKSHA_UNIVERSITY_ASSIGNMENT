

def ankit_max(marks_dict):
    """Check ankit max which is second highest num

    Args:
        marks_dict (dict): dict of the form
    Returns:
        None if there is none else name of the sec highest num
    """

    if len(marks_dict) == 0:
        return None
    mark_store = list(marks_dict.items())

    # check if everthing is the same and return None
    check = list(marks_dict.values()).count(mark_store[0][1])
    if check == len(mark_store):
        return None
    # find the first max
    max_element = max(mark_store, key=lambda mark: mark[1])
    # remove the first max
    mark_store.remove(max_element)
    # then find the new max which will be the second max
    max_element = max(mark_store, key=lambda mark: mark[1])
    return (max_element[0])


def attendance(record):
    """Check attendance of a person

    Args:
        record (str): string of the attendance
    Returns:
        tuple: (decision, percentage)
    """
    # changing the record to list
    record = record.split(" ")
    # counting the number of Absent
    num_of_a = record.count("A")
    # counting the number of Present
    num_of_p = record.count("P")
    # finding the percentage of present
    percentage = num_of_p / (num_of_a + num_of_p)
    # finding the decision based on the percentage
    decision = "not suspended" if percentage >= 0.7 else "suspended"
    return (decision, percentage)


def multiple_of_3(number):
    """check is divisible by three

    Args:
        number (int): number to check
    Returns:
        bool: True if divisible by else False
    """
    sum_of_number = 0

    # check if number is 0
    if number == 0:
        return True

    #sum each digit of the number
    for i in f"{number}":
        sum_of_number += int(i)

    #then check if it multiple of 3
    for i in range(1, sum_of_number + 1):
        if i * 3 == sum_of_number:
            return True
    return False


def checkpass(password):
    """This function check the password strength

    Args:
        password (str): It accepts the password
    Returns:
        bool: False if weak else True
    """

    result = True
    # checking the length of the password
    if len(password) < 8:
        result = False
    # check if it has special character
    if password.isalnum():
        result = False
    # checking it has digit
    if not any(char.isdigit() for char in password):
        result = False
    # checking if it has any uppercase letter
    if not any(char.isupper() for char in password):
        result = False
    # checking if it has any alphabet letter
    if not any(char.isalpha() for char in password):
        result = False
    # checking if it has any lowercase letter
    if not any(char.islower() for char in password):
        result = False
    return (result)


def deduplicate(arg):
    """Remove all the adj rep char in arg

    Args:
        arg (int): string to remove the adj rep char in
    Returns:
        str: string with rep char removed
    """

    # check if arg is empty
    if not arg:
        return ""

    result = "" + arg[0]

    prev = arg[0]

    # loop through and unique adj to the result
    for i in arg:
        if i == prev:
            continue
        prev = i
        result += i
    return result


if __name__ == "__main__":
    pass



"""
I query ChatGPT for solution to these problems

Problem 1:
    I solved the question without importing anything but, ChatGPT
    imported re which is regex module. Chatgpt also only commented on the
    code it does not write documentation for the function and I do
...
Problem 2:
    ChatGPT did similar thing which I did, it uses list but it uses if
    condition and I did not use it, it also did not add documentatiion to the
    function and I did
...
Problem 3:
    The approach it uses is different, it uses sort function and
    I only used max to find the first element then remove the element from
    and now find the max element which gives the second largest element
    It also did not add documentation and I did
Problem 4:
    ChatGPT still uses modulo and in its program but I did not use
    as instructed in the question. It also did not add documentation
    and I did
Problem 5:
    The approch seems similar but the data structure used by chatgpt is
    different from mine, it used list and I used string.
    It also did not add documentation and I did
"""
