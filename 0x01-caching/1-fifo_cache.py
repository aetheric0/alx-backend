#!/usr/bin/env python3
""" Implements a cache based on the FIFO principle for
for cache management
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a FIFO Caching system
    """
    def __init__(self):
        """ Initializes base class
        """
        super().__init__()

    def put(self, key, item):
        """ Inserts Items in Cache and discards
        first item when cache is past MAX_ITEMS
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))

    def get(self, key):
        """ Retrieves item from cache based on key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
