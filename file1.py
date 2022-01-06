fo = open('abc.txt', "r+")
print("Name of the file: ", fo.name)

hi = "hello python is fun for everyone"
fo.write(hi)

str = fo.readlines()
print("The read string is\n", str)
fo.close()