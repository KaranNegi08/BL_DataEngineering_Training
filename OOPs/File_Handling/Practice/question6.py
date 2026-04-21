data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}

def print_values(d):
    for k, v in d.items():
        # print(v)
        if isinstance(v, dict):
            yield from print_values(v)
        else:
            yield v


print(list(print_values(data)))
