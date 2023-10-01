def find_triplet_with_sum(arr, target_sum):
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return [arr[i], arr[j], arr[k]]

    return None  # Return None if no triplet is found

# Example usage:
my_list = [10, 20, 30, 9]
target = 59

result = find_triplet_with_sum(my_list, target)

if result is not None:
    print("Triplet with sum", target, "is:", result)
else:
    print("No triplet found with the given sum.")