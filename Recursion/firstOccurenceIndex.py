                                                        
def first_occurence(input_array, number):              
    l = len(input_array)
    if l == 0:                                        
        return -1                                     
    elif input_array[0] == number:
        return 0
    #return first_occurence(input_array[1:],number)
    smallerList = input_array[1:]
    isSmallerListChecked = first_occurence(smallerList, number)
    if isSmallerListChecked<0:
        return isSmallerListChecked
    return isSmallerListChecked+1# 

print(first_occurence([1,1,1,1,1],1))
print(first_occurence([1,1,1,1,1],1))
print(first_occurence([0,1,2,1,2],2))
print(first_occurence([0,3,2,1,3],3))
print(first_occurence([1,1,1,1,3],3))
print(first_occurence([1,1,1,1,3],5))


##def first_occurence1(input_array, number, start_index):
##    l = len(input_array)
##
##    if 
