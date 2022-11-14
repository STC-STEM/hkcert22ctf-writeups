import base64

src = open("wickbase64.txt", "r")
dest = open("wick.wick", "wb")

base64.decode(src, dest)
