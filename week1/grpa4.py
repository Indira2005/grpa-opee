str1 = input("str1: ")
str2 = input("str2: ")
str3 = input("str3: ")
print(str1 + " " + str2) #concatenate the two strins with a space between them
print(str1, str2, sep= " ") #alternative and better way
print(str1[:4], str2[-4:], sep= "-") #join first 4 letters of str1 aand last four of str2 with a hypen in b/w
print("-" * 50) #hyphen repeated 50 times

n1 = int(input("n1: "))
n2 = int(input("n2: "))
print("-" * n1) #print hyphen n1 times
print("-" * n2) #print hyphen n2 times

output1 = str1 == str2 == str3
print(output1)
output2 = (str1 < str2) and (str1 < str3)
print(output2)
output3 = 'h' in str1
print(output3)
output4 = str1.endswith('a') or str1.endswith('A')
print(output4)

sent = input("sent: ")
output5 = "python" in sent
print(output5)

