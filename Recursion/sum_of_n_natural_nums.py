def sum_n(n):
    if n == 0 :
        return 0
    #smallOutput = sum_n(n - 1)
    #output = smallOutput + n
    return n + sum_n(n-1)

print(sum_n(3))
print(sum_n(5))
