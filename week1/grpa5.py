age = int(input("age: "))
dob = input("DOB(mm/dd/yy): ")
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:])

fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5)
print(fifth_birthday)

last_birthday = str(day)+"/"+str(month)+"/"+str(year+age)
print(last_birthday)

month = month + 10
month, year = (month-1)%12+1, year-(month-1)//12
tenth_month = str(day)+"/"+str(month)+"/"+str(year)
print(tenth_month)

weight = float(input("weight: ")) # float: Read a number as float from stdin(Standard input)

kg = int(weight)  # Get the integer part (kg)
grams = int((weight - kg) * 1000)  # Get the fractional part converted to grams

weight_readable = str(kg)+" kg "+str(grams)+" grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)
