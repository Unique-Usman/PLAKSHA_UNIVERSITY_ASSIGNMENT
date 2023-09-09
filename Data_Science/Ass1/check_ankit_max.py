"""This check ankit maximum number"""


def ankit_max(marks_dict):
    """Check ankit max which is second highest num

    Args:
        marks_dict (dict): dict of the form
    Returns:
        None if there is none else name of the sec highest num
    """

    mark_store = list(marks_dict.items())

    # check if everthing is the same
    check = list(marks_dict.values()).count(mark_store[0][1])
    if check == len(mark_store):
        return None

    max_element = max(mark_store, key=lambda mark: mark[1])
    mark_store.remove(max_element)
    max_element = max(mark_store, key=lambda mark: mark[1])
    return (max_element[0])

if __name__ == "__main__":
    print(ankit_max({'Xavier': 25, 'Ibrahim': 25, 'Yatin': 25,
'Sami': 25, 'Takahashi': 25}))
