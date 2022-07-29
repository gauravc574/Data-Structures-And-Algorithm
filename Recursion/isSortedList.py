
def is_sorted(input_list):
    
    l = len(input_list)
    if l == 0 or l == 1:
        
        return True
    if input_list[0] > input_list[1]:
        return False
##    return is_sorted(input_list[1:])
    smallerList = input_list[1:]
    isSmallerListSorted = is_sorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False

print(is_sorted([1,2,3,4,5,6]))
print(is_sorted([1,22,3,4,5,60]))
print(is_sorted([0,2,0,0,0,2]))







def is_sorted1(input_list, start_index):
    l = len(input_list)

    if start_index == l or start_index == l-1: #completed the list case and base case
        return True
    if input_list[start_index] > input_list[start_index + 1]:
        return False
    isSmallerPartSorted = is_sorted1(input_list,start_index + 1)
    return isSmallerPartSorted
    

print(is_sorted1([1,2,3,4,5,6],0))
print(is_sorted1([1,22,3,4,5,60],0))
print(is_sorted1([0,2,0,0,0,2],0))
