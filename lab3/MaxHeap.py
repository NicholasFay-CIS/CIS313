#Nicholas Fay
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
        """
        int -> int
        This function takes in a index and returns its parent index
        self.getParent(2)
        >>> 0
        self.getParent(1)
        >>> 0
        self.getParent(3)
        >>> 1
        """
        #if the root was given
        if(index == 0):
            return 0
        #if the roots children are given
        if(index == 1 or index == 2):
            return 0
        #if the index is even
        if(index % 2 == 0):
            return (index-2)/2 
        #if the index is odd
        if(index % 2 != 0):
            return(index-1)/2

    def getRightChild(self, index):
        """
        int -> int
        This function takes in a index and returns its right child index
        self.getRightChild(0)
        >>> 2
        self.getRightChild(1)
        >>> 4
        self.getRightChild(2)
        >>> 6
        """
        child = 2*index + 2
        return child

    def getLeftChild(self, index):
        """
        int -> int
        This function takes in a index and returns its left child index
        self.getRightChild(0)
        >>> 1
        self.getRightChild(1)
        >>> 3
        self.getRightChild(2)
        >>> 5
        """
        child = 2*index + 1
        return child

    ''' Required Methods '''
    def insert(self, data):
        """
        int -> None
        This function inserts data into the heap and heapifys it after insertion
        heap.insert(10)
        >>> 
        heap.insert(20)
        >>>
        heap.insert(30)
        >>>
        """
    	# Insert an element into your heap.
    	# When adding a node to your heap, remember that for every node n, 
    	# the value in n is greater than or equal to the values of its children, 
    	# but your heap must also maintain the correct shape.
        # checks to see if the max size has been hit
        if(self.__length == self.__maxSize):
            print("Max sized already hit...")
            return
        heap_arr = self.__myArray
        heap_arr[self.__length] = data
        #get parent data
        parent = self.getParent(self.__length)
        #Update length counter
        self.__length += 1
        # while loop to bubble up when heapifying
        while(parent >= 0):
            largest_index = self.__heapify(parent)
            #get the parent
            parent = self.getParent(parent)
            #If it is the last item in the heap size, get its parent and heapify till it hits the root
            if(largest_index == -2):
                parent = self.getParent(self.__length-1)
            if(parent == 0):
                self.__heapify(parent)
                return
        return 

    def maximum(self):
        """
        None -> int
        this function returns the max number without side affects to the heap
        heap.maximum()
        >>> 20
        heap.maximum()
        >>> 30
        heap.maximum()
        >>> 40
        """
        # return the value in the heap
        if(self.__length != 0):
            return self.__myArray[0]
        print("No maximum value")
        return None

    def extractMax(self):
        """
        None -> int
        This function calls extract max in MaxHeap and returns the maximum number with a side affect to the heap
        heap.extractMax()
        >>> 20
        heap.extractMax()
        >>> 30
        heap.extractMax()
        >>> 18
        """
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
        
        #While loop to bubble down when removing the root 
        #if the index is == -1 then just return the max, as its parent is largest
        index_swap = 0
        while(index_swap <= (self.__length)):
            index_swap = self.__heapify(index_swap)
            if(index_swap == -1):
                return Max
            #if the index is 0 return the max
            #if the index is equal to the length minus 1 return max
            if(index_swap == 0):
                return Max
            if(index_swap == self.__length-1):
                return Max
            
        #return Max
        return Max
    
    def __heapify(self, p_index):
        """
        int -> int
        This function swaps the parent with the greatest child and returns the greatest index
        self.__heapify()
        >>> 1
        self.__heapify()
        >>> -1
        self.__heapify()
        >>> 2
        """  
        arr = self.__myArray
        #get left child index if they exist
        leftchild = self.getLeftChild(p_index)
        #get right child index
        rightchild = self.getRightChild(p_index)
        #if the left child 
        #print(type(rightchild))
        #if the length is at the max size
        if(self.__length > self.__maxSize):
            return -2
        #check to see if the left is greater 
        if(leftchild < self.__length and arr[leftchild] > arr[p_index]):
            largest = leftchild
        else:
            largest = p_index
        #check to see if the right is greater
        if(rightchild < self.__length and arr[rightchild] > arr[largest]):
            largest = rightchild
        #swap the values of the parent and the largest value
        if(largest != p_index):
            temp = arr[p_index]
            temp2 = arr[largest]
            arr[p_index] = temp2
            arr[largest] = temp
            return largest
        return -1








    # You probably want to turn them into a method.