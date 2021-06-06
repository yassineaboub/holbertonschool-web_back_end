#!/usr/bin/python3
"""fifo_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Create a class FIFOCache that inherits
    from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.idxs = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                dscrd = self.idxs.pop(0)
                del self.cache_data[dscrd]
                print("DISCARD:", dscrd)

            self.cache_data[key] = item
            self.idxs.append(key)

    def get(self, key):
        """getting items"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
