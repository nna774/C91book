from PIL import Image
import sys
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

piet_colors = [
    "222",
    "211", "221", "121", "122", "112", "212",
    "200", "220", "020", "022", "002", "202",
    "100", "110", "010", "011", "001", "101"
]


def to_piet_color(x, y, img):
    def get_mapped(mapped):
        return [0, 192, 255][int(mapped)]

    def calc_diff(r, g, b, rp, gp, bp):
        c1 = sRGBColor(r / 255.0, g / 255.0, b / 255.0)
        c2 = sRGBColor(get_mapped(rp) / 255.0,
                       get_mapped(gp) / 255.0,
                       get_mapped(bp) / 255.0)
        c1 = convert_color(c1, LabColor)
        c2 = convert_color(c2, LabColor)
        delta = delta_e_cie2000(c1, c2)
        return delta
    r, g, b = img.getpixel((x, y))
    pre_diff = 100000000
    decided_color = 0
    for (rp, gp, bp) in piet_colors:
        diff = calc_diff(r, g, b, rp, gp, bp)
        if diff < pre_diff:
            decided_color = (get_mapped(rp), get_mapped(gp), get_mapped(bp))
            pre_diff = diff
    img.putpixel((x, y), decided_color)

if __name__ == "__main__":
    imgname = sys.argv[1]
    img = Image.open(imgname, 'r')
    for x in range(img.width):
        for y in range(img.height):
            to_piet_color(x, y, img)
    img.save("out.png")
