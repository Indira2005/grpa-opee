def read_line (filename, n):
    cnt = 0
    with open(filename, "r") as f:
        for line in f:
            s = line.strip()
            cnt += 1
            if cnt == n:
                return s
    return "None"


