import re
import sys


def count(s):
    s = s.lower()

    pattern = r"\bum\b"

    matches = re.findall(pattern, s)

    return len(matches)


def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
