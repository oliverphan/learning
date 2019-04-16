def reverse_nested_dict(d1):
    # Take a Dict[str: Dict[str: str]] and return a new Dictionary with Key of nested
    # dictionary paired with key of outer Dictionary as value.
    newdict = {}
    # Initialize dictionary with inner keys mapped to empty list
    for v1 in d1.values():
        for k1 in v1.keys():
            newdict[k1] = []

    # Map outer keys as values in a list
    for k2 in d1.keys():
        for inner_key in d1[k2]:
            newdict[inner_key].append(k2)

    return newdict
