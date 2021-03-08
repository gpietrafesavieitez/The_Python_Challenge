from PIL import Image
oxygen = Image.open("oxygen.png")
size = oxygen.size
width = size[0]
height = size[1]
pixels = oxygen.load()
pix = pixels[0,50]
string = ""
# (0,50) => (629,50)
# block = 7 pixels
for i in range(0, 607, 7):
    string += chr(pixels[i, 50][0])

print(string)

list = [105, 110, 116, 101, 103, 114, 105, 116, 121]

str = ""
for l in list:
    str += chr(l)

print(str)