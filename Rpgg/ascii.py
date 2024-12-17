from PIL import Image

ASCII_CHARS = "@%#*+=-:. "


def resize_image(image, new_width=100):
    """Resize image to new width"""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))


def grayscale_image(image):
    """Convert image to grayscale"""
    return image.convert("L")

def pixel_to_ascii(image):
    """Convert pixel to ascii"""
    pixels = image.getdata()
    ascii_str = ""
    # Calculate the range of ASCII_CHARS to map pixel values to indices
    ascii_length = len(ASCII_CHARS)
    
    for pixel_value in pixels:
        # Map pixel_value to an index in ASCII_CHARS
        index = pixel_value * ascii_length // 256  # Scale down the pixel value
        ascii_str += ASCII_CHARS[index]
        
    return ascii_str



def image_to_ascii(image_path, new_width=100):
    """Convert image to ascii art"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}: {e}")
        return
    
    # Resize, convert to grayscale, and generate ASCII text
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    # Convert each pixel to ASCII
    ascii_str = pixel_to_ascii(image)

    # Organize ASCII characters into lines
    ascii_len = len(ascii_str)
    ascii_image = "\n".join([ascii_str[i:i + new_width] for i in range(0, ascii_len, new_width)])

    # Print the ASCII art
    print(ascii_image)

    # Save to a text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


# Test
image_path = "C:/Users/FIRAS/Documents/ynov/B2/Python/game/Rpgg/téléchargé.jpeg"
image_to_ascii(image_path, new_width=100)
# image_path = "C:/Users/FIRAS/Documents/ynov/B2/Python/game/Rpgg/téléchargé.jpeg"

