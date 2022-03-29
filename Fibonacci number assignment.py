fibonacci_number = int(input("Enter the fibonacci number "))
a=0
b=1
if fibonacci_number==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,fibonacci_number) :
        c=a+b
        a=b
        b=c
        print(c)