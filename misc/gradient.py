from PIL import Image

x = 1024
y = 768

img = Image.new('RGBA', (x,y))

for i in range(x):
    for j in range(y):
        img.putpixel((i,j), (100*i, j//4, 100))
        
img.save('gradient.png')