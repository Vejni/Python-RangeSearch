from bisect import bisect_left
import sys


# Node class definition
class Node(object):

    def __init__(self, value):
        self.value = value  # Splitting value
        self.left = None    # left child
        self.right = None   # right child
        nodes.append(self)  # automatically append to nodes array

    def getval(self):
        return self.value

    # Function to get the value of its rightmost child,
    # will be called on the left child, to get splitting value
    def getrightmost(self):
        if self.right is None:
            return self.value
        else:
            return self.right.getrightmost()

    # Function to print the LEAF nodes of a node
    def getleafs(self):
        if self.left:
            self.left.getleafs()
        if self.right:
            self.right.getleafs()
        else:
            print(self.getval(), end=" ")


# Storing numbers in order, like in Task22
def add_new_numbers(listA, number):
    i = bisect_left(listA, number)
    listA.insert(i, number)


# Function to generate the tree, it recursively calls itself or
# a version of itself with the next nevel of nodes
# Return nothing, but creates the tree structure
def create_next_level(listA):
    next_level_nodes = []    # Initialise next level nodes as empty
    # Check if the number of nodes on the level is odd,
    # if it is store the last element, and leave it out of the for loop
    if len(listA) % 2 == 1:
        last_element = listA[len(listA)-1]
        for i in range(0, len(listA)-2, 2):       # For every pair of nodes
            next_node = listA[i].getrightmost()  # Get the splitting value
            next_node = Node(next_node)           # Make it a node
            next_node.left = listA[i]            # Connect them
            next_node.right = listA[i+1]         # Connect them
            next_level_nodes.append(next_node)

        next_level_nodes.append(last_element)      # Store the lonely one too

        # If there are more than one nodes in the next level,
        # we call "recursively"
        if len(next_level_nodes) > 1:
            # But to keep the tree balanced, that is not to jagged,
            # we call the reverse version of create_next_levels
            create_next_level_reverse(next_level_nodes)

    else:
        # If number of nodes is even, we do the same,
        # but we need not to leave the last element alone
        for i in range(0, len(listA)-1, 2):
            next_node = listA[i].getrightmost()
            next_node = Node(next_node)
            next_node.left = listA[i]
            next_node.right = listA[i+1]
            next_level_nodes.append(next_node)

        if len(next_level_nodes) > 1:
            # Since we have an even number of nodes next,
            # we can call the same function.
            create_next_level(next_level_nodes)


# Modified version of create_next_level, it is called,
# if we have an odd number of nodes in the next level,
# to keep the tree balanced it will iterate through the nodes backwards
# Returns nothing, but creates the tree structure
def create_next_level_reverse(listA):
    next_level_nodes = []
    if len(listA) % 2 == 1:
        last_element = listA[0]
        for i in range(len(listA)-1, 0, -2):   # Only difference in for loop
            next_node = listA[i-1].getrightmost()
            next_node = Node(next_node)
            next_node.right = listA[i]
            next_node.left = listA[i-1]
            next_level_nodes.append(next_node)

        next_level_nodes.append(last_element)
        next_level_nodes.reverse()

        if len(next_level_nodes) > 1:
            # And the function call here, if the next level is odd as well,
            # it calls its reverse, which is the original function
            create_next_level(next_level_nodes)

    else:
        for i in range(0, len(listA)-1, 2):
            next_node = listA[i].getrightmost()
            next_node = Node(next_node)
            next_node.left = listA[i]
            next_node.right = listA[i+1]
            next_level_nodes.append(next_node)

        if len(next_level_nodes) > 1:
            create_next_level_reverse(next_level_nodes)


# Find splitting node, it returns the root of the query
def find_split_node(root, start_point, end_point):
    X = root.getval()
    while (root.right is not None) and (end_point <= X or start_point > X):
        if end_point <= X:
            root = root.left
        else:
            root = root.right
        X = root.getval()
    return root


# Query, implemented as given,
# it prints the numbers between the end_points, returns nothing
def one_D_range_query(root, start_point, end_point):
    v_split = find_split_node(root, start_point, end_point)
    # If v_split is a leaf, check if it should be returned
    if v_split.right is None:
        if v_split.getval() >= start_point and v_split.getval() <= end_point:
            print(v_split.getval(), end=" ")
            return
    else:
        # If not, look at left subtree
        v = v_split.left
        while v.left is not None:
            if start_point <= v.getval():
                v.right.getleafs()
                v = v.left
            else:
                v = v.right
        if (v is not None
                and (v.getval() >= start_point)
                and (v.getval() <= end_point)):
            print(v.getval(), end=" ")

        # Then at right subtree
        v = v_split.right
        while v.left is not None:
            if end_point >= v.getval():
                if v.left:
                    v.left.getleafs()
                v = v.right
            else:
                v = v.left
        if (v is not None
                and (v.getval() >= start_point)
                and (v.getval() <= end_point)):
            print(v.getval(), end=" ")

        return


if __name__ == "__main__":
    # Initialisation
    list_of_integers = []  # Array for the input numbers
    nodes = []  # Array to store created nodes

    # Read the first line
    first_line = sys.stdin.readline()
    info = [int(i) for i in first_line.strip().split()]
    no_elements, no_queries = info

    # Read numbers
    for _ in range(no_elements):
        line = sys.stdin.readline()
        input_integer = int(line.strip())
        add_new_numbers(list_of_integers, input_integer)

    # Creating the tree
    # Creating a leaf for each input number
    for element in list_of_integers:
        element = Node(element)

    # Then call create_next_level with the leafs,
    # it generates the tree recursively
    create_next_level(nodes)
    # Finaly, the last created node,
    # will be the root of the whole tree, so we store that
    root = nodes[len(nodes)-1]

    # Read queries
    for _ in range(no_queries):
        line = sys.stdin.readline()
        input_queries = [int(i) for i in line.strip().split()]
        one_D_range_query(root, input_queries[0], input_queries[1])
