def factorial(n: int)->int:
    """
    get the factorial of nmbers until 36
    """
    if n <= 1:
        return 1
    fact = 2
    for x in range (3,n+1):
        fact = fact * x
    return fact

    
for i in range(0, 35):
    fact = factorial(i)
    print("{} {}".format(i,fact))
