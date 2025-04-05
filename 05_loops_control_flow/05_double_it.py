def main():
        curr_value = int(input("Enter any number : "))
        while curr_value < 100:
            double_value = curr_value * 2 
            print(f"{curr_value} doubled is {double_value}")
            break

if __name__ == "__main__":
    main()