import sys
import csv

def process_csv(input_file, output_file):
    
    """Process the input CSV file and write the reformatted data to the output CSV file."""
    try:
        with open(input_file, newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            data = list(reader)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Could not read file '{input_file}'. {e}")
        sys.exit(1)

    processed_data = []
    for row in data:
        if len(row) != 2:
            print("Error: Each row must have exactly two columns.")
            sys.exit(1)
        full_name, house = row
        try:
            last_name, first_name = full_name.split(", ")
        except ValueError:
            print(f"Error: The name '{full_name}' is not properly formatted.")
            sys.exit(1)
        processed_data.append([first_name, last_name, house])

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['First', 'Last', 'House'])
            writer.writerows(processed_data)
    except Exception as e:
        print(f"Error: Could not write to file '{output_file}'. {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.csv'):
        print("Error: The input file must be a .csv file.")
        sys.exit(1)
    
    process_csv(input_file, output_file)

if __name__ == "__main__":
    main()
