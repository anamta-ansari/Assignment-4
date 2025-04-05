# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter phone number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")


def look_up_numbers(phnebook):
    while True:
        name = input("Enter name to look up: ")
        if name == "":
            break
        if name not in phnebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    look_up_numbers(phonebook)



if __name__ == '__main__':
    main()
