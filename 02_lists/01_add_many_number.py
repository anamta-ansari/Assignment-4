# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        print(f"num: {num}")
        total += num
    return total
    

numbers = [11, 22, 33, 44, 55]
print(sum_of_numbers(numbers)) 

