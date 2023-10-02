from PIL import Image

def expand_to_rectangle(pil_img, background_color):
    target_width = 384  # Desired width
    target_height = 256 # Desired height
    width, height = pil_img.size # Get current width and height
    width_scale = target_width / width # Get scale factors
    height_scale = target_height / height 
    scale = min(width_scale, height_scale) # Get minimum scale factor
    new_width = int(width * scale) # Calculate the size of the scaled image
    new_height = int(height * scale)
    resized_img = pil_img.resize((new_width, new_height), Image.ANTIALIAS) # Create the resized image
    result = Image.new('RGB', (target_width, target_height), background_color) # Create the result image with the correct background color
    result.paste(resized_img, ((target_width - new_width) // 2, (target_height - new_height) // 2)) # Paste the resized image into the result image
    return result
im = Image.open('test.png')  # Open the image
target_width = 384  # Desired width
target_height = 256  # Desired height
background_color = (0, 0, 0)  # Black background
im_result = expand_to_rectangle(im, target_width, target_height, background_color)
im_result.save('result.png')

for i in range(0,6):
    list = []
    ligne = int(i/3)
    colonne = i%3
    print(ligne,colonne)
    pixeldl = ligne*128
    pixeldc = colonne*128
    print(pixeldl,pixeldc,":")
    for y in range(pixeldl,pixeldl+128):
        for x in range(pixeldc,pixeldc+128):
            r,g,b = im_result.getpixel((x,y))
            #assigne sur la liste les valeurs de r,g,b pour dans la colonne i
            list += (r,g,b)
open.write()