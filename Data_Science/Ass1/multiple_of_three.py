"""To check the if a number is multiple of 3"""


def multiple_of_3(number):
    """check is divisible by three

    Args:
        number (int): number to check
    Returns:
        bool: True if divisible by else False
    """
    sum_of_number = 0

    if number == 0:
        return True

    for i in f"{number}":
        sum_of_number += int(i)

    for i in range(1, sum_of_number + 1):
        if i * 3 == sum_of_number:
            return True
    return False


if __name__ == "__main__":
    print(multiple_of_3(9))
