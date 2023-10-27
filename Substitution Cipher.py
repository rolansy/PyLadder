import string
d={}
data=""
x=""
for i in range(len(string.ascii_letters)):
    d[string.ascii_letters[i]]=string.ascii_letters[i-2]
print(d)
with open ("cfile.txt") as f:
    while True:
        c=f.read(1)
        x+=c
        if not c:
            print("End of File")
            break
        if c in d:
            data+=d[c]
        else:
            data+=c
print(x)
print(data)