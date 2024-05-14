import sys

def swap_unique_keys_values(d):
    values = set()
    newd = {}
    for (k, v) in d.items():
        try:
            if not (v in values):
                values.add(v)
                newd[v] = k
            else:
                newd.pop(v)
        except KeyError:
            pass
    return newd
