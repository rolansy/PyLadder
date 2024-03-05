
def ver(s):
	if '@' not in s:
		print('a')
		return False
	if '.' not in s[s.index('@'):]:
		print('b')
		return False
	if not s[s.index('@')+1:s[s.index('@'):].index('.')].isalpha():
		print('c')
		return False
	if not s[s[s.index('@'):].index('.')+1:].isalpha():
		print('d')
		return False
	return True

x=input("Enter Email : ")
t=ver(x)
if t:
	print("Valid Email")
else: print("Invalid Email")