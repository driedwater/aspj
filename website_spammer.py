import urllib.request
i = 25
while i != 0:
    fp = urllib.request.urlopen("http://127.0.0.1:5000/register")
    mybytes = fp.read()

    mystr = mybytes.decode("utf-8")
    fp.close()
    print(mystr)
    i -= 1