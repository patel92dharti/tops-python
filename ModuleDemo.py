import UDF

while True:

    print("*"*30)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibpnacci")
    print("5. Prime")
    print("6. Pattern")
    print("7. Exit")
    print("*"*30)

    choice=int(input("Enter Your Choice : "))
    print("*"*30)

    if choice==1:
        a=int(input("Enter Value : "))
        UDF.OddEven(a)
        print("*"*30)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.MaxOfTwo(a,b)
        print("*"*30)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.MaxOfThree(a,b,c)
        print("*"*30)
    elif choice==4:
        a=int(input("Enter Value : "))
        UDF.Fibonacci(a)
        print("*"*30)
    elif choice==5:
        a=int(input("Enter Value : "))
        UDF.Prime(a)
        print("*"*30)
    elif choice==6:
        a=int(input("Enter Value : "))
        UDF.Pattern(a)
        print("*"*30)
    else:
        print("Good Bye")
        print("*"*30)
        break
