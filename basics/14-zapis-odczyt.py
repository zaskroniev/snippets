file = open("countries_and_capitals.txt", "w+")

countries_and_capitals = {"poland": "Warsaw",
                          "Czechia": "Prague",
                          "Germany": "Berlin"}

for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n")

file.close()

##

file = open("countries_and_capitals.txt")

for line in file.readlines():
    print(line.strip()) #strip usuwa niepotrzebne znaki nowej linii