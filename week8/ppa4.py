def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
        
    Name,Age
    Arti,20
    Kalam,60
    Atul,25
    Krishnan,24
    Sahana,20
    """
    d = {}
    with open(filename, "r") as f:
        header = f.readline()
        for line in f:
            s = line.strip().split(",")
            d[s[0]] = int(s[1])
    return d
            