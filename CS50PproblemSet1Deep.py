user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

cleaned_input = user_input.lower().strip()

if cleaned_input == "42":
    print("Yes")
elif cleaned_input == "forty-two":
    print("Yes")
elif cleaned_input == "forty two":
    print("Yes")
else:
    print("No")
