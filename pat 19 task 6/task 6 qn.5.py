def min_difference_between_bags(mangoes, students):
    if len(mangoes) < students:
        return 0  # Not enough bags for each student

    mangoes.sort()
    min_diff = sum(mangoes)

    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

mangoes = [8, 12, 6, 7, 14, 15]
students = 3
result = min_difference_between_bags(mangoes, students)
print("Minimum difference between bags:", result)