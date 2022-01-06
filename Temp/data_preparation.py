import os
from PIL import Image

image_source_path = 'picture/'
image_target_path = 'picture/'

# We are using Pillow to resize all images to our desired size

for filename in os.listdir(image_source_path):
    path = os.path.join(image_source_path, filename)
    image = Image.open(path).resize((1024, 1024), Image.ANTIALIAS)

    resized_image = image.save(image_target_path + filename)
    print(f"{filename} image is resized...")
