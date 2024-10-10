# Given functions for count management

_counted = 0


def mark_as_counted(position):
    '''
    Mark a position as _counted.

    Parameters
    ----------
    position : a non-negative integer to be marked as _counted

    See Also
    --------
    check_if__counted : return True when for position marked as _counted
    reset_all_to_not_counted : undo the effect of mark_as_counted on all positions
    '''
    global _counted
    _counted |= (1 << position)


def check_if_counted(position):
    '''
    Return whether a position has been _counted.

    Parameters
    ----------
    position : a non-negative integer to be marked as _counted

    See Also
    --------
    mark_as_counted : mark position as _counted
    reset_all_to_not_counted : undo the effect of mark_as_counted on all positions
    '''
    global _counted
    return bool(_counted & (1 << position))


def reset_all_to_not_counted():
    '''
    Mark all positions as not _counted.

    See Also
    --------
    check_if_counted : return False on any position after reset_all_to_not_counted
    mark_as_counted : mark a position as _counted so that check_if_counted returns True
    '''
    global _counted
    _counted = 0
