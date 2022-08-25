from PIL import Image

filename = '/Users/brian/Pictures/disco_diffusion_art/Garden(0)_0.png'

im = Image.open(filename)

h_off = int(0.1*im.height)
w_off = int(0.1*im.width)
offset = max(h_off, w_off)

w2 = im.width + 2*offset
h2 = im.height + 2*offset
i2 = Image.new('RGB', (w2, h2))

for h in range(im.height):
    for w in range(im.width):
        v = im.getpixel((w, h))
        i2.putpixel((w+offset, h+offset), v)

for h in range(im.height):
    for w in range(offset):
        vl = im.getpixel((w, h))
        i2.putpixel((offset-w, h+offset), vl)

        vr = im.getpixel((im.width-w-1, h))
        i2.putpixel((im.width+offset+w, h+offset), vr)

for h in range(offset):
    for w in range(im.width):
        vt = im.getpixel((w, h))
        i2.putpixel((w+offset, offset-h), vt)

        vb = im.getpixel((w, im.height-h-1))
        i2.putpixel((w+offset, im.height+offset+h), vb)

im.close()
base, ext = filename.split('.')
import ipdb; ipdb.set_trace()
i2.save(f'{base}_borders.{ext}')
i2.close()
