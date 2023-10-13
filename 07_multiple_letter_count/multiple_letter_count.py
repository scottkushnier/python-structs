def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    all_letters = set(phrase)
#    print('letters:', all_letters)
    ret = {letter:phrase.count(letter) for letter in all_letters}
    return(ret)

# print(multiple_letter_count('yay'))