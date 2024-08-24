d = {}
with open("test.txt", "r") as f:
    for line in f:
        s = line.strip().split("\n")
        for word in s:
            if word in d.keys():
                d[word] += 1
            else :
                d[word] = 1
print(d)