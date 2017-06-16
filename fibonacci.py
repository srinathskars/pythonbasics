fo = open("foo.txt", "r+")
str=fo.read(100)
print("read string is:", str)
fo.close()
