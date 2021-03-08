import bz2


def inflate(data):
    d = bz2.decompress(data)
    print(d)
    print(d.decode("ascii"))


def inflateFromFile(file):
    f = open(file, "rb")
    content = f.read()
    f.close()
    print(content)
    inflate(content)


# BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08

f = open("un.txt", "rb")
content = f.read()
f.close()
bz2.decompress(content)

# only works well on python2...