def extract_lines(filename):
    """
    Get all males who have scored at least 70 marks in Python
    
    Argument:
        filename: string
    Return:
        None
    SeqNo,Name,Gender,CT,Python,PDSA
    """
    with open(filename, "r") as f1, open("python.csv", "w") as f2:
        header = f1.readline()
        f2.write(f"{header}")
        for line in f1:
            s = line.strip().split(",")
            if s[2] == "M":
                if int(s[4]) >= 70:
                    f2.write(f"{line}")
                    