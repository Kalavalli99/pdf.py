from PIL import Image

image1 = Image.open('image1.png')
image2 = Image.open('image2.png')
image3 = Image.open('image3.png')
image4 = Image.open('image4.png')
 
im1 = image1.convert('RGB')
im2 = image2.convert('RGB')
im3 = image3.convert('RGB')
im4 = image4.convert('RGB')

imagelist = [im2,im3,im4]

im1.save("converted.pdf",save_all=True, append_images=imagelist)
