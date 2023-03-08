name = "Zuzanna"

print(name[-4:])

#rozdzielenie wyrazów - metoda split
question = "I can do this"
print(question.split(" "))

#połączenie wyrazów - metoda join
character = " "
print(character.join(["I", "can", "do", "this"]))

#usunięcie litery
print(name.lstrip("Z")) #z lewej, z prawej pstrip
print(name.strip("a")) #usuwa skranje z prawej i lewej
print(name.strip()) #usuwa niepotrzebne spacje z przodu i z tyłu

#zera z przodu, podajemy ilość znaków z których ma się składać nowy string
james_bond = 7
print(str(james_bond).zfill(3))