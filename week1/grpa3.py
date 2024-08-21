s = "hello python"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id

output1 = s[2]   #third character of s
print(output1)

output2 = s[-4]  #fourth last cjharacter of s -- for characters from end, use '-' and the position of char from the end
print(output2)

output3 = s[0:3] #first three characters of s
print(output3)

output4 = s[0:-1:2]  #every second charachter of s -- here 0 is the beginning, -1 is the end and 2 is the step
output4 = s[::2]  #alternative method for every second character
print(output4)

output5 = s[-3:]  #last three characters of s
print(output5)

output6 = s[::-1]  #reverse of s
print(output6)

output7 = course_code[3] #get the term number
print(output7)

output8 = course_code[0:2] #get the course year as a two digit number
output8 = course_code[:2]  #alternative for course year
print(output8)