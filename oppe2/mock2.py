def consistent_sales_increase(filename):
    '''Return the name of the region with the highest count of representatives, 
    who have shown consistent sales growth across the quarters.

    Args:
        filename (str): path of the file. 

    Return:
        str: Name of the region with highest count of such representatives. 
    '''
    regions = []
    reg_count = {}
    with open(filename, "r") as f:
        header = f.readline()
        for line in f:
            s = line.strip().split(",")
            if s[4] < s[5] < s[6] <s[7]:
                regions.append(s[3])
        for region in regions:
            reg_count[region] = regions.count(region)
        reg_max = 0
        reg_max = max(reg_count, key = lambda x: reg_count[x])
        return reg_max

        
