def calculate_total_spent(filename):
    '''
    Args:
        filename (str): The path to the file containing transaction data.

    Returns:
        dict: A dictionary where keys are customer names and values are the total amount spent.
        
    Alice Brown,119.21,2023-10-20
    Carol White,476.74,2024-06-07
    Alice Brown,22.76,2024-07-24
    '''
    d = {}
    with open(filename, "r") as f:
        for line in f:
            s = list(line.strip().split(","))
            s = s[:2]
            if s[0] in d.keys():
                d[s[0]] += float(s[1])
            else:
                d[s[0]] = float(s[1])
    return d

