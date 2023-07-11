tolerance = 10 ** -10


def bisection(f, a, b, counter=0):
    # Check if the interval is within the tolerance
    if abs(a - b) < tolerance:
        return (a + b) / 2

    # Calculate the midpoint of the interval
    midpoint = (b - a) / 2

    # Determine which half of the interval to continue with
    if f(a + midpoint) * f(b) < 0:
        return bisection(f, a + midpoint, b, counter + 1)
    else:
        return bisection(f, a, b - midpoint, counter + 1)
