def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    dict = {}
    for char in phrase.lower():
        if char in set('aeiou'):
            if dict.get(char):
                dict[char] += 1
            else:
                dict[char] = 1
    return dict
