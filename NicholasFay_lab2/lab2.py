# Nicholas Fay

from sys import argv
from BST import BST
from Node import Node
# Loop over input file (filename passed via argv).
    # Split each line into a task and number (if one exists) 
    #   hint: use the split method for strings https://docs.python.org/2/library/string.html#string.split
    # Perform the function corresponding to the specified task
    # i.e., insert, delete, inorder, preorder, postorder
    # Close the file when you're done.

def main(argv):
	input_file = argv[1]
	with open(input_file, 'r') as file_ob:
		#creates the binary search tree
		tree = BST()
		for line in file_ob:
			#splits the line into a list
			line = line.split()
			#if it wants a traversal 
			if(line[0] == "inorder" or line[0] == "preorder" or line[0] == "postorder"):
				tree.traverse(line[0], tree.getRoot())
				print("")
			#if it wants to insert
			if(line[0] == "insert"):
				num = int(line[1])
				tree.insert(num)
			#if it wants to delete
			if(line[0] == "delete"):
				num = int(line[1])
				tree.delete(num)
	file_ob.close()
if __name__ == "__main__":
    main(argv)

