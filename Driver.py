import pywhatkit

import contacts as contacts

USER = 'Osaid'


def driver():
    print("Welcome to your automated Whatsapp messaging CMD {}!".format(USER))
    CMD = input('What do you want to do {}? \n>>>'.format(USER)).split()
    switcher(CMD[0], CMD[1:])

    while True:
        CMD = input('What do you want to do now {}? \n>>>'.format(USER)).split()
        if CMD[0] == 'exit':
            break
        switcher(CMD[0], CMD[1:])


def switcher(command, function):
    switch = {
        'update': update_file_name,
        'send': send,
        'get_contact': get_contact,
        3: 'get_contacts_list',
        4: 'stand_by',
        5: 'exit'
    }
    return switch.get(command)(function)


def update_file_name(filename):
    print("updating the file name to {}!".format(" ".join(filename)))


def send(info):
    print('sending > {} > to {}'.format(" ".join(info[1:]), info[0]))

def get_contact(info):
    print(" ".join(r.get_contact(info[0])))

r = contacts.Contacts('contacts.txt')

driver()

