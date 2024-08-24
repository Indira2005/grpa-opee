def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    1,2,3
    4,5,6
    7,8,9
    """
    l1 = []
    l2 = []
    with open(filename, "r") as f:
        for line in f:
            s = line.strip().split(",")
            for i in range(len(s)):
                s[i] = int(s[i])
            l1.append(s)
    return l1