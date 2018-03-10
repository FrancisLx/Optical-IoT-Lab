from PIL import Image
import colorsys
import os
def getNames(folder):
    imageList = os.listdir(folder)
    imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return imageList

imageList = getNames(r"C:\Users\Francis\Desktop\face database")
count = 0

for img in imageList:
    im = Image.open(img)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    fig_rgb = Image.new('RGB',(width, height))
    fig_hsv = Image.new('RGB',(width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x,y]
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            if r>95 and g>40 and b>20 and (abs(r-g) > 15) and r>g and r>b:
                fig_rgb.putpixel([x, y],(255, 255, 255))
            else:
                fig_rgb.putpixel([x, y],(0,0,0))
            if h>=0 and h<=0.25 and s>=0.15 and s<=0.9:
                fig_hsv.putpixel([x, y],(255, 255, 255))
            else:
                fig_hsv.putpixel([x, y], (0, 0, 0))
    count += 1
    fig_rgb.save(r'C:\Users\Francis\Desktop\face database\%d.jpg'%count)
    fig_hsv.save(r'C:\Users\Francis\Desktop\face database\%d.jpg'%(count*100))
