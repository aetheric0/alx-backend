#!/usr/bin/env python3
from base_caching import BaseCaching
""" MRU Caching System
"""


class MRUCache(BaseCaching):
    """ Defines the MRU Caching System
    """
    def __init__(self):
        """ Initializes the base class and creates
        a tracking list for keys
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Inserts an item to the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.order.pop()
            del self.cache_data[mru]
            print("DISCARD: {}".format(mru))
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Retrieves cache based on key supplied
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
