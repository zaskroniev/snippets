countries_and_capitals = {"poland": "Warsaw",
                          "Czechia": "Prague",
                          "Germany": "Berlin"}

#przechwytywanie i obsługiwanie wyjątków
try:
    print(2/0)
    print(countries_and_capitals["USA"])
except KeyError:
    print("Klucz nie został znaleziony.")
except ZeroDivisionError:
    print("Nie można dzielić przez zero.")
finally:
    print("To wykona się zawsze.")

print("Program dalej działa!")