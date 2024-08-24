def get_max_line(filename):
    """
    Get the line that houses the maximum value.
    Argument:
        filename: string, path to the file.
    Return:
        result: integer, the line number that contains the maximum value.
    """
    max_val = None
    l = []
    with open(filename, "r") as f:
        for line in f:
            s = int(line.strip())
            l.append(s)
        for i in range(len(l)):
            if max_val is None or l[i] > max_val:
                max_val = l[i]
                ans = i+1
    return ans


            
