num = int(input("Enter a number: "))

flag = False

def is_prime(n, flag):
    if n == 1:
        print(n, "is not a prime")
    elif n > 1:
        for k in range(2, n):
            if (n % k) == 0:
                flag = True 
                break
        if flag:
            print(n, "is not a prime")
        else:
            print(n, "is a prime")    

is_prime(n=num, flag=flag)