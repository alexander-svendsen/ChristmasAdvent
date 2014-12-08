from PIL import Image
import operator
from collections import  defaultdict


im = Image.open("image.png")
pix = im.load()
width, height = im.size


color_dict = defaultdict(int)
for x in xrange(width):
    for y in xrange(height):
        color_dict[pix[x, y]] += 1


print sorted(color_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[9]

