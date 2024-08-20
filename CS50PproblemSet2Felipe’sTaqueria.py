def main():
    
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    print("Enter your order (Ctrl-D to finish):")

    try:
        while True:
            item = input().strip()

            normalized_item = item.title()

            if normalized_item in menu:
                
                total_cost += menu[normalized_item]
                print(f"${total_cost:.2f}")
            else:

                continue

    except EOFError:

        print("Order complete.")

if __name__ == "__main__":
    main()
