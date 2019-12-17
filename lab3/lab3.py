from sys import argv
from pQueue import pQueue

def main(argv):
    # Loop over input file. 
    # Split each line into the task and the corresponding number (if one exists)
    # Depending on what the input task was, preform the corresponding function
    # Finally, close your file.

    inputFile = argv[1]
    num_lines = 0
    with open(inputFile, 'r') as file_ob:
    	for line in file_ob:
    		num_lines += 1

    with open(inputFile, 'r') as file_ob:
		#creates the heap
		#heap_size = len(file_ob.readlines())
		heap = pQueue(num_lines)
		for line in file_ob:
			#splits the line into a list
			line = line.split()
			#print(line)
			#if it wants to know if the heap is empty
			if(line[0] == "isEmpty"):
				empty = heap.isEmpty()
				if(empty == True):
					print("Empty"),
				else:
					print("Not Empty"),
				print("")
			#if it wants to find the maximum
			if(line[0] == "maximum"):
				max_v = heap.maximum()
				print(max_v),				
				print("")
			#if it wants to insert
			if(line[0] == "insert"):
				num = int(line[1])
				heap.insert(num)
			#if it wants to delete
			if(line[0] == "extractMax"):
				max_v = heap.extractMax()
				print(max_v),
				print("")
			#if it wants to print
			if(line[0] == "print"):
				print("Current Queue:"),
				heap.printQueue()
		file_ob.close()

if __name__ == "__main__":
    main(argv)