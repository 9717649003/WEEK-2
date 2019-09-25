n=int(input())

item=input()
b=item.split()
a=[]
for i in b:
    a.append(int(i))
c=[]
c=a[n::-1]
for j in range(n-1):
    print(a[j]+c[j],end=" ")
print(a[n-1]+c[n-1],end="")