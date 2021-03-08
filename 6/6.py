import zipfile

zip_obj = zipfile.ZipFile("channel.zip")


def get_comments():
    # 46145
    next = "90052"
    comments = ""
    while next != "46145":
        fileInfo = zip_obj.getinfo(next + ".txt")
        comments += fileInfo.comment.decode("utf-8")
        file = zip_obj.open(next + ".txt")
        content = file.read().decode("utf-8")
        print(content)
        separate = content.split(" ")
        for item in separate:
            if item.isnumeric():
                next = item
        file.close()
    print(comments)

get_comments()



