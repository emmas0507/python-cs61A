# test on the function decorator
import string
from operator import add, sub

def trace(fn):
    def wrapped(x):
        print(fn)
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

# the decorator is equivalent to
def triple(x):
    return 3 * x

# examples on the decorator

def memoize(f):
    cache = {}
    print("create cache")
    def helper(x):
        print("helper(" + str(x) + ")")
        # print("cache is {x!r}".format(x=cache))
        if x not in cache:
            print(str(x) + " not in cache")
            cache[x] = f(x)
        return cache[x]
    return helper

@memoize
def fib(n):
    print("started new fib")
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# example of high order function
def outer(n):
    def inner(m):
        return n - m
    return inner

def make_derivative(f, h=1e-5):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> square = lambda x: x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    "*** YOUR CODE HERE ***"
    def derivative_atx(x):
        return (f(x+h) - f(x))/h
    return derivative_atx

def letter_to_num(letter):
    if not isinstance(letter, str):
        print("input {} is not a string".format(repr(letter)))
    elif letter not in string.ascii_lowercase and letter not in string.ascii_uppercase:
        print("input {} is not a valid letter".format(letter))
        return None
    else:
        diff = ord(letter) - ord('a')
        if diff >= 0:
            return diff
        else:
            return ord(letter) - ord('A') + len(string.ascii_lowercase)

def num_to_letter(n):
    if not isinstance(n, int):
        print("input {} is not a valid integer".format(repr(n)))
        return None
    elif n < 0 or n > 51:
        print("input {} is within 0 to 51".format(repr(n)))
        return None
    else:
        if n <= 25:
            return chr(ord('a') + n)
        else:
            return chr(ord('A') + n - len(string.ascii_lowercase))

def caesar_generator(num, op):
    """Returns a one-argument Caesar cipher function. The function should "rotate" a
    letter by an integer amount 'num' using an operation 'op' (either add or
    sub).

    You may use the provided `letter_to_num` and `num_to_letter` functions,
    which will map all lowercase letters a-z to 0-25 and all uppercase letters
    A-Z to 26-51.

    >>> letter_to_num('a')
    0
    >>> letter_to_num('c')
    2
    >>> num_to_letter(3)
    'd'

    >>> caesar2 = caesar_generator(2, add)
    >>> caesar2('a')
    'c'
    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus3('d')
    'a'
    """
    "*** YOUR CODE HERE ***"
    return lambda x: num_to_letter(op(letter_to_num(x), num))

if __name__ == "__main__":
    # print("{x!r}".format(x=fib))
    print(triple(12))
    # x = fib(5)
    # print("result is " + str(x))
    # fib = memoize(fib)
    outer(61)
    f = outer(10)
    print(f(4))
    print(outer(5)(4))

    #############################
    # print result of make derivative function
    square = lambda x: x*x
    derivative = make_derivative(square)
    result = derivative(3)
    print(result)

    print(letter_to_num('B'))
    print(num_to_letter(51))

    caesar2 = caesar_generator(2, add)
    brutus3 = caesar_generator(3, sub)
    print("{}".format(caesar2('a')))
    print("{}".format(brutus3('d')))