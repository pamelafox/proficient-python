def sum_pos_scores(scores):
    """ Calculates total score based on list of scores,
    but only considers positive scores for the total.
    """
    total = 0
    for score in scores:
        if score > 0:
            total += score
    return total