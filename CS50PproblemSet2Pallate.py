def is_valid(s):
    
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    has_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
            if not s[i:].isdigit():
                return False
            if char == '0':
                return False
            break

    if not s.isalnum():
        return False

    return True

def main():
    plate = input("Enter a vanity plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
