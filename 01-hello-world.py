first_name = input("Jak masz na imię? ")
age = int(input("Ile masz lat? "))

#print
#print(f"Hello {first_name}!")
#print(f"Mam {age} lat.")

if first_name == "Zuzu":
    print("Cześć Zuzu! Kopę lat!")
else:
    print("Miło mi Cię poznać!")

if age >= 18:
    print("Jesteś pełnoletni.")
else:
    print(f"Musisz poczekać jeszcze {18 - age} lat.")