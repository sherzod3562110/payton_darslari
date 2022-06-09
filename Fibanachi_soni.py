n=int(input())
f1=1
f2=1
fk=0
if n<=2:
    print(1)
elif n>=3:
    for i in range(2,n,1):
        fk=f1+f2
        f1=f2
        f2=fk
    print(fk)
