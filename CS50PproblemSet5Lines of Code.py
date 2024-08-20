import sys
import os

def count_lines_of_code(filename):
    line_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    line_count += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)
    
    return line_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not filename.endswith('.py'):
        print("Error: The file must have a .py extension.")
        sys.exit(1)
    
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)

    lines_of_code = count_lines_of_code(filename)
    
    print(lines_of_code)

if __name__ == "__main__":
    main()
