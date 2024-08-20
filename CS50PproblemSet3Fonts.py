import sys
import random
from pyfiglet import Figlet

def main():
    
    figlet = Figlet()

    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        
        font = random.choice(available_fonts)
        
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        
        if sys.argv[2] in available_fonts:
            
            font = sys.argv[2]
        else:
            
            print(f"Error: '{sys.argv[2]}' is not a valid font.")
            sys.exit(1)
    else:
        
        print("Usage: figlet.py [-f FONT_NAME | --font FONT_NAME]")
        sys.exit(1)

    figlet.setFont(font=font)

    text = input("Input text: ")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
