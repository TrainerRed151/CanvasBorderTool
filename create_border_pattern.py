from PIL import Image
from tqdm import tqdm
import sys


def read_image():
    if len(sys.argv) < 2:
        print('Please provide a file.')
        exit()

    filename = sys.argv[1]
    print(f'Reading image {filename}')
    return Image.open(filename), filename


def calculate_offset(im):
    h_off = int(0.1*im.height)
    w_off = int(0.1*im.width)

    return max(h_off, w_off)


def create_border_image(im, offset):
    print('Creating new image...')
    w2 = im.width + 2*offset
    h2 = im.height + 2*offset

    i2 = Image.new('RGB', (w2, h2))
    _fill_border(im, i2, offset)

    return i2


def _fill_border(im, i2, offset):
    for h in tqdm(range(im.height), ascii=True, desc='Copying original pixels'):
        for w in range(im.width):
            v = im.getpixel((w, h))
            i2.putpixel((w+offset, h+offset), v)

    for h in tqdm(range(im.height), ascii=True, desc='Creating left/right borders'):
        for w in range(offset):
            vl = im.getpixel((w, h))
            i2.putpixel((offset-w, h+offset), vl)

            vr = im.getpixel((im.width-w-1, h))
            i2.putpixel((im.width+offset+w, h+offset), vr)

    for w in tqdm(range(im.width), ascii=True, desc='Creating top/bottom borders'):
        for h in range(offset):
            vt = im.getpixel((w, h))
            i2.putpixel((w+offset, offset-h), vt)

            vb = im.getpixel((w, im.height-h-1))
            i2.putpixel((w+offset, im.height+offset+h), vb)


def main():
    im, filename = read_image()
    offset = calculate_offset(im)
    i2 = create_border_image(im, offset)
    im.close()

    print('Saving new image...')
    base, ext = filename.split('.')
    i2.save(f'{base}_borders.{ext}')
    i2.close()

    print(f'New file created at: {base}_borders.{ext}')


if __name__ == '__main__':
    main()
