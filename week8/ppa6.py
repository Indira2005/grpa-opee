def write_AP(a_1, d, n):
    """
    Write the AP to a file

    Arguments:
        a_1: first term, integer
        d: common difference, integer
        n: number of terms, integer
    Return:
        None
    """
    c = a_1
    with open("out.txt", "w") as f:
        f.write(f"{a_1}\n")
        for i in range(n-1):
            c = c + d
            f.write(f"{c}\n")
            
            
            