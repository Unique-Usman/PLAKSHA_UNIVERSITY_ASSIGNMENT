"""This check attendance percentage"""


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
    percentage = float("{:.1f}".format(num_of_p / (num_of_a + num_of_p)))
    # finding the decision based on the percentage
    decision = "not suspended" if percentage >= 0.7 else "suspended"

    return ((decision, percentage))


if __name__ == "__main__":
    record = input("\n")
    print(type(attendance(record)))
