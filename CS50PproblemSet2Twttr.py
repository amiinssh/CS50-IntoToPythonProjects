def main():

    text = input("Input: ")

    result = remove_vowels(text)

    print(f"Output: {result}")

def remove_vowels(text):

    vowels = "AEIOUaeiou"

    no_vowels = ''.join([char for char in text if char not in vowels])

    return no_vowels

if __name__ == "__main__":
    main()
