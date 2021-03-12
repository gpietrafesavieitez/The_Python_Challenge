
with open("test2.gif", "wb") as gif:
    gfx = open("evil2.gfx", "rb")
    data = gfx.read()
    for i in range(2, len(data), 5):
        gif.write(chr(data[i]).encode("utf-8"))
    gfx.close()
gif.close()

data = open('evil2.gfx', 'rb').read()

for i in range(5):
 open('%d.jpg' %i, 'wb').write(data[i::5])




