def main():
    import sys

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    month_to_number = {month: str(index + 1).zfill(2) for index, month in enumerate(months)}

    while True:
        user_input = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ").strip()
        
        if '/' in user_input:
            try:
                month, day, year = map(int, user_input.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31 and year >= 1:
                    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                    print(formatted_date)
                    break
                else:
                    print("Invalid date. Please try again.")
            except ValueError:
                print("Invalid format. Please try again.")
        
        elif ',' in user_input:
            try:
                month_day, year = user_input.split(',')
                month_name, day = month_day.strip().split(' ')
                day = int(day)
                year = int(year.strip())
                
                if month_name in month_to_number and 1 <= day <= 31 and year >= 1:
                    month = month_to_number[month_name]
                    formatted_date = f"{year:04d}-{month}-{day:02d}"
                    print(formatted_date)
                    break
                else:
                    print("Invalid date. Please try again.")
            except ValueError:
                print("Invalid format. Please try again.")
        else:
            print("Invalid format. Please try again.")

if __name__ == "__main__":
    main()
