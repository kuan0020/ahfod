from PIL import Image,ImageDraw
from random import randint as rint

def random_gradient(name):
    x = 1024
    y = 768
    img = Image.new("RGB", (x,y), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # r,g,b = rint(0,255), rint(0,255), rint(0,255)
    r, g, b = 178, 34, 34
    # dr = (rint(r-65, r+65) - r)/y
    # dg = (rint(g-65, g+65) - g)/y
    # db = (rint(b-65, b+65) - b)/y
    color2 = [0,81,79]
    dr = color2[0]
    dg = color2[1]
    db = color2[2]
    
    dr = rint(dr-50, dr)/400
    dg = rint(dg-50, dg)/400
    db = rint(db-50, db)/400
    
    print(dr, dg, db)
    
    for i in range(x):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,y), fill=(int(r),int(g),int(b)))

    img.save(name+".png", "PNG")

if __name__ == "__main__":
    for name in range(1):
        random_gradient(str(name))