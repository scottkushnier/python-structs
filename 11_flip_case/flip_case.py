def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    acc = ""
    for char in phrase:
        if char == to_swap:
            acc += to_swap.swapcase()
        elif char == to_swap.swapcase():
            acc += to_swap
        else:
            acc += char
    return acc