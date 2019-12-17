from MaxHeap import MaxHeap

class pQueue(object):
    def __init__(self,size) :
        # Build the Constructor
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        """
        int -> None
        This function calls insert from MaxHeap
        heap.insert(20)
        >>>
        heap.insert(30)
        >>>
        heap.insert(50)
        >>>
        """
        self.__myHeap.insert(data)
        
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
        return self.__myHeap.maximum()
    
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
        return self.__myHeap.extractMax()

    def isEmpty(self):
        """
        None -> Bool
        This function returns true if the heap is empty and False if it is not.
        heap.isEmpty()
        >>> False
        heap.isEmpty()
        >>> True
        """
        # Return true when the priority queue is empty
        if(self.__myHeap.getLength() == 0):
            return True
        return False
    
    def printQueue(self):
        """
        None -> None
        This function prints the current Heap
        heap.printQueue()
        >>> 25, 20, 5
        heap.printQueue()
        >>> 25, 5
        heap.printQueue()
        >>> 30, 25, 20, 5
        """
        # print out Current Queue: 
        # followed by each element separated by a comma. 
        # Do not add spaces between your elements.
        #
        # (Optional; python gives us ~*~ magic methods ~*~ and there happens to 
        # be one for strings (def __str__) You can replace this method (printQueue)
        # with the magic method __str__, and use it to return the string 
        # representation of your Queue if it pleases you.)
        array = self.__myHeap.getHeap()
        array_l = []
        array_s = ""
        for node in array:
            #add every node into the array
                #then print all none items
            array_l.append(node)
        for item in array_l:
            if item is not None:
                array_s += str(item) + ","
        array_s = array_s[:-1]
        print(array_s)
        return



