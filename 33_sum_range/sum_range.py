def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    acc = 0
    if start:
        start_at = start
    else:
        start_at = 0
    if end:
        if end > len(nums):
            stop_at = len(nums)
        else:
            stop_at = end+1
    else:
        stop_at = len(nums)
#    print('start', start_at, 'stop', stop_at)
    for i in range(start_at,stop_at):
        acc += nums[i]
    return acc
