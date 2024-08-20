def main():
    cost = 50
    accepted_coins = [25, 10, 5]
    amount_due = cost

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin
        else:
            print(f"Amount Due: {amount_due}")  # If invalid coin, reprint the same amount

    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
