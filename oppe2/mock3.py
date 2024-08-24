def calculate_total_price(prices_file: str, shopping_file: str) -> int:
    '''Compute the total amount spent on the products.

    Args:
        prices_file (str): path of file containing product purchase details.
        shopping_file (str): path of file containing product prices.

    Returns:
        float: The total amount.
    '''
    with open(shopping_file, "r") as f1, open(prices_file, "r") as f2:
        l1 = []
        l2 = []

        header1 = f1.readline()
        for line in f1:
            list1 = line.strip().split(",")
            list1 = list1[1:3]
            l1.append(list1)

        header2 = f2.readline()
        for line in f2:
            list2 = line.strip().split(",")
            list2 = list2[1:3]
            l2.append(list2)
        print(l1, l2, sep = "\n")

        ans = 0
        for fl in l1:
            for sl in l2:
                if fl[0] == sl[0]:
                    ans = ans + float(fl[1])*float(sl[1])

        print(ans)

