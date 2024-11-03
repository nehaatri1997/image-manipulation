# -*- coding: utf-8 -*-
"""Image manipulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vn3eVLx8pQq0URWJ7zFDxrbNlz2MFwZN
"""

pip install pillow

"""to blurr an image"""

from PIL import Image, ImageEnhance, ImageFilter

# Function to open an image
def open_image(path):
    image = Image.open(path)
    image.show()  # Display the image
    return image

# Function to save an image
def save_image(image, path):
    # Convert the image to RGB to remove the alpha channel if present
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image.save(path)
    print(f"Image saved to {path}")

# Function to resize an image
def resize_image(image, size):
    resized_image = image.resize(size)
    resized_image.show()  # Display resized image
    return resized_image

# Function to rotate an image
def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    rotated_image.show()  # Display rotated image
    return rotated_image

# Function to crop an image
def crop_image(image, box):
    cropped_image = image.crop(box)
    cropped_image.show()  # Display cropped image
    return cropped_image

# Function to adjust brightness
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)
    brightened_image.show()  # Display brightened image
    return brightened_image

# Function to apply a filter (e.g., BLUR)
def apply_filter(image, filter_type):
    filtered_image = image.filter(filter_type)
    filtered_image.show()  # Display filtered image
    return filtered_image

# Main Program
if __name__ == "__main__":
    # Open an image
    img = open_image("result.png")  # Replace 'your_image.jpg' with your image path

    # Resize the image
    resized_img = resize_image(img, (300, 300))  # Resize to 300x300

    # Rotate the image by 45 degrees
    rotated_img = rotate_image(img, 45)

    # Crop the image (box defined as left, upper, right, lower)
    cropped_img = crop_image(img, (100, 100, 400, 400))

    # Adjust brightness (1.0 means no change, <1.0 for darker, >1.0 for brighter)
    brightened_img = adjust_brightness(img, 1.5)

    # Apply a blur filter
    blurred_img = apply_filter(img, ImageFilter.BLUR)

    # Save the edited image
    save_image(blurred_img, "blurred_image.jpg")

"""to crop an image

"""

from PIL import Image

# Function to crop an image
def crop_image(image_path, output_path, crop_box):
    # Open an image file
    try:
        with Image.open(image_path) as img:
            # Crop the image using the crop_box (left, upper, right, lower)
            cropped_img = img.crop(crop_box)
            # Show the cropped image
            cropped_img.show()
            # Save the cropped image to a file
            # Convert to RGB before saving to JPEG to handle transparency
            cropped_img = cropped_img.convert("RGB")
            cropped_img.save(output_path)
            print(f"Cropped image saved at: {output_path}")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")

# Example Usage
if __name__ == "__main__":
    # Path to the image file
    input_image = "result.png"  # Replace with your image file path
    output_image = "cropped_image.jpg" # or cropped_image.png to keep transparency

    # Define the crop box (left, upper, right, lower)
    crop_box = (100, 100, 400, 400)  # Adjust these values as needed

    # Call the function to crop the image
    crop_image(input_image, output_image, crop_box)