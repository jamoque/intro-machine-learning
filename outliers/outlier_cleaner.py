#!/usr/bin/python
from operator import itemgetter
from itertools import izip

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error_squared).
    """
    
    cleaned_data = []

    for p, a, n in izip(predictions, ages, net_worths):
        error_squared = (p - n) ** 2
        cleaned_data.append((a, n, error_squared))

    # sort by the largest squared error
    cleaned_data.sort(key=itemgetter(2))

    # slice ~10% of the data with the largest error
    remove = int(round(0.1 * len(cleaned_data)))
    cleaned_data = cleaned_data[:-remove]

    return cleaned_data

