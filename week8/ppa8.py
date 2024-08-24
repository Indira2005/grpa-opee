def improvement(filename):
    """
    Find all students who have shown an improvement
    
    Argument:
        filename: string, path to file
    Return: 
        count: integer
    Name,Gender,CT,Python,PDSA
    """
    cnt = 0
    with open(filename, "r") as f:
        header = f.readline()
        for line in f:
            s = line.strip().split(",")
            if int(s[2]) < int(s[3]) < int(s[4]):
                cnt += 1
    return cnt
    