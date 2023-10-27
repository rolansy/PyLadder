import string
d={}
for i in range(len(string.ascii_letters)):
    d[string.ascii_letters[i]]=string.ascii_letters[i-2]
print(d)