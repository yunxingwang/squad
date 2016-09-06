from math import log, exp


def geomean(values):
    """
    The intuitive/naive way of calculating a geometric mean (first
    multiply the n values, then take the nth-root of the result) does not
    work in practice. When you multiple an large enough amount of large
    enough numbers, their product will oferflow the float representation,
    and the result will be Infinity.

    We use the alternative method described in
    https://en.wikipedia.org/wiki/Geometric_mean -- topic "Relationship with
    arithmetic mean of logarithms" -- which is exp(sum(log(x_i)/n))

    Zeros are excluded from the calculation. Since for us numbers are usually
    measurements (time, counts, etc), we interpret 0 as "does not exist".
    """
    values = [v for v in values if v != 0]

    n = len(values)
    log_sum = 0.0
    for v in values:
        log_sum = log_sum + log(v)
    return exp(log_sum / n)
