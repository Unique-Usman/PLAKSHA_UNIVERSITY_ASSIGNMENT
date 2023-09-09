"""To check the password"""


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


if __name__ == "__main__":
    while True:
        password = input("Input the string\n")
        print(checkpass(password))
