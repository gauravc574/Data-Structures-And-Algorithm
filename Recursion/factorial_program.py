#base case is given as absence of it will lead to Recursion Error
#RecursionError: maximum recursion depth exceeded(approx 1000-1022)

'''
Maths behind recursion is Principal Mathematical Induction(PMI)


'''

def factorial(n):
    if n == 0: #base(trivial) case for breaking
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number whose factorial needs to be calculated : "))

print(factorial(n))
 
