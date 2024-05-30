def get_val(collection, key, default='git'):
    if collection == {}:
        return default
    elif key is None:
        return default
    return collection[key]