#słownik {key : value}
author = {
    'first_name': 'Zofia',
    'last_name': 'Nałkowska'
}

#print(author['first_name'])
#print(author['last_name'])

#items robi tuple
for item in author.items():
    print(item[0], item[1])
#to samo co wyżej
for first_name, last_name in author.items():
    print(first_name, last_name)

#author.items(), author.keys(), author.values()