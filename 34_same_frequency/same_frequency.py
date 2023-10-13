def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return tally_freqs(num1) == tally_freqs(num2)

def tally_freqs(num1):
    s = str(num1)
    dict = {}
    for digit in s:
        if dict.get(digit):
            dict[digit] += 1
        else:
            dict[digit] = 1
    return(dict)
