def suggest_supplies(temperature, windspeed, incline):
    """
    >>> suggest_supplies(33, 3, 0)
    ''
    >>> suggest_supplies(33, 3, 5)
    'stick '
    >>> suggest_supplies(33, 6, 0)
    'windbreaker '
    >>> suggest_supplies(17, 0, 0)
    'thermal '
    >>> suggest_supplies(33, 6, 10)
    'windbreaker stick '
    >>> suggest_supplies(17, 0, 10)
    'stick thermal '
    """
    supplies = ''
    if windspeed > 5:
        supplies += 'windbreaker '
    elif incline > 0:
        supplies = 'stick '
    elif temperature < 32:
        supplies += 'thermal '
    return supplies

suggest_supplies(33, 6, 10)