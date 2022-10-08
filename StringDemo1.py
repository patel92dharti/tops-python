s=input("Enter String:")

sp=0
n=0
w=1
c=0

for i in s:
    c=c+1
    if i.isspace():
        sp=sp+1
        w=w+1
    elif i.isnumeric():
        n=n+1

print("Number Of Space : ",sp)
print("Number Of Numeric : ",n)
print("Number Of Word : ",w)
print("Number Of Character : ",c)
