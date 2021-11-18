def n_items(max_n):
    n, numbers = 0, []
    while n <= max_n:
        numbers.append(n)
        n += 1
    return numbers


lst = n_items(20)
print(lst)
