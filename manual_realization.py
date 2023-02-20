# ручная реализация поиска цепочек
def _seq(arr):
    element_index = 1
    counter = max_counter = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            counter += 1
        else:
            if counter > max_counter:
                max_counter = counter
                element_index = i
            counter = 1
        if counter > max_counter:
            max_counter = counter
            element_index = i + 1
    return element_index - max_counter, element_index


# замена цепочек
def chain_replace(a, b):
    a_start, a_end = _seq(a)
    b_start, b_end = _seq(b)
    ta = a[a_start:a_end].copy()
    tb = b[b_start:b_end].copy()
    a = a[:a_start] + tb + a[a_end:]
    b = b[:b_start] + ta + b[b_end:]
    print(f"Произошел обмен в списке А: {a}")
    print(f"Произошел обмен в списке B: {b}")

    return a, b