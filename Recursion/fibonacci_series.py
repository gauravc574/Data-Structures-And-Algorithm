def fibonacci_series(n):
    if n == 1:
        return 1
    fibonacci_series(n -1) + fibonacci_series(n-2)
    print(n )
fibonacci_series(5)

