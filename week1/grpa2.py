a = int(input("a: " ));
output1 = a >= 5 
print(output1)
output2 = (a%5 == 0) 
print(output2)
output3 = ((a%2 != 0) and a < 10)
print(output3)
output4 = ((a % 2 != 0) and (a > -10 and a < 10))
print(output4)
output5 = (len(str(a)) % 2 == 0 and len(str(a)) <= 10)
print(output5)

price1 = int(input("Price 1: "))
discount1 = int(input("Discount 1: "))
price2 = int(input("Price 2: "))
discount2 = int(input("Discocunt 2: "))

output6 = float((price1 - (discount1/100)*price1)) < float((price2 - (discount2/100)*price2))
print(output6)