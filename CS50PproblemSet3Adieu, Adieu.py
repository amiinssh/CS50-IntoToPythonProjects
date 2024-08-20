def main():
    
    import sys
    
    names = []
    
    try:
        
        while True:
            
            name = input("Name: ")
            names.append(name)
    except EOFError:
        
        pass

    if len(names) == 1:
        
        message = f"Adieu, adieu, to {names[0]}"
        
    elif len(names) == 2:
        
        message = f"Adieu, adieu, to {names[0]} and {names[1]}"
        
    else:
        
        message = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"
    
    print(message)

if __name__ == "__main__":
    main()
