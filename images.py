# Pillow library for image manioulation
# Name = Indrajeet Mondal; Date = 17th October 2023
# SourceCode

from PIL import Image, ImageFilter

# Open an image
img = Image.open("pikachu.jpg")

# Applying the image filter: Blur
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

# Re-open the original image
img = Image.open("pikachu.jpg") 

# Applying the image filter: Smooth
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", "png")

# Re-open the original image again
img = Image.open("pikachu.jpg")

# Applying the image filter: Sharpen
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", "png")

# Re-open the original image again
img = Image.open("pikachu.jpg")

# Rotating the image
crooked = img.rotate(270) 
crooked.save("rotate.png", "png")

# Re-open the original image again
img = Image.open("pikachu.jpg")

# Resizing the image
resize = img.resize((300, 300))
resize.save("resized.png", "png")

# Re-open the original image again
img = Image.open("pikachu.jpg")

# Selecting a region
# The crop method takes a box argument, so you need to pass it as a tuple (left, upper, right, lower)
region = img.crop((100, 100, 400, 400))
region.save("region.png", "png")

# Re-open the original image again
img = Image.open("pikachu.jpg")

# Converting the image
filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")

# Display the image
filtered_img.show()

# Display image properties
print(img.format)
print(img.mode)
