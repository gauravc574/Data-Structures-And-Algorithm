def sum_of_array(input_array):
    l = len(input_array)
    sumx = 0
    if  l == 0:
        return 0
    
    return  input_array[0] + sum_of_array(input_array[1:])
    
print(sum_of_array([1,2,3]))
print(sum_of_array([1]))
