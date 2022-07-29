def check_num(input_array, number):
    l = len(input_array)
    if l == 0:
        return False
    if input_array[0] == number:
        return True
    return check_num(input_array[1:],number)
print(check_num([1,2,3],1))
print(check_num([1,-3,2,3],-3))
print(check_num([0,2,3],0))
print(check_num([2,8,-5,7,-9],7))
print(check_num([2,8,-5,7,-9],-7))
