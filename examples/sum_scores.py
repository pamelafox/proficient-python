def sum_scores(scores):
    """ Calculates total score based on list of scores.
    >>> sum_scores([])
    0
    >>> sum_scores([8, 9, 7])
    24
    """
    total = 0
    for score in scores:
        total += score
    return total