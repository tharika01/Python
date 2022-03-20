def fib_series(num: int) -> int:
    if 0 <= num <= 1:
        return num
    first, second = 0, 1
    for i in range(num):
        third = first + second
        second = first
        first = third
        #print("{} {}".format(first,second))
        #print(third)
    return third


num = int(input("Enter number of terms in fibonaci series: "))
res = fib_series(num)
print(res)
#for i in range ():    
#    print(i, fib_series(i))

