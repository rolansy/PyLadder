import random
door={}
gdoor=[]
swap=0
dontswap=0
x=random.randint(0, 2)
door[x]="BMW"
for i in range(3):
    if(i==x):
        continue
    else:
        door[i]="Goat"
        gdoor.append(i)
c=int(input("Enter your Choice : "))
dooropen=random.choice(gdoor)
while(dooropen==c): #so that at the end, dooropen != c
    dooropen=random.choice(gdoor)
print("Open Door : Goat : ",dooropen)
ch=input("Do you want to swap [y/n]: ")
if ch=='y':
    if door[c]=="Goat":
        print("Player Won")
        swap+=1
    else:
        print("Player Lost")
else:
    if door[c]=="Goat":
        print("Player Lost")
    else:
        print("Player Lost")
        dontswap+=1
    

