from utils import linear_gradient, bezier_gradient, temp_img
from PIL import Image, ImageDraw
import subprocess, os

def top_down(x, y, colors):
    img = Image.new("RGB", (x, y), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    if len(colors) == 1:
        end = "#FFFFFF"
        gradient_dict = linear_gradient(colors[0], end, n=y)
        r = gradient_dict['r']
        g = gradient_dict['g']
        b = gradient_dict['b']
        

    else:
        colors = tuple(colors)
        bezier = bezier_gradient(colors, n_out=y)
        gradient_dict = bezier['gradient']
        r = gradient_dict['r']
        g = gradient_dict['g']
        b = gradient_dict['b']

    for i in range(len(gradient_dict['r'])):
        draw.line((0, i, x, i), fill=(r[i], g[i], b[i]))

    for i in range(len(gradient_dict['r']), y):
        draw.line((0, i, x, i), fill=(r[-1], g[-1], b[-1]))

    return img


def left_right(x, y, colors):
    img = Image.new("RGB", (x, y), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    if len(colors) == 1:
        end = "#FFFFFF"
        gradient_dict = linear_gradient(colors[0], end, n=x)
        r = gradient_dict['r']
        g = gradient_dict['g']
        b = gradient_dict['b']

    else:
        colors = tuple(colors)
        bezier = bezier_gradient(colors, n_out=x)
        gradient_dict = bezier['gradient']
        r = gradient_dict['r']
        g = gradient_dict['g']
        b = gradient_dict['b']

    for i in range(len(gradient_dict['r'])):
        draw.line((i, 0, i, y), fill=(r[i], g[i], b[i]))

    for i in range(len(gradient_dict['r']), x):
        draw.line((i, 0, i, y), fill=(r[-1], g[-1], b[-1]))

    return img

def plasma_regular(x,y):
    opath = 'plasma_regular.png'
    cmd = 'convert -size ' + str(x) + 'x' + str(y) + ' plasma: '+ opath
    subprocess.call(cmd, shell=True)
    return temp_img(opath)
    
def plasma_color(x,y, colors):
    opath = 'plasma_color.png'
    cmd = 'convert -size ' + str(x) + 'x' + str(y) + ' plasma:'
    
    for x in range(len(colors)-1):
        cmd = cmd + str(colors[x]) + '-'
    
    cmd = cmd + str(colors[-1]) + ' ' + opath
    
    subprocess.call(cmd, shell=True)
    return temp_img(opath)
    
    
# def 

if __name__ == "__main__":
    
    colors = ["#96ceb4", "#ff6f69", "#ffcc5c" ]
    img = left_right(['#fff'],1200, 1200)
    img.show()

