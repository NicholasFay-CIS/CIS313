from sys import argv
#Nicholas Fay 
#Lab 1
#CIS 313 

class Node(object):
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
            
    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data

    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data
            
    def getNext(self):
        # return the "next" data field
        return self.__next

class Queue(object):
    def __init__(self):
        #Initializes the head and tail values to be None
        self.__head = None
        self.__tail = None
    
    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        #This adds an item to the queue, if the queue is empty adds the new node to be the head and tail
        node = Node(newData, None)
        #if the queue is empty
        if (self.isEmpty()):
            #set the head and tail to be the node
            self.__head = node
            self.__tail = node
        #else we want to set the tails next to be the new node, and update the tail.
        self.__tail.setNext(node)
        self.__tail = node
        return None


    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue  
        # This removes a value from the queue, it will return the values that has been removed
        if (self.isEmpty()):
            return None
        #temp variable for the head value
        temp = self.__head
        #updates the head value
        self.__head = temp.getNext()
        return temp.getData()

    
    def isEmpty(self):
        # Check if the Queue is empty
        #if the head and the tail are None then the queue is empty
        if (self.__head is None and self.__tail is None):
            return True
        return False


    def printQueue(self):
        # Loop through your queue and print each Node's data
        if (self.__head is None and self.__tail is None):
            return None
        #Prints every node that contains a value in the queue
        while node != None:
            #node is set to the head value
            node = self.__head
            print("{}".format(node.getData()))
            #get the next node in the linked list
            node = node.getNext()
        return None

class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null
        self.__top = None
    
    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top
        node = Node(newData, None)
        #if the stack is empty, the top should be the new node
        if (self.__top == None):
            self.__top = node
        else:
        #set the the new node and update top to be the new node. 
            node.setNext(self.__top)
            self.__top = node
        return None

    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        if (self.__top == None):
            return None
        #temp node to hold the data from top value
        temp_node = self.__top.getData()
        #updates self.__top
        self.__top = self.__top.getNext()
        return temp_node
 
    def isEmpty(self):
        # Check if the Stack is empty
        if(self.__top is None):
            return True
        return False
        
    def printStack(self):
        # Loop through your stack and print each Node's data
        # our first node is the top node
        node = self.__top
        #if the top node is none then the stack is empty
        if (self.__top == None):
            print("There is nothing in the stack")
            return None
        #prints all nodes that contain values that have been stored on the stack
        while node != None:
            print("{}".format(node.getData()))
            #get the next node in the stack
            node = node.getNext()
        return None
 
def main(argv):
    # Create a Scanner that reads system input
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:
        # Loop over the scanner's input
        # For each line of the input, send it to isPalindrome()
        # If isPalindrome returns true, print "This is a Palindrome." 
        # Otherwise print "Not a Palindrome."
        #skip the header line telling how many items we need to check
        file_ob.next()
        #go through every line in the file (besides the first one that we skipped)
        for line in file_ob:
            test = isPalindrome(line)
            #if palindrome returns false
            if (test == False):
                print("Not a Palindrome")
            #if palindrome returns true
            if (test == True):
                print("This is a Palindrome")
    return None

def isPalindrome(s):
    """
    str -> bool
    Function determines if a string is a palindrome or not. 
    It strips all new line characters, spaces and turns 
    uppercase letters to lower case letters. It adds all the elements of the string
    to both the stack and the queue, then pops and dequeus from the data structures
    and compares the values to find any mis matches. 
    isPalindrome("hello")
    >>> False

    isPalindrome("556655")
    >>> True

    isPalindrome("Helleh")
    >>> True
    """
    #creates a stack and a queue
    myStack = Stack() 
    myQueue = Queue()
    #strips all uneeded characters from the string
    s = s.strip()
    #gets rid of all white spaces
    s = s.replace(" ", "")
    #turns all the uppercase characters to lower case
    s = s.lower()
    #adds all items of the string to the queue and stack
    for i in range(len(s)):
        myStack.push(s[i])
        myQueue.enqueue(s[i])
    #checks the values that the stack poped and queue dequeued if they are the same.
    for i in range(len(s)//2):
        x = myStack.pop()
        y = myQueue.dequeue()
        #if the two items are different, return false 
        if (x != y):
            return False
    return True
   
def isPalindromeEC(s):
    # Implement if you wish to do the extra credit.
    return None

if __name__ == "__main__":
    main(argv)
