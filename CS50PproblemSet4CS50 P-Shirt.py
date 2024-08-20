import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python shirt.py input_file output_file")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Error: Input and output files must have .jpg, .jpeg, or .png extensions.")
        sys.exit(1)
    
    if input_ext != output_ext:
        print("Error: Input and output files must have the same extension.")
        sys.exit(1)
    
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        sys.exit(1)
    
    try:
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")
        
    except IOError as e:
        
        print(f"Error: Unable to open image files. {e}")
        sys.exit(1)
    
    input_image_resized = ImageOps.fit(input_image, shirt_image.size)
    
    output_image = Image.new('RGBA', input_image_resized.size)
    output_image.paste(input_image_resized, (0, 0))
    output_image.paste(shirt_image, (0, 0), shirt_image)
    
    try:
        output_image.convert("RGB").save(output_path, format='PNG' if output_ext == '.png' else 'JPEG')
    except IOError as e:
        print(f"Error: Unable to save the output file. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
