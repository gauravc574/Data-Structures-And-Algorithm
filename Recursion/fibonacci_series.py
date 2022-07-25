def fibonacci_series(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci_series(n-1) + fibonacci_series(n-2)
    print(n) 
    
print(fibonacci_series(4))

