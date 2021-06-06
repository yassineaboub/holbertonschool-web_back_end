#!/usr/bin/python3
"""lru_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Create a class LRUCache that inherits
    from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigning to the dictionary"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            to_discard = self.keys.pop(0)
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """return the value linked"""

        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
