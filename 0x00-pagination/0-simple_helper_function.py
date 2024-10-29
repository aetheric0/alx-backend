#!/usr/bin/env python3
""" Function to return index_range for pagination
"""


def index_range(page, page_size):
    """ Returns a tuple that shows the range of indexes
    for the pagination parameters supplied
    """
    start_index = 1
    start_index = (page - start_index) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
