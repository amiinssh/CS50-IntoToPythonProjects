import datetime
import sys


def date_to_words(n):
    """Convert a number to words."""
    ones = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    thousands = ["", "thousand"]

    def num_to_words(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        elif 20 <= num < 100:
            return tens[num // 10] + ("" if num % 10 == 0 else "-" + ones[num % 10])
        elif 100 <= num < 1000:
            return (
                ones[num // 100]
                + " hundred"
                + ("" if num % 100 == 0 else " and " + num_to_words(num % 100))
            )
        elif 1000 <= num < 10000:
            return (
                ones[num // 1000]
                + " thousand"
                + ("" if num % 1000 == 0 else " " + num_to_words(num % 1000))
            )
        else:
            raise ValueError("Number out of range for this function")

    if n == 0:
        return ones[0]
    elif n < 10000:
        return num_to_words(n)
    else:
        raise ValueError("Number out of range for this function")


def calculate_age_in_minutes(birthdate):
    """Calculate the age in minutes given a birthdate."""
    today = datetime.date.today()
    birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    if birth_date > today:
        raise ValueError("Birthdate cannot be in the future.")
    delta = today - birth_date
    return delta.days * 24 * 60


def main():
    """Main function to prompt user and display age in minutes."""
    try:
        birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
        age_in_minutes = calculate_age_in_minutes(birthdate)
        age_in_words = date_to_words(age_in_minutes)
        print(age_in_words)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
