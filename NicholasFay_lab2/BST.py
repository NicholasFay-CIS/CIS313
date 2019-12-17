from Node import Node
from time import sleep
class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        """
        None -> node obj
        this returns the root of the node
        tree.getRoot()
        >>> 30
        ^ if the root is 30
        """
        # Private Method, can only be used inside of BST.
        return self.__root
    def __findNode(self, data, node = None):
        """
        (int) -> Node obj
        This find the node in a given tree
        This is called by functions (exists) and (delete)
        self.__findNode(20)
        if the node is in the tree
        >>> < some memory address>
        if the node is not in the tree 
        >>> None
        """
        # Private Method, can only be used inside of BST.
        # Search tree for a node whose data field is equal to data.
        # Return the Node object
        #if the root is none return none
        if(self.__root == None):
            return None
        #if node is none update node
        if(node == None):
            node = self.__root
        #if the nodes value is the data, return the node
        if (node.getData() == data):
            #print("The data found is {}".format(self.__root.getData()))
            return self.__root
        #print("the root node being used is {}".format(node.getData()))
        #if the data is greater than the root
        if(node.getData() < data):
            if(node.getRightChild() == None):
                #if there is no node on the right side of the tree
                return None
            #if the roots right childs data equals the data
            if(node.getRightChild().getData() == data):
                #print("found the node")
                #print("being compared to data {}" .format(data))
                #print("The right child is {}".format(node.getRightChild()))
                #print("The right child has a value of {}".format(node.getRightChild().getData()))
                return node.getRightChild()
            else:
                #print("checking to the right")
                #pass the root as the new node to traverse from 
                return self.__findNode(data, node.getRightChild())
        #if the nodes data is greater than data     
        if(node.getData() > data):
            if(node.getLeftChild() == None):
                #if there is no node on the left side of the tree 
                return None
            #if the left child data is the data
            if(node.getLeftChild().getData() == data):
                return node.getLeftChild()
            else:
                #print("checking to the left")
                return self.__findNode(data, node.getLeftChild())
        return None

    def exists(self, data):
        """
        int -> bool
        This function returns true if the value exists as a node otherwise it returns false
        tree.exists(30)
        >>> True
        tree.exists(10000000)
        >>> False
        tree.exists(1111)
        >>> False
        """
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        #call to findNode function
        node_found = self.__findNode(data)
        if(node_found == None):
            return False
        return True

    def insert(self, data, root = None):
        """
        int -> None
        this function inserts a node into a function
        tree.insert(10)
        >>>
        tree.insert(20)
        >>>
        tree.insert(30)
        >>>
        """
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        if (self.__root == None):
            #if the root is none, establish the value is the root of the tree
            new_node = Node(data)
            self.__root = new_node
            #print("Inserting the root {}".format(data))
            #print("Root Node is {}".format(new_node))
            return None
        #this sets the root
        if (root == None):
            root = self.__root

        new_node = Node(data)
        #insert on the right side of the tree
        if(root.getData() < new_node.getData()):
            #if the roots right child is None
            if (root.getRightChild() == None):
                root.setRightChild(new_node)
                new_node.setParent(root)
                #print("inserted {}".format(data))
                #print("the node is {}".format(new_node))
                return 
            else:
                #recursion right
                self.insert(data, root.getRightChild())
        #insert on the left side of the tree
        if(root.getData() > new_node.getData()):
            if(root.getLeftChild() == None):
                root.setLeftChild(new_node)
                new_node.setParent(root)
                #print("inserted {}".format(data))
                #print("the node is {}".format(new_node))
                return
            else:
                #recursion left side
                self.insert(data, root.getLeftChild())

    def delete(self, data):
        """
        int -> None
        This function deletes a node in the binary search tree. If it does not exist then it will print cant delete
        tree.delete(-1)
        >>> Data does not exist
        tree.delete(30)
        >>>
        tree.delete(40)
        >>>
        """
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree.
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove 
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor when there are two children
        #print("The root is {} ".format(self.__root.getData()))
        if(self.exists(data) == False):
            print("Data does not exist")
            return None
        # If you find the node and ...
        if(self.exists(data) == True):
            Node = self.__findNode(data)
            #if the delete method calls on the root
            if(data == self.__root.getData()):
                if(Node.getRightChild() == None and Node.getLeftChild() == None):
                    self.__root = None
                    return
                #swap values with the successor
                successor = self.__findSuccessor(Node)
                if(Node.getRightChild() != None and Node.getLeftChild() == None and Node.getRightChild().getRightChild() == None and Node.getRightChild().getLeftChild() == None):
                    #if hte node has a right child and not a left child and its right child has no children
                    Node.setData(Node.getRightChild().getData())
                    Node.setRightChild(None)
                    return
                if(Node.getLeftChild() != None and Node.getRightChild() == None and Node.getLeftChild().getRightChild() == None and Node.getLeftChild().getLeftChild() == None):
                    if(successor == None):
                        Node.setData(Node.getLeftChild().getData())
                    Node.setLeftChild(None)
                    return
                #if the successor is None set x to be none if it is not None set x to the successors data
                if(successor != None):
                    x = successor.getData()
                if(successor == None):
                    x = None
                if(successor != None):
                    successor.setData(data)
                #if the right child is None
                if(Node.getRightChild() == None):
                    #if the left childs children are not none
                    if(Node.getLeftChild().getRightChild() != None and Node.getLeftChild().getRightChild() != None):
                        #set the grandchild to be the right grandchild
                        grandchild = Node.getLeftChild().getRightChild()
                    else:
                        #set it to be the left grandchild
                        grandchild = Node.getLeftChild().getLeftChild()
                    Node.setData(grandchild.getData())
                    #if the nodes left childs left child is not none
                    if(Node.getLeftChild().getRightChild() == None and Node.getLeftChild().getLeftChild() != None):
                        #set the root to be the left child
                        self.__root = Node.getLeftChild()
                    Node.getLeftChild().setParent(None)
                    Node.getLeftChild().setRightChild(None)
                    #if the right grandchild is the one that is not None
                    if(Node.getLeftChild().getRightChild() != None and Node.getLeftChild().getLeftChild() == None):
                        Node.getLeftChild().setRightChild(None)
                        return
                    return
                #Node has the data of successor.
                Node.setData(x)
                #if the successor does not have a right child
                if(successor.getRightChild() == None):
                    #if its chldren are none
                    if(Node.getRightChild().getRightChild() == None and Node.getRightChild().getLeftChild() == None and Node.getLeftChild().getRightChild() == None and Node.getLeftChild().getLeftChild() == None):
                        Node.setRightChild(None)
                        successor.setParent(None)
                        return 
                    #if the successors right child and left child are none
                    if(successor.getRightChild() == None and successor.getLeftChild() == None):
                        Node.setData(x)
                        #if the successors parent is the Node
                        if(successor.getParent() == Node):
                            Node.setRightChild(None)
                            return
                        #if the successors parent is not None then set its left child to None and its parent to None
                        successor.getParent().setLeftChild(None)
                        successor.setParent(None)
                        return
                    #if the successors left child is Not none
                    if(successor.getLeftChild() != None):
                        successor.getParent().setLeftChild(None)
                        successor.setParent(None)
                        return
                    # if the nodes child has no children, set the nodes right child to be none
                    if(Node.getRightChild().getRightChild() == None and Node.getRightChild().getLeftChild() == None and Node.getLeftChild().getRightChild() == None and Node.getLeftChild().getLeftChild() == None):
                        Node.setRightChild(None)
                        return
                    #if the successors right child and left child is None
                    if(successor.getRightChild() == None and successor.getLeftChild() == None):
                        Node.setRightChild(None)
                        return
                    #else set its parents left child to be None
                    successor.getParent().setLeftChild(None)
                    return
                #if the successor node does have a right child
                if(successor.getRightChild() != None):
                    #set the successors right child parent to be the successors parent
                    successor.getRightChild().setParent(successor.getParent())
                    successor.getParent().setRightChild(successor.getRightChild())  
                    return 
            #if the node we are deleting is not a root
            x = self.__findSuccessor(Node)
            if(x == None):
                Node.getParent().setRightChild(None)
                return
            #A
            #if the node has no children
            if(Node.getRightChild() == None and Node.getLeftChild() == None):
                if(Node.getParent().getData() < Node.getData()):
                    #if is a right child
                    Node.getParent().setRightChild(None)
                else:
                    #if is a left child
                    Node.getParent().setLeftChild(None)  
                return
            #B
            #if the node has a right child but not a left
            if(Node.getRightChild() != None and Node.getLeftChild() == None):
                parent = Node.getParent()
                child = Node.getRightChild()
                ##changed right to left ###########
                #if the parents data is less than node data
                if(parent.getData() < Node.getData()):
                    #set the right child and parents accordingly
                    parent.setRightChild(child)
                    child.setParent(parent)
                    return
                #if this is not the case and parent is greater
                parent.setLeftChild(child)
                child.setParent(parent)
                return
            #if the node has a left child but not a right
            if(Node.getLeftChild() != None and Node.getRightChild() == None):
                parent = Node.getParent()
                child = Node.getLeftChild()
                if(parent.getData() < Node.getData()):
                    #if the parents data is greater than the nodes data
                    parent.setRightChild(child)
                    child.setParent(parent)
                    return
                #else if do 
                parent.setLeftChild(child)
                child.setParent(parent)
                return
            #if we are trying to delete the root
            #if the node we want to delete has two children.    
            #C
            if(Node.getRightChild() != None and Node.getLeftChild() != None):
                #case 1
                #find the successor
                successor = self.__findSuccessor(Node)
                Node.setData(successor.getData())
                successor.setData(data)
                #check the successors right child 
                if(successor.getRightChild() == None):
                    if(successor.getParent().getData() > successor.getData()):
                        successor.getParent().setRightChild(None)
                        return
                    successor.getParent().setLeftChild(None)
                    return
                #case 2
                #if the successors right child is not None
                if(successor.getRightChild() != None):
                    #set the right child to be the right child of the successors parent
                    successor.getRightChild().setParent(Node)
                    #eliminate ties the successor has to parent and right children.
                    successor.setParent(None)
                    successor.setRightChild(None)
                    #successor.getParent().setLeftChild(successor.getRightChild()) 
                    return
        return None

    def __findSuccessor(self, aNode):
        """
        Node obj -> Node obj
        This function finds and returns the successor
        if the successor is none return none
        this is called by otherfunctions such as delete
        self.__findSuccessor(Node)
        >>> Node (successor Node)
        >>> None if the node does not have a successor
        """
        #continuously traverses till it finds the most left child on the right side of the tree
        if(aNode == self.__root):
            #if the node is the root and the root has no chldren
            if(self.__root.getRightChild() == None and self.__root.getLeftChild() == None):
                return None
            #if the root only has a left child
            if(self.__root.getRightChild() == None and self.__root.getLeftChild() != None):
                return None
        if(aNode.getRightChild()):
            #if the nodes right child is not None
            successor = aNode.getRightChild()
            #update successor
            while(successor.getLeftChild()):
                successor = successor.getLeftChild()
            return successor
        #if there is no right child 
        if(aNode.getRightChild() == None):
            successor = aNode.getParent()
            #if the successor's left child is the node. return the node
            if(successor.getLeftChild() == aNode):
                return aNode
            while(successor.getParent()):
                #if there are multiple of the same values, there is no successor
                if(successor.getParent().getData() == aNode.getData()):
                    print("multiple nodes with the same value")
                    break
                #if the successors left child is the node, return the successor
                if(successor.getLeftChild() == aNode):
                    return successor
                if(successor.getData() < aNode.getData()):
                    #put a return
                    return successor.getParent()
            #if the root is the successor
            if(successor == self.__root):
                if(aNode.getData() > self.__root.getData()):
                    #then no successor
                    return None

            return successor
                
    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node in a specified order
        """
        str, Node obj -> None
        This prints all the orders of the tree.
        self.traverse("inorder", 30 (root obj))
        >>> 10 20 30 40
        self.traverse("preorder", 30 (root obj))
        >>> 30 20 10 40
        self.traverse("postorder", 3 (root obj))
        >>> 10 20 40 30
        """
        if top is not None:
            #if the order is preorder
            if order == "preorder":
                print(top.getData()),
                self.traverse(order, top.getLeftChild())
                self.traverse(order, top.getRightChild())
                
            elif order == "inorder":
                #if the order is inorder
                # your code here, remove pass
                self.traverse(order, top.getLeftChild())
                print(top.getData()),
                self.traverse(order, top.getRightChild())


            elif order == "postorder":
                #if the order is postorder
                # your code here, remove pass
                self.traverse(order, top.getLeftChild())
                self.traverse(order, top.getRightChild())
                print(top.getData()),
            
            else:
                print("Error, order {} undefined".format(order))



