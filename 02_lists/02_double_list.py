# Write a program that doubles each element in a list of numbers.
numbers = [3,6,9,12]

def double_numbers(numbers):
    doubled_list = []  
    for num in numbers:  
        doubled_value = num * 2  
        doubled_list.append(doubled_value)  
    return doubled_list  


def main():
    print(double_numbers(numbers)) 


if __name__ == "__main__":
    main()
