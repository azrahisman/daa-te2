import random
import time

# Code dari URL yang dibagikan pada soal, ditambahkan code untuk generate random tree

# A naive recursive Python3 implementation 
# for vertex cover problem for a tree

# A utility function to find min of two integers

# A binary tree node has data, pointer to
# left child and a pointer to right child 
class Node:
	def __init__(self, x):
		
		self.data = x
		self.left = None
		self.right = None

# The function returns size of 
# the minimum vertex cover
def vCover(root):
	
	# The size of minimum vertex cover 
	# is zero if tree is empty or there
	# is only one node
	if (root == None):
		return 0
		
	if (root.left == None and
	root.right == None):
		return 0

	# Calculate size of vertex cover when 
	# root is part of it
	size_incl = (1 + vCover(root.left) +
					vCover(root.right))

	# Calculate size of vertex cover 
	# when root is not part of it
	size_excl = 0
	if (root.left):
		size_excl += (1 + vCover(root.left.left) + vCover(root.left.right))
	if (root.right):
		size_excl += (1 + vCover(root.right.left) + vCover(root.right.right))

	# Return the minimum of two sizes
	return min(size_incl, size_excl)

# function to generate binary tree (general idea from Abdul Bari on Udemy)
def generate_random_tree(num_of_vertices):
    vertices_generated = 0
    if num_of_vertices <= 0:
        return None

    # create the root node
    root = Node(random.randint(1, 1000000))
    vertices_generated += 1

    # implement queue for the iterating process
    q = []
    q.append(root)

    while vertices_generated < num_of_vertices:
        curr_node = q.pop(0) # pop and use it to generate more subtrees

        left_child = Node(random.randint(1, 1000000))
        curr_node.left = left_child # set said vertex to be the left child of initial node
        q.append(left_child)

        vertices_generated += 1

        if vertices_generated < num_of_vertices:
            right_child = Node(random.randint(1, 1000000))
            curr_node.right = right_child # set said vertex to be the right child of initial node
            q.append(right_child)

            vertices_generated += 1

    return root

# Driver Code
if __name__ == '__main__':
	
	# # Let us construct the tree 
	# # given in the above diagram
	# root = Node(20)
	# root.left = Node(8)
	# root.left.left = Node(4)
	# root.left.right = Node(12)
	# root.left.right.left = Node(10)
	# root.left.right.right = Node(14)
	# root.right = Node(22)
	# root.right.right = Node(25)

	# record start time
	start_time=time.time()

	# implementation of the generating tree
	num_vertices = int(input("Enter the number of vertices: "))
	root = generate_random_tree(num_vertices)

	print("Size of the smallest vertex cover is", vCover(root))

	# record end and delta time
	end_time=time.time()
	delta_time=end_time-start_time
	print("time needed:", delta_time)

# This code is contributed by mohit kumar 29, tweaked by azra
