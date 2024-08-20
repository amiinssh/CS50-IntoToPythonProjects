def main():
    
    while True:
        
        try:
            
            fraction = input("Enter a fraction (X/Y): ").strip()
            
            x, y = fraction.split('/')
            
            x = int(x)
            y = int(y)
            
            if y == 0:
                print("Invalid input. Please enter a valid fraction.")
                continue
            
            if x > y:
                print("Invalid input. Please enter a valid fraction.")
                continue
            
            percentage = round((x / y) * 100)
            
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            
            break
        
        except (ValueError, ZeroDivisionError) as e:
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
