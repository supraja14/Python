a=int(input())
b=int(input())
s=[]
import math
def perfect_sq(n):
    return n == int(math.sqrt(n)) ** 2
for i in range(a,b):
  if perfect_sq(i)==True:
    s.append(i)
print (*s,sep=',')