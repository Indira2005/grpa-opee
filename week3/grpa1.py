task = input("task: ")

if task == "sum_until_0":
    num = int(input("number: "))
    sum = num
    while (num != 0):
        num = int(input("number: "))
        sum = sum + num
    print(sum)

elif task == "total_price":
    total_price = 0
    while (True):
        line = input("quantity, price: ")
        if line == "END":
            break
        quantity, price = line.split()
        quantity, price = int(quantity), int(price)
        total_price = total_price + quantity*price
    print(total_price)

elif task == "only_ed_or_ing":
    fin_string = ""
    while (True):
        word = input("word: ")
        if word.upper() == "STOP":
            break
        if word.lower().endswith("ed") or word.lower().endswith("ing"):
            fin_string = fin_string + " " + word
    print(fin_string)

elif task == "reverse_sum_palindrome":
    num = int(input("num: "))
    while num != -1:
        rev_num = int(str(num[::-1]))
        sum = num + rev_num
        if str(sum) == str(sum[::-1]):
            print(num)
        num = int(input("num:"))

elif task == "double_string":
    line = input()
    while line != " ":
        print(line*2)
        line = input()

elif task == "odd_char":
    line = input()
    while line[-1] != ".":
        print(line[::2], end =" ")
        line = input()
    print(line[::2])

elif task == "only_even_squares":
    while (True):
        line = input()
        if line == "NAN":
            break
        num = int(line)
        if num % 2 == 0:
            print(num ** 2)

elif task == "only_odd_lines":
    result  = ""
    line_no = 1
    while True:
        line = input()
        if line == "END":
            break
        if line_no%2:
            result = line + "\n" + result
        line_no+=1
    print(result)        
        




        
