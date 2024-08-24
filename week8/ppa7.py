def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    with open(filename, "r") as f1, open("out.txt", "w") as f2:
        for line in f1:
            c = line.strip()
            f2.write(f"{c}")
            f2.write(".\n")
            