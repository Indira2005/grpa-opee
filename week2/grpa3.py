continuous_tense = True
word = input("word: ")
if word[-3:] == "ing":
    word = word[:-3]
print(word)

if continuous_tense:
    word = word+"ing"
print(word)

age = int(input("age: "))
if age < 18:
    age_group = "Child"
else :
    age_group = "Adult"
print(age_group)

time = input("time: ")
if int(time[:1]) >= 1 and int(time[:1]) <= 12:
    is_time_valid = True

time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM") * 12
print(time_in_hrs)


