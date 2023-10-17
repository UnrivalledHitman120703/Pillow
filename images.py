from PIL import Image, ImageFilter

# Open an image
img = Image.open("pikachu.jpg")

# Applying the image filter: Blur
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

# Applying the image filter: Smooth
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", "png")

# Applying the image filter: Sharpen
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", "png")

# Converting the image
filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")

# Display the image
print(img)
# Display image properties
print(img.format)
print(img.mode)
