PRECISION = 0.0001


def sqrt(number):
    low = 0.0
    high = middle = float(number)
    old_middle = float(-1)

    while abs(old_middle - middle) >= PRECISION:
        old_middle = middle
        middle = float(high + low) / 2.0
        if middle * middle > number:
            high = middle
        else:
            low = middle

    return middle
