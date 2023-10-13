def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    l = len(lst)
    if l:
        return lst[l-1]
    else:
        return None
    
print(last_element([1, 2, 3]))
print(last_element([]))