from operator import sub, mul
from math import log, pow

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    result = [0] * (n+1)
    for i in range(n+1):
        if i <= 3:
            result[i] = i
        else:
            result[i] = result[i-1] + 2 * result[i-2] + 3 * result[i-3]
    return result[n]


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    # not the right code, computation is too long
    if n == 1 or n == 2:
        return n
    else:
        if has_seven(n-1) or (n-1) % 7 == 0:
            if pingpong(n-2) < pingpong(n-1):
                return pingpong(n-1) - 1
            else:
                return pingpong(n-1) + 1
        else:
            if pingpong(n-2) < pingpong(n-1):
                return pingpong(n-1) + 1
            else:
                return pingpong(n-1) - 1

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def cal_m(amount):
        if amount == 0:
            return 0
        else:
            logm = int(log(amount, 2))
            return int(pow(2, logm))

    def count_changes(amount, largest_value):
        if amount < 0:
            print("amount should not be negative")
        elif amount < largest_value:
            return count_changes(amount, cal_m(amount))
        elif count_changes_list[corr_index(largest_value)][amount] > -1:
            return count_changes_list[corr_index(largest_value)][amount]
        else:
            count_changes_list[corr_index(largest_value)][amount] = count_changes(amount - largest_value, largest_value) + count_changes(amount, largest_value // 2)
            if largest_value == amount:
                for i in range(amount, len(count_changes_list)):
                    count_changes_list[i][amount] = count_changes_list[corr_index(largest_value)][amount]
            return count_changes_list[corr_index(largest_value)][amount]

    def corr_index(n):
        if n <= 2:
            return n
        else:
            return int(log(n, 2)) + 1

    count_changes_list = [[-1 for x in range(amount+1)] for y in range(int(log(amount, 2)) + 2)]
    for i in range(amount+1):
        count_changes_list[0][i] = 0
    for i in range(len(count_changes_list)):
        count_changes_list[i][0] = 1
    test = count_changes(amount, cal_m(amount))
    return test

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
    else:
        mid = [x for x in range(1, 4) if x not in [start, end]][0]
        # import pdb; pdb.set_trace()
        move_stack(n-1, start, mid)
        move_stack(1, start, end)
        move_stack(n-1, mid, end)


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'


if __name__ == "__main__":
    # for i in range(30)[1:]:
    #    print(pingpong(i))

    print(count_change(100))
    move_stack(3, 1, 3)


