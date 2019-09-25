#FINDING THE SMALLER NUMBER

a=input("enter string : ")
i=0
b=""
c=""
while(a[i]!=" "):
    b+=a[i]
    i+=1
for j in range(i+1,len(a)):
    c+=a[j]
d=int(b)
e=int(c)
print( (d, e) [d > e],end="") 