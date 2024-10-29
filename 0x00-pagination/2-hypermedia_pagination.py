#!/usr/bin/env python3
""" Returns a list of the items in the range of page indexes
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
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
        if end_index > len(self.__dataset) or start_index >= len(self.__dataset):
            return index_data
        return self.__dataset[start_index:min(end_index, len(self.__dataset))]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        index_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = (total_data + page_size - 1) // page_size

        data_dict = {
            'page_size': len(index_data),
            'page': page,
            'data': index_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return data_dict
