documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name(docs):
    user_input = input('Input document number: ')
    test_list = list()
    for i in docs:
        test_list.append(i['number'])

    if user_input in test_list:
        for i in docs:
            if user_input == i['number']:
                print(i['name'])
    else:
        print('There is no id with this number')


def get_shelf(dirs):
    user_input = input('Input document number: ')
    test_list = list()
    for v in dirs.values():
        for el in v:
            test_list.append(el)

    if user_input in test_list:
        for k, v in dirs.items():
            if v.count(user_input) > 0:
                print(k)
    else:
        print('There is no id with this number')
    return k


def get_list(docs):
    for i in docs:
        every_dict = dict(i)
        t = every_dict.get("type")
        num = every_dict.get("number")
        name = every_dict.get("name")
        print(t, num, name)


def get_list_shelf(dirs):
    for k, v in dirs.items():
        print(f'Shelf={k}, Docs={v}')


def add_doc(docs, dirs):
    type = input('Input type of document: ')
    number = input('Input number: ')
    name = input('Input name: ')
    new_shelf = input('In which shelf should we place it?: ')
    new_doc = {"type": type, "number": number, "name": name}
    if new_shelf in dirs:
        for k, v in dirs.items():
            if k.count(new_shelf) > 0:
                v.append(number)
                docs.append(new_doc)
                print('Documents added to shelf and registry')
    else:
        print('There is no shelf. Documents do not added')

    return docs, dirs


def del_doc(docs, dirs):
    user_input = input('Input document number: ')
    num_list = list()
    for i in docs:
        num = i.get('number')
        num_list.append(num)
    if num_list.count(user_input) == 0:
        print('There is no id with this number')
    elif num_list.count(user_input) > 0:
        docs.pop(num_list.index(user_input))
        print(f'Documents with number {user_input} removed from registry')
        for v in dirs.values():
            if user_input in v:
                v.remove(user_input)
                print(f'Documents with number {user_input} removed from shelf')
                break

    return docs, dirs


def move_doc(dirs):
    user_input = input('Input document number: ')
    dest_shelf = input('Input destination shelf: ')
    test_list = list()
    # print(type(test_list))
    for v in dirs.values():
        for el in v:
            test_list.append(el)

    if user_input in test_list and dest_shelf in dirs:
        for v in dirs.values():
            if v.count(user_input) > 0:
                v.remove(user_input)
                for k, v in dirs.items():
                    # print(v.count(user_input), k.count(dest_shelf))
                    if k.count(dest_shelf) > 0:
                        v.append(user_input)
    elif user_input in test_list and dest_shelf not in dirs:
        print('There is no shelf with this number')
    elif user_input not in test_list and dest_shelf in dirs:
        print('There is no id with this number')

    return dirs


def add_shelf(dirs):
    new_shelf = input('Input new shelf: ')
    new_list = list()
    if new_shelf not in dirs:
        dirs[new_shelf] = new_list
    elif new_shelf in dirs:
        print(f'Shelf with number {new_shelf} already exist')

    return dirs


while True:
    try:
        user_input = input('Type command. p, s, l, ls, a, d, m, as - is allowed. q - for quit: ')
        if user_input == 'p':
            get_name(documents)
        elif user_input == 's':
            get_shelf(directories)
        elif user_input == 'l':
            get_list(documents)
        elif user_input == 'ls':
            get_list_shelf(directories)
        elif user_input == 'a':
            add_doc(documents, directories)
        elif user_input == 'd':
            del_doc(documents, directories)
        elif user_input == 'm':
            move_doc(directories)
            # print(move_doc(directories))
        elif user_input == 'as':
            add_shelf(directories)
            # print(add_shelf(directories))
        elif user_input == 'q':
            break
    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        print("Press q in another iteration")
