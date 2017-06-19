def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y

print("CALCULATOR")
print("Select an operation:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

ch=input("Enter your choice: ")

num1=int (input("Enter first number: "))
num2=int (input("Enter second number: "))

if ch==1:
	print(add(num1,num2))
elif ch==2:
	print(sub(num1,num2))
elif ch==3:
	print(mul(num1,num2))
elif ch==4:
	print(div(num1,num2))
else:
	print("Invalid")