#zbiory sets - wartości nie mogą się powtarzać
#kolejność nie ma znaczenia
#duplikaty zostają usunięte
first_names = set()

first_names.add('Michał')
first_names.add('Kacper')
first_names.add('Ania')
first_names.add('Jola')
first_names.add('Zygmunt')
first_names.add('Wincent')

print(first_names)

#------

team_a = {'Anka', 'Jola', 'Basia', 'Hela', 'Hania'}
team_b = {'Anka', 'Jola', 'Hela', 'Madzia'}

print("SUMA:", team_a | team_b)
print("CZĘŚĆ WSPÓLNA:", team_a & team_b)
print("RÓŻNICA SYMETRYCZNA:", team_a ^ team_b)
print("A - B:", team_a - team_b)

