# """ YOU ARE ASKED TO BUILD A DATA STRUCTURE THAT CONTAINS 100 MILL USERS INFO(NAME,USERNAME,EMAIL), WAP THAT CLD INSERT,
#  FIND,UPDATE AND LIST ALL USERS GIVEN USER NAME AND IT IS SORTED BASED ON USERNAME."""

# Database=[]   # the data base is a list of dictionaries

# class Database2():
#     def __init__(self,User_name,Name,Email): 
#         self.username= User_name
#         self.name= Name
#         self.email= Email
#         self.User={self.username:[self.name, self.email]} 
#     def Insert(self,User=self.User): 
#         #user info in a dict, {username:[Name,email]} bc usernames are unique and used for sorting
#         # to add the info to the database while keeping the order of sorted
#         lo=0
#         hi=len(Database)-1
#         while (lo<=hi):
#             mid=(lo+hi)//2 # gives the middle dictionary's index
#             if (self.username>Database[hi].keys()): #comparing the 2 keys and find which one is on the behind 
#             Database.insert(hi+1,User)
#             break
#             elif (self.username<Database[lo].keys()): #bc the elts are unique u won't have an equal 
#                 if (lo==0):
#                     Database.insert(0,User)
#                     break
#                 else:
#                     Database.insert(lo-1,User)
#                     break
#             else:
#                 if (num>Database[mid] and num<Database[mid+1]):
#                     Database.insert(mid+1,num)
#                     break
#                 elif (num>Database[mid]): #it is found to the right
#                     lo=mid+1
#                 elif (num<Database[mid]): # it is found to the left
#                     hi=mid-1
#         return Database

#     def Find(self,username):
#         lo=0
#         hi=len(Database)-1
#         while (lo<=hi):
#             mid=(lo+hi)//2 #the index
#             if (username==Database[mid].keys()):
#                 return Database[mid]  # let it return the dictionary
#             elif (username<Database[mid].keys()): # user found to the left
#                 hi=mid-1
#             elif (username>Database[mid].keys()): # uset found to the right
#                 lo=mid+1
#             else:
#                 return "User not in the database."
        
#     def Update(self,old_username,new_username=old_username,Name,Email): # New username is optional
#         Result= Find(old_username)
#         if (Result=="User not in the database."):
#             return "The user is not found in the data base."
#         else: # if the user is found
#             for user_na in Result.keys(): #to update the username
#                 user_na=new_username
#             for information in Result.values():#if u want to edit the name and email which is in a list
#                 information[0]=Name
#                 information[1]=Email
#             Updated_user={user_na:information}
#         if (new_username!=old_username):
#             Database.remove(find(old_username))
#             Inserting=Insert(Updated_user)
#             return Inserting
#         else:
#             Database[old_username]= information
#         return Database       




#     def List_users(self):
#         pass

dist={
    'hey':'me',
    'love':'you',
}

print(list(dist.keys())[0])