import random
import pickle
chr_converts = {
    'a': 'c',
    'c': 't',
    't': 'b',
    'b': 'n',
    'n': 'h',
    'h': 'v',
    'v': 'w',
    'w': 'f',
    'f': 'j',
    'j': 'g',
    'g': 'o',
    'o': 'r'
}
special_chr = ('?', '!', '@', '#', '$', '%', '&', '*')


class Passwords:

    def generate(self, data):
        new_pass = ''
        count = 2
        for character in data:
            if character in chr_converts:
                new_pass += chr_converts.get(character, character)
            elif len(data) % count == 0:
                new_pass += random.choice(special_chr)
                count += 1
            else:
                new_pass += str(random.randint(0, len(data)))
                count += 1

        return new_pass

    def store(self, old_password, new_password):
        passwords = pickle.load(open('passwords.txt', 'rb'))
        passwords[old_password] = new_password
        pickle.dump(passwords, open('passwords.txt', 'wb'))

    def get_pass(self, user_input):
        passwords = pickle.load(open('passwords.txt', 'rb'))
        password = passwords.get(user_input, 'Invalid Keyword')
        return password

    def create_file(self):
        passwords = {}
        pickle.dump(passwords, open('passwords.txt', 'wb'))
        return 'New File Created'