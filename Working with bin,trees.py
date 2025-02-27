# CONVERTING TUPLES INTO BINARY TREES

# creating the tree
class Tree_Node():
    def __init__(self,key):
        self.key= key # root node in each tree or subtree
        self.left=None   # attributes of the object node
        self.right=None


# given a tuple of format (left_subtree, key , right_subtree) we can change that into a tree format

def tuple_to_tree(data):  # change from tuple to Node
    if isinstance(data,tuple) and len(data)==3:
        Node=Tree_Node(data[1]) #created the first node
        Node.left= tuple_to_tree(data[0])
        Node.right= tuple_to_tree(data[2])
    elif data==None: #i.e no node is created
        Node=None
    else:
        Node=data

    return Node 

# given a tree change it to the tuple expression format

def tree_to_tuple(Tree): #output= tuple
    list_1=['left', 'root_key' , 'right']  # first form the list then return the tuple
    if isinstance(Tree, Tree_Node):
        list_1[1]= Tree.key # the root node
        list_1[0]= tree_to_tuple(Tree.left)  #the left part will be the tree now  not tree.key.left bc that is an integer
        list_1[2]= tree_to_tuple(Tree.right) #the right part will be the tree now
    elif Tree==None:   # node is none 
        return None
    else:  #if the data inside is an integer then u will just return it
        return Tree
    
    return tuple(list_1)

# TESTING WITH DIFFERENT TESTCASES

Tree1= Tree_Node(4)                 # Tree =    4
Node1= Tree_Node(6)                     #     6   7
Node2= Tree_Node(7)                     #   8       9

Tree1.left= Node1
Tree1.right= Node2

Node1.left= Tree_Node(8)
Node2.right= Tree_Node(9)    
# print(isinstance(Node2.key,Tree_Node))  ####output = False bc u r accessing the intenal thing

Tuple1= tree_to_tuple(Tree1)
print(Tuple1)

Tree1= tuple_to_tree(Tuple1)
print(Tree1)
