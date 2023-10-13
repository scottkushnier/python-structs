def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    first_char = True
    acc = ""
    for char in phrase:
        if (char == ' '):
            acc += char
            first_char = True
        else:
            if first_char:
                acc += char.upper()
                first_char = False
            else:
                acc += char.lower()
    return acc