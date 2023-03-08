number = 1

print("While: ")
while number <= 6:
    print(number)
    number += 1

print("For: ")
for number in range(0,7): #przedział prawostronnie otwarty!!!
    print(number)

print("For - początek - koniec - krok")
for number in range(0,15,2):
    print(number)

print("Continue, break")
for number in range(0,11):
    if number == 4:
        continue    #pominie 4 (nie idzzie już dalej do printa, tylko zaczyna nowe wywołanie pętli)
    if number == 8:
        break       #skończy na 7 (bo print jest po sprawdzeniu warunku)
    print(number)