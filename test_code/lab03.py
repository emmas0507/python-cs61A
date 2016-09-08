# lab03.py

def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    total, k = 0, n
    while k >= 0:
        total = total + k
        k = k - 2
    return total

def count_up(n):
    """Print out all numbers up to and including n in ascending order.
    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    if n == 1:
        print("1")
        return
    else:
        count_up(n-1)
    print(n)

def skip_mul(n):
        """Return the product of n * (n - 2) * (n - 4) * ...

        >>> skip_mul(5) # 5 * 3 * 1
        15
        >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
        0
        """
        if n <= 1:
            return n
        else:
            return n * skip_mul(n - 2)

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 1:
        return 1
    elif a % b == 0:
            return b
    else:
        return gcd(b, a % b)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"


if __name__ == '__main__':
    print("{}".format(repr(skip_add(5))))

    count_up(5)
    print("{}".format(repr(skip_mul(5))))
    print("{}".format(repr(skip_mul(8))))
    print("gcd is {}".format(repr(gcd(40, 40))))

    print("some tests")
    x = 5
    x = lambda x: lambda x: lambda y: 3+x
    print("{}".format(repr(x(3)(5)(7))))

    you = 'fly'
    yo, da = lambda do: you, lambda can: True
    yo = yo('jedi')
    da = (3 and 4 and 5 and (False or ' you shall'))
    print(yo)
    print(da)