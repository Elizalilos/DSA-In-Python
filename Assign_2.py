""" Rotated lists problem u are given a list whose elements are unique and rotated
(the last element is taken from the original sorted list and added in the front)
 find the min amt of time it was rotated. """ 

# find which side is sorted and the first entry to the sorted list is in unsorted

def count_rotation(rotated_list):
    num_rotate=0 # not being rotated
    original=sorted(rotated_list) # not .sort() bc it wont give a new list it will update the old
    lo=0
    hi= len(rotated_list)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if rotated_list[lo]<rotated_list[mid]: #left is sorted
            lo=mid+1
        elif rotated_list[lo]>rotated_list[mid]: #left is unsorted,not = bc unique nums
            hi=mid-1
        elif rotated_list[mid]==original[0]: #Original 1st entry
            num_rotate=mid
            break

    return num_rotate

#Test_case=[list, expected_output]

Test_cases=[
    [[9,10,1,2,3,4,5,6,7,8],2] , #10 elts with 2 rotation
    [[],0], #empty list can't be rotated hence 0 will be returned
    [[1],0], # a list with one element is the same
    [[1,2,4,5,6,7],0], # a list rotated n times will give original back, so does no rotation
    [[2,3,4,5,6,1],5] # a list rotated n-1 times
]

# testing

for test_case in Test_cases:
    res=count_rotation(test_case[0])
    if res==test_case[1]:
        print("Pass")
    else:
        print("\t Failed".upper())