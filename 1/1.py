import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def translate(text):
    msg = ""
    for letter in text:
        posAbc = string.ascii_lowercase.find(letter)
        if posAbc != -1:
            index = posAbc + 2
            if index < len(string.ascii_lowercase):
                character = string.ascii_lowercase[index]
                msg += character
            else:
                i = posAbc - len(string.ascii_lowercase)
                i = i + 2
                character = string.ascii_lowercase[i]
                msg += character
        else:
            msg += letter
    return msg


print(translate(text))