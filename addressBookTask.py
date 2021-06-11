import pickle

BOOK = 'C:\\Users\\fk724s\\OneDrive\\Документы\\files\\Programming\\addressBookInfo\\book.txt'
contacts = {}


class Person:
    """Представляет любого человека."""

    def __init__(self, name, age):
        self.name = name
        self.phoneNumber = age
        print('(contact created: {})'.format(self.name))

    def tell(self):
        """Вывести информацию."""

        print('{}: {} \n'.format(self.name, self.phoneNumber), end="")


def add(name, phone):
    name = Person(name, phone)
    contacts[name] = phone


def delete(dictionary, deleteName):
    for i in dictionary:
        if i.name == deleteName:
            print('(contact deleted: {})'.format(i.name))
            dictionary.pop(i)
            break


def view(dictionary):
    for member in dictionary:
        member.tell()


def longTimeUse(file, dictionary):
    k = open(file, 'wb')
    pickle.dump(dictionary, k)
    k.close()


def loadFromFile(file):
    global contacts
    k = open(file, 'rb')
    contacts = pickle.load(k)


def command(request):
    if 'add' in request:
        name, phone = request[1], request[2]
        add(name, phone)
        longTimeUse(BOOK, contacts)

    elif 'delete' in request:
        delName = request[1]
        delete(contacts, delName)
        longTimeUse(BOOK, contacts)

    elif 'view' in request:
        loadFromFile(BOOK)
        view(contacts)

    else:
        print('Command not exist. Try to write a different command (enter \'help\' to view all commands)')


while True:
    s = input()
    if s == 'help':
        print('''You can use this commands:
- add
- delete
- view

To view information about function enter its name''')

        helpReq = input()

        if helpReq == 'add':
            print('this function append new person information to address book')

        elif helpReq == 'delete':
            print("this function delete person information from address book")

        elif helpReq == 'view':
            print('this function print all information about people from address book')

        elif helpReq == 'stop':
            break

        else:
            print('Command not exist')
    elif s == 'stop':
        break
    else:
        command(s.split('-'))
