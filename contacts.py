class Contacts:

    def __init__(self, name_of_file):
        self.file = name_of_file

    def store_contact(self, name, number, relationship, birthdate=None):
        try:
            with open(self.file, 'a') as f:
                f.write('\n{} {} {}'.format(name, number, relationship))
        except():
            print('operation failed')
        print('done')

    def get_contacts(self):
        file = open(self.file, 'r')
        f = file.readlines()
        contact_list = []
        for line in f:
            contact_list.append(line.strip())
        return contact_list

    def contact_info(self):
        pass

    def get_contact(self, contact):
        contact_list = []
        for i in self.get_contacts():
            if contact in i:
                contact_list.append(i)
        return contact_list

    def is_present(self, number):
        for i in self.get_contacts():
            if number in i:
                return "yes"

    def number_of_contacts(self):
        return len(self.get_contacts())