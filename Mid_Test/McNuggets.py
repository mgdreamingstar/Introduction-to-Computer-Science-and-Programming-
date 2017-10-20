def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for ia in range(n//6+1):
        if 6*ia == n:
            return True
        for ib in range(n//9+1):
            if 6*ia + 9*ib == n:
                return True
            for ic in range(n//20+1):
                if 6*ia + 9*ib + 20*ic == n:
                    return True
    else:
        return False

McNuggets(15)
McNuggets(22)
