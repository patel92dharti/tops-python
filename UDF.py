def OddEven(a):
    if a%2==0:
        print(a," Is Even")
    else:
        print(a," Is Odd")

def MaxOfTwo(a,b):
    if a>b:
        print(a," Is Max")
    else:
        print(b," Is Max")

def MaxOfThree(a,b,c):
    if a>b:
        if a>c:
            print(a," Is Max")
        else:
            print(c," Is Max")
    elif b>c:
        print(b," Is Max")
    else:
        print(c," Is Max")

def Fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()

def Prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n," Is Not Prime")
                break
        else:
            print(n," Is Prime")
    else:
        print(n," Is Not Prime")
        

def Pattern(n):
    for i in range(1,n):
        print("*"*i)
