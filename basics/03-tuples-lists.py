#tuple a = ('one', 'two', 'three')
#niemutowalne

#list
#fruits = ['peach', 'orange', 'mango', 'lemon', 'lemon', 'apple']
#fruits.sort()

#for fruit in fruits:
#    print(fruit)

fruits = []

for i in range(5):
    fruits.append(input(f"Jaki jest Twój {i+1} ulubiony owoc? "))

fruits.sort()

for fruit in fruits:
    print(fruit)