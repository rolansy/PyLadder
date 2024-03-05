import re

def ver(s):
    em=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(em,s):
        return True
    return False

x=input("Enter Email : ")
t=ver(x)
if t:
	print("Valid Email")
else: print("Invalid Email")