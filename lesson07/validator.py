def get_positive_value(value):
    if value > 0:
        return value
    else:
        raise ValueError(" value < 0")