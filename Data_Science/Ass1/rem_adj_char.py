"""Removes Adjacent Character"""


def deduplicate(arg):
    """Remove all the adj rep char in arg

    Args:
        arg (int): string to remove the adj rep char in
    Returns:
        str: string with rep char removed
    """

    if not arg:
        return ""
    result = "" + arg[0]

    prev = arg[0]

    for i in arg:
        if i == prev:
            continue
        prev = i
        result += i
    return result

if __name__ == "__main__":
    print(deduplicate("blahblahblah"))
