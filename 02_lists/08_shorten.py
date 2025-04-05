#You need to write a function called shorten(lst), which removes items from the end of a list until the list has at most MAX_LENGTH items.

MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    print("Rmoved items from list:")
    shorten(lst)
    print(lst)


if __name__ == '__main__':
    main()