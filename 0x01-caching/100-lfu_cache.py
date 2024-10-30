#!/usr/bin/env python3
""" LFU Caching System
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ Initializes the instance of class
    """
    def __init__(self):
        super().__init__()
        self.freq = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """ Inserts item in cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = min(self.freq,
                          key=lambda k: (self.freq[k],
                                         self.order.index(k)))
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            self.order.remove(lfu_key)
            print("DISCARD: {}".format(lfu_key))
        self.cache_data[key] = item
        self.freq[key] += 1
        self.order.append(key)

    def get(self, key):
        """ Retrieve item from cache based on key supplied
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
