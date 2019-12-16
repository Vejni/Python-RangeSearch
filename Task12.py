from bisect import bisect_left
import sys

# Function definitions


# Storing numbers in order
def add_new_numbers(listA, number):
    listA.append(number)
    listA.sort()


# Querying usind binary search
def query(listA, starting_point, end_point, print_res=False):
    i = bisect_left(listA, starting_point)
    for element in listA[i:]:
        if element <= end_point:
            if print_res:
                print(element, end=", ")
        else:
            break


if __name__ == "__main__":
    # Initialisation
    list_of_integers = []  # Array for the input numbers

    # Read the first line
    first_line = sys.stdin.readline()
    info = [int(i) for i in first_line.strip().split()]
    no_elements, no_queries = info

    # Read numbers
    for _ in range(no_elements):
        line = sys.stdin.readline()
        input_integer = int(line.strip())
        add_new_numbers(list_of_integers, input_integer)

    # Read queries
    for _ in range(no_queries):
        line = sys.stdin.readline()
        input_queries = [int(i) for i in line.strip().split()]
        query(list_of_integers, input_queries[0], input_queries[1], True)
