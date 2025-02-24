# find the start and ending index of a number in a list of numbers arranged in increasing order?
def position(cards,query,mid): # help us know where the card lies
    if (cards[mid]==query):
        return 'found'
    elif (cards[mid]>query): #look in the left slice
        return 'left'
    elif (cards[mid]<query): #look in the right slice
            return 'right'

def locate_cards(cards,query,position):     
    def locate_0():   #to locate the starting point
        lo=0
        hi=len(cards)-1
        list_0=-1
        while (lo<=hi):
            mid=(lo+hi)//2
            res=position(cards,query,mid)
            if res=='left': #look in the left slice
                hi=mid-1
            elif res=='right': #look in the right slice
                lo=mid+1
            elif res=='found': # the card is in the middle but we need to check prior existence
                if (mid>1 and cards[mid-1]!=query):
                    list_0=mid
                elif (mid>1 and cards[mid-1]==query): #check in the left slice then 
                    hi=mid-1
        return list_0

    def locate_1(): #to locate for the ending point
        lo=0
        hi=len(cards)-1
        list_1=-1
        while (lo<=hi):
            mid=(hi+lo)//2
            res=position(mid)
            if (res=='left'): #look in the left slice
                hi=mid-1
            elif (res=='right'): #look in the right slice
                lo=mid+1
            elif (res=='found'):
                if mid>-1 and cards[mid+1]!=query:
                    list_1=mid
                elif mid>-1 and cards[mid+1]==query: #look in the right slice
                    lo=mid+1
        return list_1
        
    list_0= locate_0()
    list_1= locate_1()
    lists=[list_0,list_1]
    return lists

# test_case=[{cards:query},expected_output]
# Test_cases=[
#     [ {(1,2,3,4,5,6,6,6,6,6,6,6,6,7,7,8,9,10):1},[0,0] ],#query postioned on first,
#     [ {(1,2,3,4,5,6,6,6,6,6,6,6,6,7,7,8,9,10):10},[17,17] ], #query on last place
#     [ {(1,2,3,4,5,6,6,6,6,6,6,6,6,7,7,8,9,10):6},[5,12]], # repetitive query
#     [ {(1,2,3,4,5,6,6,6,6,6,6,6,6,7,7,8,9,10):11},[-1,-1]] ,#query not there
#     [ {(1,2,3,4,5,7,8,8,8,9,10):7},[5,5]] #query on the middle
# ]

# # Testing
# print("hi")
# for test_case in Test_cases:
#     test=test_case[0]
#     for key,value in test.items():
#         cards=key
#         query=value
#         Output=locate_cards(cards,query,position)
#         if (test_case[1]==Output):
#             print("passed")   
#         else:
#             print("\t FAILED")
#             print(f"{cards}, {query}")
#             print(f"\tExpected output: {test_case[1]}")  
#             print(f"\t Output obtained: {Output}")

print(locate_cards((1,2,3,4,5,6,6,6,6,6,6,6,6,7,7,8,9,10),1,position))