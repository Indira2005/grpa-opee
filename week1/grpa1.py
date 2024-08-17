a = int(input("a: "))
b = int(input("b: "))
output1 = a + b
print(f"Sum of a and b = {output1}")
output2 = 2*(a + b)
print(f"Twice the sum of a and b = {output2}")
output3 = abs(a-b)
print(f"Absolute difference between a and b = {output3}")
output4 = abs((a+b) - (a*b))
print(f"Absolute difference between sum and product of a and b = {output4}")

price = float(input("Price: "))
discount_percent = float(input("Discount percent: "))
discounted_price = float((price - (discount_percent/100)*price))
rounded_discounted_price = round(discounted_price)
print(f"Discounted price = {discounted_price}")

total_mins = int(input("Total minutes: "))
hrs = total_mins//60
mins = total_mins - (hrs*60)
print(f"Time in hrs and mins = {hrs} hrs {mins} mins")