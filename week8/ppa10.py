def number_grid(m, n):
    """
    Write a number grid to a file

    Arguments:
        m, n: positive integers
    Return:
        None
    1,2,3   
    4,5,6
    7,8,9
    10,11,12
    13,14,15
    """
    with open("numgrid.csv", "w") as f:
        for i in range (1, m*n+1):
            f.write(f"{i}")
            if i % n == 0:
                f.write("\n")
            else :
                f.write(",")