def has_sublist_with_zero_sum(arr):
    prefix_sum = set()
    current_sum = 0

    for num in arr:
        current_sum += num

        if current_sum == 0 or current_sum in prefix_sum:
            return True

        prefix_sum.add(current_sum)

    return False

my_list = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(my_list)

if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("No sub-list with a sum equal to zero found.")