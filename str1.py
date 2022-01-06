str=input('enter the string:')
a=[]
str= str.split()
#print(str)
for i in str:
    if i not in a:
        a.append(i)
print(a)