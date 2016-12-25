from PIL import Image
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()
    imgname = sys.argv[1]
    img = Image.open(imgname, 'r')
    new_img = img.resize((img.width * 10, img.height * 10))
    for x in range(new_img.width):
        print("{}/{}".format(x, new_img.width))
        for y in range(new_img.height):
            color = img.getpixel((x // 10, y // 10))
            new_img.putpixel((x, y), color)
    new_img.save(imgname + "-10.png")
