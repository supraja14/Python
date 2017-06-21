#program to find LCM

def lcm(x,y):
	if x>y:
		max=x
	else:
		max=y
	while(True):
		if((max%x==0) and (max%y==0)):
			lcm=max
			break
		max=max+1
	return lcm
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print ("LCM is", lcm(a,b))