def factorial(n):
    """some math function

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120

    """
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# print(factorial(5))
