import sys
import os
import csv
from tabulate import tabulate

def read_csv(file_path):
    """Read a CSV file and return its content as a list of lists."""
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.csv'):
        print("Error: The file must have a .csv extension.")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    data = read_csv(file_path)

    if not data:
        print("Error: The file is empty.")
        sys.exit(1)

    print(tabulate(data, headers='firstrow', tablefmt='grid'))

if __name__ == "__main__":
    main()
