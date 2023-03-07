#import funkcji z innego pliku .py
from finances import calculate_brutto

netto = float(input("Podaj wartość netto: "))
vat = float(input("Podaj wartość vat: "))

brutto = calculate_brutto(netto, vat)

print(f"Wartość brutto wynosi {brutto}.")