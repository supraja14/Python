n=int(input())
n1 = 0

n2 = 1

count = 0
while count < nterms:
	print(n1,end=' , ')

	nth = n1 + n2n
	n1 = n2
	n2 = nth
	count += 1