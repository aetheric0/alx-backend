#!/usr/bin/env python3
""" The LRU Caching System
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines the LRU caching system
    """
    def __init__(self):
        """ Initializes base class and declares
        list for tracking keys
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Inserts an item in cache based on LRU
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.order.pop(0)
            del self.cache_data[lru]
            print("Discard: {}".format(lru))
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Retrieves a cache based on key supplied
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
