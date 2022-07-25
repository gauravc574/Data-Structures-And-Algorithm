#Square Pattern
"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
    4444
    4444
    4444
    4444
"""
def square_pattern(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(n ,end="")
            j += 1
        print()
        i += 1
print(square_pattern(4))


