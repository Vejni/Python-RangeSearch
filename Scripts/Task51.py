import sys
from operator import itemgetter


# Node class definition
class Node(object):
    def __init__(self, value):
        self.value = value  # Splitting value
        self.left = None    # left child
        self.right = None   # right child

    # Function to return a list of all the offsprings of a node
    def get_offsprings(self):
        result = []
        stack = [self]
        node = None
        while stack:
            if node is None:
                node = stack.pop()
            if node is not None:
                result.append(node.value)
                stack.append(node.right)
                node = node.left
        return result

    # Get the leftmost offspring
    def get_leftmost(self):
        if not(self.left):
            return self.value
        else:
            return self.left.get_leftmost()

    # Get rightmost offspring
    def get_rightmost(self):
        if not(self.right):
            return self.value
        else:
            return self.right.get_rightmost()


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


# Function to recursively check if the given point
# is in the rectangle, same as in Task31
# Takes in 3 lists, that is points,
# and a number which indicates the current axis to check
# Returns True or False
def within_range(point_A, point_B, point_C, i):
    if (int(point_A[i]) >= int(point_B[i])
            and int(point_A[i]) <= int(point_C[i])):
        i = i + 1
        if i == (len(point_A)):  # Base case
            return True
        # If the point is within the range,
        # call the function again on the next axis
        else:
            return (True and within_range(point_A, point_B, point_C, i))
    else:
        return False


# Function to create MinMax lists
# Input: list of Points
# Output: List of tuples, first element is the min, second is max
def create_minmax(points):
    dims = len(points[0])  # Get the dimension of the space
    min_max = []         # Initialise list
    for i in range(dims):
        maximum = points[0][i]
        minimum = maximum
        for j in range(1, len(points)):
            if points[j][i] >= maximum:
                maximum = points[j][i]
            if points[j][i] <= minimum:
                minimum = points[j][i]
        min_max.append([minimum, maximum])
    return min_max


# Check if two regions intersect
# Generate minMax lists before, pass it as parameters
def intersect(minmax1, minmax2):
    for d in range(len(minmax1)):
        if not (
                minmax2[d][0] <= minmax1[d][0] <= minmax2[d][1]
                or minmax2[d][0] <= minmax1[d][1] <= minmax2[d][1]
                or minmax1[d][0] <= minmax2[d][0] <= minmax1[d][1]
                or minmax1[d][0] <= minmax2[d][1] <= minmax1[d][1]):
            return False
    return True


def search_KD_tree(v, start_point, end_point, results):
    # Check if the node has to be returned
    if within_range(v.value, start_point, end_point, 0):
        results.append(v.value)

    if v.left:
        list1 = v.left.get_offsprings()
        minmax1 = create_minmax(list1)
        list2 = [start_point, end_point]
        minmax2 = create_minmax(list2)
        # Fully contained within goes here
        # Intersect
        if(intersect(minmax1, minmax2)):
            results = (
                results
                + search_KD_tree(v.left, start_point, end_point, [])
            )
    # Other side of the tree
    if v.right:
        list1 = v.right.get_offsprings()
        minmax1 = create_minmax(list1)
        list2 = [start_point, end_point]
        minmax2 = create_minmax(list2)
        # Fully contained within goes here
        # Intersect
        if (intersect(minmax1, minmax2)):
            results = (
                results
                + search_KD_tree(v.right, start_point, end_point, [])
            )
    return results


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

    # Read queries
    for _ in range(no_queries):
        # String manipulations
        line = sys.stdin.readline()
        line = line.strip()
        line = line.replace('[', '')
        line = line.replace(']', '')
        input_point = line.split(' ')

        start = []
        for i in range(no_dimensions):
            start.append(int(input_point[i]))

        end = []
        for i in range(no_dimensions, 2*no_dimensions):
            end.append(int(input_point[i]))

        # Function call
        points = search_KD_tree(root, start, end, [])

        for p in points:
            print(str(p).replace(',', ''), end=" ")
        print("")
