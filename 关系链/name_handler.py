with open('name.txt', 'r') as file:
    names = file.read()
    name_list = names.split('\n')
    for name in name_list.copy():
        if 'wiki' not in name:
            name_list.remove(name)

for name in name_list:
    print(name.strip('/wiki/'))
