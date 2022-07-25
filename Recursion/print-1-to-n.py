def print_n(n):
    if n == 0:
        return
    
    print_n(n-1)
    print(n)
    return
print_n(10023)
