def first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    element_count = {}

    # Iterate through the list and count the occurrences
    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

# Example usage:
my_list = [2, 3, 5, 3, 7, 2, 5]
result = first_non_repeating_element(my_list)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found in the list.")