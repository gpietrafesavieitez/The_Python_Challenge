from urllib import request, parse


def iterate(n):
    url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?"
    url_start = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
    c = 0
    while c < n:
        resp = request.urlopen(url_start)
        if resp.code == 200:
            html = resp.read().decode("utf-8")
            num = ""
            for letter in html:
                if letter.isnumeric():
                    num += letter
            params = {"nothing": num}
            querystring = parse.urlencode(params)
            url_start = url_base + querystring
            print("[" + str(c) + "] => " + num + " => " + html)
            c += 1


iterate(400)
# 8022
