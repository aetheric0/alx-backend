#!/usr/bin/env python3
""" Module implements caching from the base module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and implements a get and put method
    """

    def put(self, key, item):
        """ Inserts a key and item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
