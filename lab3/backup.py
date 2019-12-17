import math

class MaxHeap(object):

    def __init__(self, size):
        # finish the constructor, given the following class data fields:
        self.__maxSize = size
        self.__length = 0
        self.__myArray = [None] * size

	''' free helper functions '''
    def getHeap(self):
        return self.__myArray   

    def getMaxSize(self):
        return self.__maxSize
    
    def setMaxSize(self, ms):
        self.__maxSize = ms

    def getLength(self):
        return self.__length
    
    def setLength(self, l):
        self.__length = l

    def getParent(self, index):
        if(index == 0):
            return 0
        if(index == 1 or index == 2):
            return 0
        if(index % 2 == 0):
            return (index-2)/2 
        if(index % 2 != 0):
            return(index-1)/2

    def getRightChild(self, index):
        child = 2*index + 2
        return child

    def getLeftChild(self, index):
        child = 2*index + 1
        return child

    ''' Required Methods '''
    def insert(self, data):
    	# Insert an element into your heap.
    	# When adding a node to your heap, remember that for every node n, 
    	# the value in n is greater than or equal to the values of its children, 
    	# but your heap must also maintain the correct shape.
        if(self.__length == self.__maxSize):
            print("Max sized already hit...")
            return
        heap_arr = self.__myArray
        heap_arr[self.__length] = data
        parent = self.getParent(self.__length)
        #print("parent is {}".format(parent))
        self.__length += 1
        while(parent >= 0):
            largest_index = self.__heapify(parent)
            #print(largest_index)
            parent = self.getParent(parent)
            #print("the largest index is {}".format(largest_index))
            if(largest_index == -2):
                parent = self.getParent(self.__length-1)
            if(parent == 0):
                self.__heapify(parent)
                return
            """
            if(parent == 0):
                self.__heapify(parent)
                return
            #print("The updated parent is {}".format(parent))
            """
        return 

    def maximum(self):
        # return the value in the heap
        if(self.__length != 0):
            return self.__myArray[0]
        return None

    def extractMax(self):
        # remove and return the minimum value in the heap
        if (self.__length == 0):
            print("Heap underflow..."),
            return None
        #sets the max to be the roo
        Max = self.__myArray[0]
        #sets the root to be the last index of the list 
        self.__myArray[0] = self.__myArray[self.__length-1]
        self.__myArray[self.__length-1] = None
        self.__length -= 1
        '''
        leftchild = self.getLeftChild(0)
        rightchild = self.getRightChild(0)
        if(self.__myArray[leftchild] > self.__myArray[rightchild]):
            largest_child = leftchild
        else:
            largest_child = rightchild
        '''
        #print("The swapped root is {}".format(self.__myArray[0]))
        #print("The largest child of the root is {}".format(self.__myArray[largest_child]))
        index_swap = 0
        while(index_swap <= (self.__length)):
            index_swap = self.__heapify(index_swap)
            if(index_swap == -1):
                return Max
            #print(self.__length)
            #print(index_swap)
            if(index_swap == 0):
                return Max
            if(index_swap == self.__length-1):
                return Max
            """
            leftchild = self.getLeftChild(largest_child)
            print("after the heapify, the left child is {}".format(self.__myArray[leftchild]))
            rightchild = self.getRightChild(largest_child)
            print("after the heapify, the right child is {}".format(self.__myArray[rightchild]))
            if(self.__myArray[leftchild] > self.__myArray[rightchild]):
                largest_child = leftchild
            else:
                largest_child = rightchild
            print("The largest child is {}".format(self.__myArray[largest_child]))
            """

            #if(self.getLeftChild(largest_child) > self.__length and self.getRightChild(largest_child) > self.__length):
                #return Max
        return Max
    
    def __heapify(self, p_index):  
        arr = self.__myArray
        #get left child index if they exist
        leftchild = self.getLeftChild(p_index)
        #get right child index
        rightchild = self.getRightChild(p_index)
        #if the left child 
        #print(type(rightchild))
        #print(rightchild)
        if(self.__length > self.__maxSize):
            return -2
        if(leftchild < self.__length and arr[leftchild] > arr[p_index]):
            largest = leftchild
        else:
            largest = p_index
        if(rightchild < self.__length and arr[rightchild] > arr[largest]):
            largest = rightchild
        if(largest != p_index):
            temp = arr[p_index]
            temp2 = arr[largest]
            arr[p_index] = temp2
            arr[largest] = temp
            return largest
        return -1








    # You probably want to turn them into a method.