# Sample lists
list1 = [1, 2, 3, 4, 5, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [7, 8, 9, 10, 11]

# Find duplicates in the three lists
duplicates = set(list1) & set(list2) & set(list3)

# Convert the result back to a list if needed
duplicates_list = list(duplicates)

# Print the duplicates
if duplicates_list:
    print("Duplicates in the three lists:", duplicates_list)
else:
    print("No duplicates found in the three lists.")