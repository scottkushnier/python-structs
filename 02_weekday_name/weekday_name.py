
day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week >= 1 and day_of_week <= 7:
        return day_names[day_of_week-1]
    else:
        return None

print(weekday_name(1))
print(weekday_name(3))
print(weekday_name(7))
print(weekday_name(9))
print(weekday_name(0))
