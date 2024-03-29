import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


# Function definitions
def add_new_numbers(listA, number):
    listA.append(number)


def query(listA, starting_point, end_point, print_res=False):
    for element in listA:
        if element >= starting_point and element <= end_point:
            if print_res:
                print(element, end=", ")


if __name__ == "__main__":
    # Initialisation
    list_of_integers = []  # Array for the input numbers

    # Read the first line
    first_line = sys.stdin.readline()
    info = [int(i) for i in first_line.strip().split()]
    no_of_elements, no_of_queries = info

    # Read numbers
    for _ in range(no_of_elements):
        line = sys.stdin.readline()
        input_integer = int(line.strip())
        add_new_numbers(list_of_integers, input_integer)

    # Read queries
    for _ in range(no_of_queries):
        line = sys.stdin.readline()
        input_queries = [int(i) for i in line.strip().split()]
        query(list_of_integers, input_queries[0], input_queries[1])
