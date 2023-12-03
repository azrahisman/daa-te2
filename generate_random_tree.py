# ===== CODE FOR GENERATING TREE =====

import random

# taken from given code for Vertex Cover Problem using Dynamic Programming
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

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
