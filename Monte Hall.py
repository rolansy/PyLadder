import random
door={}
gdoor={}
swap=0
dontswap=0
x=random.randint(0, 2)
door[x]="BMW"
for i in range(3):
    if(i==x):
        continue
    else:
        door[i]="Goat"

