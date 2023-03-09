#wyświetla kolejne wyrazy ciągu Fibonacciego - zadaną ilość
def fibbonaci_display(quantity):
    item_one = 0
    item_two = 1
    number = 0
    while number < quantity:
        if number == 0:
            print(item_one)
            #item_one += 1
        elif number == 1:
            print(item_two)
        else:
            print(item_one + item_two)
            temporary = item_one
            item_one = item_two
            item_two = temporary + item_two
        number += 1

quantity = int(input("Ile liczb z ciągu Fibbonaciego chcesz wyświetlić? "))
fibbonaci_display(quantity)
