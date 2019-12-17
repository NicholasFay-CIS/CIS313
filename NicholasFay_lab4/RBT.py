
# BinarySearchTree is a class for a binary search tree (BST)
# when called, a BST is initialized with no root and size 0.
# size keeps track of the number of nodes in the tree
#Nicholas Fay


from Node import RB_Node
from time import sleep
class RedBlackTree:
    # initialize root and size
    def __init__(self):
        self.root = None
        self.size = 0
        self.sentinel = RB_Node(None,None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    '''
    Free Methods
    '''

    def sentinel(self):     
        return self.sentinel

    def root(self):
        return self.root

    def __iter__(self):
        # in-order iterator for your tree
        return self.root.__iter__()

    def getKey(self, key):
        # expects a key
        # returns the key if the node is found, or else raises a KeyError

        if self.root:
            # use helper function _get to find the node with the key
            res = self._get(key, self.root)
            if res: # if res is found return the key
                return res.key
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    
    def getNode(self, key):
        # expects a key
        # returns the RB_Node object for the given key
        
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function _get receives a key and a node. Returns the node with
    # the given key
    def _get(self, key, currentNode):
        if currentNode is self.sentinel: # if currentNode does not exist return None
            #print("couldnt find key: {}".format(key))
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            # recursively call _get with key and currentNode's leftChild
            return self._get( key, currentNode.leftChild )
        else: # key is greater than currentNode.key
            # recursively call _get with key and currentNode's rightChild
            return self._get( key, currentNode.rightChild )

    
    def __contains__(self, key):
        # overloads the 'in' operator, allowing commands like
        # if 22 in rb_tree:
        # ... print('22 found')

        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.getNode(key)
        if z.leftChild is self.sentinel or z.rightChild is self.sentinel:
            y = z
        else:
            y = z.findSuccessor()
        
        if y.leftChild is not self.sentinel:
            x = y.leftChild
        else:
            x = y.rightChild

        #if x is sentinel it will be adjusted later in the delete
        #is x not sentinel?

        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x

        if y is not z:
            z.key = y.key

        if y.color == 'black':
            if x is self.sentinel:
                #if x is the sentinel then fixup y
                self._rb_Delete_Fixup(y)
            else:
                self._rb_Delete_Fixup(x)

    def traverse(self, order = "in-order", top = -1):
        # Same a BST traverse
        if top is -1:
            top = self.root
            last_call = True
        
        last_call = False

        if top is not self.sentinel:
            if order == "in-order":
                self.traverse(order, top = top.leftChild)
                print(top.key),
                self.traverse(order, top = top.rightChild)

            if order == "pre-order":
                #prints the top key
                print(top.key),
                self.traverse(order, top = top.leftChild)
                self.traverse(order, top = top.rightChild)

            if order == "post-order":
                self.traverse(order, top = top.leftChild)
                self.traverse(order, top = top.rightChild)
                print(top.key),

        if last_call:
            print

    '''
    Required Methods Begin Here
    '''

    def insert(self, key, root = None):
        # add a key to the tree. Don't forget to fix up the tree and balance the nodes.
        """
        int -> None
        this function inserts a node into a function
        tree.insert(10)
        >>>
        tree.insert(20)
        >>>
        tree.insert(30)
        >>>
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        """
        if (self.root == None):
            #if the root is none, establish the value is the root of the tree
            new_node = RB_Node(key)
            self.root = new_node
            new_node.parent = self.sentinel
            new_node.leftChild = self.sentinel
            new_node.rightChild = self.sentinel
            return 
        #this sets the root
        if (root == None):
            root = self.root

        #new_node is made of RB_Node(key)
        #insert on the right side of the tree
        if(root.key < key):
            #if the roots right child is None
            if (root.rightChild == self.sentinel):
                new_node = RB_Node(key)
                root.rightChild = new_node
                new_node.parent = root
                new_node.leftChild = self.sentinel
                new_node.rightChild = self.sentinel
                self._rbInsertFixup(new_node)
                return 
            else:
                #recursion right
                self.insert(key, root.rightChild)
        #insert on the left side of the tree
        if(root.key > key):
            if(root.leftChild == self.sentinel):
                new_node = RB_Node(key)
                root.leftChild = new_node
                new_node.parent = root
                new_node.leftChild = self.sentinel
                new_node.rightChild = self.sentinel
                self._rbInsertFixup(new_node)
                return
            else:
                #recursion left side
                self.insert(key, root.leftChild)
        

    def _rbInsertFixup(self, z):
        """
        This function fixes the tree according to red black tree properties.
        This function is called by insert and calls both right and left rotate.
        (self, Node obj) -> None
        self._rbInsertFixup(10)
        >>>
        self._rbInsertFixup(15)
        >>>
        self._rbInsertFixup(20)
        >>>
        """
        # write a function to balance your tree after inserting
        while(z != self.root and z.parent.color == 'red'):
            #sleep(.5)
            #z.print_()
            #z.color = 'red'
            if(z.parent == z.parent.parent.leftChild):
                #z.parent.print_()
                new_node = z.parent.parent.rightChild
                if(new_node.color == 'red'):
                    #new_node.print_()
                    z.parent.color = 'black'
                    new_node.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if(z == z.parent.rightChild):
                        #z.print_()
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rightRotate(z.parent.parent)

            else:
                if(z.parent == z.parent.parent.rightChild):
                    #print("True")
                    new_node = z.parent.parent.leftChild
                    if(new_node.color == 'red'):
                        #new_node.print_()
                        z.parent.color = 'black'
                        new_node.color = 'black'
                        z.parent.parent.color = 'red'
                        z = z.parent.parent
                    else:
                        if(z == z.parent.leftChild):
                            #z.print_()
                            z = z.parent
                            self.rightRotate(z)
                        z.parent.color = 'black'
                        z.parent.parent.color = 'red'
                        self.leftRotate(z.parent.parent)
            self.root.color = 'black'
            return 

    def _rb_Delete_Fixup(self, x):
        # receives a node, x, and fixes up the tree, balancing from x.
        """
        (self, Node obj) -> None
        This function fix's up the tree after deleting. This is called by delete.
        This function calls both left and right rotate.
        self._rb_Delete_Fixup(10)
        >>>
        self._rb_Delete_Fixup(20)
        >>>
        self._rb_Delete_Fixup(30)
        >>>
        """
        #If the x is not the root and the color is black
        while(x != self.root and x.color == 'black'):
            if(x == x.parent.leftChild):
                new_node = x.parent.rightChild
                #if the node is red
                if(new_node.color == 'red'):
                    new_node.color = 'black'
                    x.parent.color = 'red'
                    self.leftRotate(x.parent)
                    new_node = x.parent.rightChild
                if(new_node.leftChild.color == 'black' and new_node.rightChild.color == 'black'):
                    new_node.color == 'red'
                    x = x.parent
                    #if the new nodes right child is black
                elif(new_node.rightChild.color == 'black'):
                    new_node.leftChild.color = 'black'
                    new_node.color = 'red'
                    self.rightRotate(new_node)
                    new_node = x.parent.rightChild
                else:
                    new_node.color = x.parent.color
                    x.parent.color = 'black'
                    new_node.rightChild.color = 'black'
                    self.leftRotate(x.parent)
                    x = self.root
                #what if none of the cases above are hit
            else:
                #if x is not its parents left child
                    new_node = x.parent.leftChild
                    if(new_node.color == 'red'):
                        new_node.color = 'black'
                        x.parent.color = 'red'
                        self.rightRotate(x.parent)
                        new_node = x.parent.leftChild
                    if(new_node.rightChild.color == 'black' and new_node.leftChild.color == 'black'):
                        new_node.color = 'red'
                        x = x.parent
                        #if the new nods left child is black
                    elif(new_node.leftChild.color == 'black'):
                        new_node.rightChild.color = 'black'
                        new_node.color = 'red'
                        self.leftRotate(new_node)
                        #After rotate, set newnode to be x's parents leftchild
                        new_node = x.parent.leftChild
                    else:
                        new_node.color = x.parent.color
                        x.parent.color = 'black'
                        new_node.leftChild.color = 'black'
                        self.rightRotate(x.parent)
                        x = self.root
            #set x to be a black node
            #return
        x.color = 'black'
        return 

    def leftRotate(self, currentNode):
        """
        (Node obj) -> None
        This function does the left rotation, this function is called by delete fixup and 
        insert fixup
        self.leftRotate(2)
        >>>
        self.leftRotate(4)
        >>>
        self.leftRotate(10)
        >>>
        """
        # perform a left rotation from a given node
        #if the currentNode does not have a right child 
        if(currentNode.hasRightChild() == False):
            return
        #new node is the right child of the current node
        new_node = currentNode.rightChild
        #swap the current nodes right child with the new_nodes left child 
        currentNode.rightChild = new_node.leftChild
        #if the new node does not have a left child
        #new_node.leftChild != None
        #if(new_node.hasLeftChild()):
        if(new_node.leftChild != self.sentinel):
            #set its left childs parent to be the current node
            new_node.leftChild.parent = currentNode
        #else set the new nodes parent to be the current nodes parent
        new_node.parent = currentNode.parent 
        #if the current node does not have a parent
        if(currentNode.parent == self.sentinel):
            #set the root to be the new node
            self.root = new_node
        #if the current node is equal to the current nodes parents left child 
        elif (currentNode == currentNode.parent.leftChild):
            #parents left child now becomes new node
            currentNode.parent.leftChild = new_node
        else:
            #parents right child now become new node
            currentNode.parent.rightChild = new_node
        #the new nodes left child is the current node
        new_node.leftChild = currentNode
        #the current nodes parent is not the new node
        currentNode.parent = new_node
        return

    def rightRotate(self, currentNode):
        """
        (Node obj) -> None
        This function fixes the tree by doing the appropriate rotations.
        It is called by delete fix up and insert fixup
        self.rightRotate(10)
        >>>
        self.rightRotate(20)
        >>>
        self.rightRotate(30)
        >>> 
        """
        # perform a right rotation from a given node
        if(currentNode.hasLeftChild() == False):
            return
        #new node is the right child of the current node
        new_node = currentNode.leftChild
        #swap the current nodes right child with the new_nodes left child 
        currentNode.leftChild = new_node.rightChild
        #if the new node does not have a left child
        #new_node.leftChild != None
        #if(new_node.hasRightChild()):
        if(new_node.rightChild != self.sentinel):
            #set its left childs parent to be the current node
            new_node.rightChild.parent = currentNode
        #else set the new nodes parent to be the current nodes parent
        new_node.parent = currentNode.parent 
        #if the current node does not have a parent
        if(currentNode.parent == self.sentinel):
            #set the root to be the new node
            self.root = new_node
        #if the current node is equal to the current nodes parents left child 
        elif (currentNode == currentNode.parent.rightChild):
            #parents left child now becomes new node
            currentNode.parent.rightChild = new_node
        else:
            #parents right child now become new node
            currentNode.parent.leftChild = new_node
        #the new nodes left child is the current node
        new_node.rightChild = currentNode
        #the current nodes parent is not the new node
        currentNode.parent = new_node
        return


    def search(self, Node):
        """
        (int) -> int or bool
        This function is called in main. Its purpose is to tell if the node exists in the tree
        If the node exists it will print found. It also returns the key return the key.
        self.search(10)
        >>> False
        self.search(20)
        >>> Found: 20 
        self.search(5)
        >>> False
        """
        x = self.__contains__(Node)
        if x == True:
            print("Found: {}".format(Node))
            return Node
        else:
            print("Not Found")
            return Node

#Optional handy methods that you can imagine can start here



