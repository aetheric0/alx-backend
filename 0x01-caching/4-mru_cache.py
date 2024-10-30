from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
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
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
