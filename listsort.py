get=input()
a=get.split()
a=[int(s) for s in a]
gett=input()
b=gett.split()
b=[int(t) for t in b]
a.extend(b)
sort=sorted(a)
out=set(sort)
output=sorted(out)
print(*output,sep=' ')