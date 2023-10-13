import math

def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    acc = [1]
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt+1):
        if num % i == 0:
            acc.append(i)
    acc_2 = [int(num/x) for x in acc if x < sqrt]
    acc.extend(acc_2[::-1])
    return(acc)

#print(find_factors(321421))