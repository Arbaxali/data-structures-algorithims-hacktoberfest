def fib(n):
    a = 0
    b = 1
    cin = 0
    while(cin < n):
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            cin = c
           
            print(c)

num = int(input("enter the num ")) 
fib(num)       