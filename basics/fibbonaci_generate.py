#generuje listę wyrazów ciągu Fibonacciego o zadanej długości
def fibbonaci_display(quantity):
    item_one = 0
    item_two = 1
    number = 0
    sequence = []
    while number < quantity:
        if number == 0:
            sequence.append(item_one)
            #item_one += 1
        elif number == 1:
            sequence.append(item_two)
        else:
            sequence.append(item_one + item_two)
            temporary = item_one
            item_one = item_two
            item_two = temporary + item_two
        number += 1
    return sequence

quantity = int(input("Ile liczb z ciągu Fibbonaciego chcesz wyświetlić? "))
sequence = fibbonaci_display(quantity)

print(sequence)