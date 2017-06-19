num=int(raw_input("Enter a number"))
sum=0
n=num

while num!=0:
	rem=num%10
	sum=sum*10+rem
	num=num/10
if sum==n:
	print "is a  palindrome"
else:
	print "is Not a palindrome"