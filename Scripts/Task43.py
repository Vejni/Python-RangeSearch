import sys
from operator import itemgetter


# Node class definition
class Node(object):
    def __init__(self, value):
        self.value = value  # Splitting value
        self.left = None    # left child
        self.right = None   # Right child

    # Function to print the tree, does depth first traversal
    @staticmethod
    def print_tree(self):
        print(self.value)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


# Store new point function, parameters, two lists
def add_new_point(lst, number):
    lst.append(number)


# Returns the median POINT of a list,
# if even elements,
# returns the bigger one as I took the picture as an example
# Sort list before use
def median(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return None
    index = (lst_len - 1) // 2
    if (lst_len % 2):
        return (lst[index])
    else:
        return (lst[index + 1])


# Function to build the tree, returns the root at the end,
# takes in a list of points and 0 in the beginning
def build_kd_tree(P, depth):
    if len(P) == 0:
        return None
    elif len(P) == 1:
        return Node(P[0])

    axis = depth % no_dimensions
    P.sort(key=itemgetter(axis))            # Sort the list on the desired axis
    med_value = median(P)                   # Get the median on that axis
    rounded_middle = int(len(P)/2)          # Rounded down middle

    v_left = build_kd_tree(P[:(rounded_middle)], (depth+1))
    v_right = build_kd_tree(P[(rounded_middle+1):], (depth+1))

    median_point = Node(med_value)
    median_point.left = v_left
    median_point.right = v_right
    return median_point


if __name__ == "__main__":
    # Initialisation
    list_of_points = []  # Array for the input numbers

    # Read the first line
    first_line = sys.stdin.readline()
    info = [int(i) for i in first_line.strip().split()]
    no_elements, no_dimensions, no_queries = info

    # Read numbers
    for i in range(no_elements):
        line = sys.stdin.readline()
        input_point = [int(i) for i in line.strip().split()]
        add_new_point(list_of_points, input_point)

    # Create tree
    root = build_kd_tree(list_of_points, 0)

    # Print tree, depth first order
    Node.print_tree()
