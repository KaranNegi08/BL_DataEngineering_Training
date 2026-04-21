data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}

def count_keys(d):
    count =0
    for k,v  in d.items():
        count += 1
        if isinstance(v, dict):
            count += count_keys(v)
    return count

print(count_keys(data))