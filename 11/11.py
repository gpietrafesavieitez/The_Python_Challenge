from PIL import Image
cave = Image.open("cave.jpg")
pix = cave.load()
test = Image.new("RGB", cave.size)
for i in range(0, cave.width, 2):
    for j in range(0, cave.height, 2):
        # get rgb
        even = pix[i, j]
        odd = pix[i + 1, j + 1]

        test.putpixel((i, j), even)
        test.putpixel((i + 1, j + 1), odd)
test.save("test.jpg")