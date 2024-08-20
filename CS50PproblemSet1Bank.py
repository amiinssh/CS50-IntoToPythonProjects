user_input = input("greetings: ").strip()

if user_input.lower().startswith("hello"):
    print("$0")
    
elif user_input == "How you doing?":
    print("$20")

elif user_input.lower().startswith("h"):
    print("$20")

else:
    print("$100")