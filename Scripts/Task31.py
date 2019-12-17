import sys


# Store new point function, parameters, two lists
def add_new_point(lst, number):
    lst.append(number)


# Query function, parameters, three lists
def query(lst, starting_point, end_point, print_res=False):
    results = [
        str(i).replace(',', '')
        for i in lst
        if within_range(i, starting_point, end_point, 0)]
    # Note that our results array contains string as elements,
    # To match the desired output

    # Print results
    if print_res:
        for i in results:
            print(i, end=" ")
        print


# Function to recursively check if the given point is in the rectangle
# Takes in 3 lists, that is points,
# and a number which indicates the current axis to check
# Returns True or False
def within_range(point_a, point_b, point_c, i):
    if (int(point_a[i]) >= int(point_b[i])
            and int(point_a[i]) <= int(point_c[i])):
        i = i + 1
        if i == (len(point_a)):  # Base case
            return True
        # If the point is within the range,
        # call the function again on the next axis
        else:
            return (True and within_range(point_a, point_b, point_c, i))
    else:
        return False


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

    # Read queries
    for i in range(no_queries):
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
        query(list_of_points, start, end, True)
