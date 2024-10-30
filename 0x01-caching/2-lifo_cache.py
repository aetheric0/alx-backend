#!/usr/bin/env python3
""" Implements a LIFO Caching System
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a LIFO caching system
    """
    def __init__(self):
        """ initializes BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """ Manages Caching systen, adds new cache
        or removes last added cache if cache exceeds
        max size
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = self.cache_data.popitem()
                print("DISCARD {}".format(last_item[0]))

    def get(self, key):
        """ Retrieves cache based on key supplied
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
