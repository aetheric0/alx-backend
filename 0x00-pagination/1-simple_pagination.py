#!/usr/bin/env python3
""" Returns a list of the items in the range of page indexes
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Returns a tuple that shows the range of indexes
    for the pagination parameters supplied
    """
    start_index = 1
    start_index = (page - start_index) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        self.__dataset = self.dataset()
        index_data = []
        indexes = index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        if end_index > len(self.__dataset) - 1:
            return index_data
        while (start_index < end_index):
            index_data.append(self.__dataset[start_index])
            start_index += 1
        return index_data
