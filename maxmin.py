
def find_max_min(integer_list):  # Function to find minimum and maximum integers in given list
    # Sort the list of integers into ascending order
    ordered_integers = sorted(integer_list)
    # Gets the first element of the list = minimum integer
    min_integer = ordered_integers[0]
    # Gets the last element of the list = maximum integer
    max_integer = ordered_integers[-1]
    return min_integer, max_integer


integer_list = list(map(int, input("Enter a list of integers separated by spaces (e.g. [1, 2, 3, 4]: ")  # map applies int to every element in the list and convert to list.
                        .replace(',', '')  # Remove commas if present
                        .replace('[', '')  # Remove opening bracket
                        .replace(']', '')  # Remove closing bracket
                        .split()))  # Split into individual numbers


print(f"For {integer_list}, the minimum and maximum integers are: {find_max_min(integer_list)}")
