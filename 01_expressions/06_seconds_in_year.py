# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement

def seconds_in_a_year():
    seconds_per_minute = 60
    minutes_per_hour = 60
    hours_per_day = 24
    days_per_year = 365  # Use 366 for a leap year
    year = int(input("Enter the number of years: "))
    days_of_year = year * days_per_year

    total_seconds = seconds_per_minute * minutes_per_hour * hours_per_day * days_of_year

    print(f"There are {total_seconds} seconds in {year} year.")

if __name__ == "__main__":
    seconds_in_a_year()
