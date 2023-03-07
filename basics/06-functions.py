#argumenty pozycyjne - przekazujemy w kolejnosci według deklaracji
#argumenty nazwane - kolejnosc dowolna, posługuje sie nazwą

def calculate_sum(a, b, c=10):
    print("Suma a+b+c wynosi",a+b+c)
    return a+b+c

calculate_sum(2, 3)
result = calculate_sum(2, 3, 2)

print("Wynikiem funkcji jest", result)