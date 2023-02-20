from itertools import groupby


# реализация замены цепочек с помощью стандартных функций
def chain_search_auto(a: list[int], b: list[int]):
    if not a and not b:
        print(a)
        print(b)
        return a, b
    if a and not b:
        b.append(a.pop(0))
        print(f"Произошел обмен в списке А: {a}")
        print(f"Произошел обмен в списке B: {b}")
        return a, b
    if not a and b:
        a.append(b.pop(0))
        print(f"Произошел обмен в списке А: {a}")
        print(f"Произошел обмен в списке B: {b}")
        return a, b

    max_chain_a = max(([list(g) for k, g in groupby(a)]), key=len)
    max_chain_b = max(([list(g) for k, g in groupby(b)]), key=len)

    str_max_a = ",".join(map(str, max_chain_a))
    str_max_b = ",".join(map(str, max_chain_b))

    str_a = ",".join(map(str, a))
    str_b = ",".join(map(str, b))

    str_a = str_a.replace(str_max_a, str_max_b, 1)
    str_b = str_b.replace(str_max_b, str_max_a, 1)

    a = list(map(int, str_a.split(",")))
    b = list(map(int, str_b.split(",")))
    print(f"Произошел обмен в списке А: {a}")
    print(f"Произошел обмен в списке B: {b}")

    return a, b
