import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def generate_target(level):
    return random.randint(1, level)

def guess_number(target):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < target:
                    print("Too small!")
                elif guess > target:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass

def main():
    level = get_level()
    target = generate_target(level)
    guess_number(target)

if __name__ == "__main__":
    main()
