# image-manipulation

This project demonstrates various basic image manipulation techniques, including resizing, rotating, cropping, adjusting brightness, and applying filters using Python's Pillow library.

# Project Overview
The project consists of the following functionalities:

Open and Display Image: Load an image file and display it.
Resize Image: Resize the image to a specified dimension.
Rotate Image: Rotate the image by a specified angle.
Crop Image: Crop a specific section of the image.
Adjust Brightness: Modify the brightness level of the image.
Apply Filters: Apply various filters, such as blur, to the image.
Save Image: Save the modified image to a specified location.

# Requirements
Python 3.x
Pillow (PIL): The Python Imaging Library is used for image processing tasks.


# Code Overview
Key Functions
open_image(path): Opens and displays the image from the specified path.
save_image(image, path): Saves the image to the specified path, converting it to RGB format if necessary.
resize_image(image, size): Resizes the image to the specified size (width, height).
rotate_image(image, angle): Rotates the image by a specified angle in degrees.
crop_image(image, box): Crops the image based on the specified box dimensions (left, upper, right, lower).
adjust_brightness(image, factor): Adjusts brightness by a specified factor (1.0 = original, <1.0 = darker, >1.0 = brighter).
apply_filter(image, filter_type): Applies a specified filter (e.g., ImageFilter.BLUR).
