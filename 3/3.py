f = open("3.txt", "r")
text = f.read()


def find_guarded(text):
    msg = ""
    for i in range(len(text)):
        if i + 7 < len(text) and i > 0:
            if text[i - 1].islower() and text[i].isupper() and text[
                i + 1].isupper() and text[i + 2].isupper() and text[i + 3].islower() and \
                    text[i + 4].isupper() and text[i + 5].isupper() and \
                    text[i + 6].isupper() and text[i + 7].islower():
                msg += text[i + 3]
    return msg


print(find_guarded(text))
