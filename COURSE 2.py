""" YOU ARE ASKED TO BUILD A DATA STRUCTURE THAT CONTAINS 100 MILL USERS INFO(NAME,USERNAME,EMAIL), WAP THAT CLD INSERT,
 FIND,UPDATE AND LIST ALL USERS GIVEN USER NAME AND IT IS SORTED BASED ON USERNAME."""

#what i learnt if u say dict.keys() it returns a list of the keys in the dict saying dict_keys(list of keys)
#to access individual key u need to convert it to a list or tuple and access the index

Database=[]   # the data base is a list of dictionaries

class Database2():
    def __init__(self,User_name,Name,Email): 
        self.username= User_name
        self.name= Name
        self.email= Email
        self.User={self.username:[self.name, self.email]} 
    def Insert(self,User=None):
        #u can't say self.User as a parameter bc it isn't defined so u set it to None 
        #user info in a dict, {username:[Name,email]} bc usernames are unique and used for sorting
        # to add the info to the database while keeping the order of sorted
        User= User or self.User #if User=None i.e false then it will take self.user else it is true so it remains the same
        lo=0
        hi=len(Database)-1
        while (lo<=hi):
            mid=(lo+hi)//2 # gives the middle dictionary's index
            if self.username>list(Database[hi].keys())[0]: #comparing the 2 keys and find which one is on the behind 
                Database.insert(hi+1,User)
                break
            elif (self.username<  list(Database[lo].keys())[0]: #bc the elts are unique u won't have an equal 
                if (lo==0):
                    Database.insert(0,User)
                    break
                else:
                    Database.insert(lo-1,User)
                    break
            else:
                if self.username >list(Database[mid].keys())[0] and self.username<list(Database[mid+1].keys())[0]:
                    Database.insert(mid+1,self.username)
                    break
                elif (self.username>list(Database[mid].keys())[0]: #it is found to the right
                    lo=mid+1
                elif (self.username<list(Database[mid].keys())[0]: # it is found to the left
                    hi=mid-1
        return Database

    def Find(self,username):
        lo=0
        hi=len(Database)-1
        while (lo<=hi):
            mid=(lo+hi)//2 #the index
            if username==list(Database[mid].keys())[0]:
                return Database[mid]  # let it return the dictionary
            elif username<list(Database[mid].keys())[0]: # user found to the left
                hi=mid-1
            elif username>list(Database[mid].keys())[0]: # user found to the right
                lo=mid+1
            else:
                return "User not in the database."
        
    def Update(self,old_username,new_username=old_username,Name,Email): # New username is optional
        Result= self.Find(old_username) # to maek sure u r using the method for that object specific to this class and object
        if (Result=="User not in the database."):
            return "The user is not found in the data base."
        else: # if the user is found
            for user_na in Result.keys(): #to update the username
                user_na=new_username
            for information in Result.values():#if u want to edit the name and email which is in a list
                information[0]=Name
                information[1]=Email
            Updated_user={user_na:information} 
        if (new_username!=old_username):
            Database.remove(Result)
            Inserting=self.Insert(Updated_user) # the data base will be updated
            return Inserting
        else:
            Database[old_username]= information
        return Database       

    def List_users(self):
        for Data in Database:
            print(Data)
