#Write a Python function that asks the user for a message, stores it in a list, and appends it three times. Then, print the list before and after adding the message

def copy_message():
    # Ask user for input
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Print list before adding elements
    print("List before:", my_list)

    # Append the message three times
    for i in range(3):
        my_list.append(message)

    # Print list after adding elements
    print("List after:", my_list)



if __name__ == "__main__":
    copy_message()