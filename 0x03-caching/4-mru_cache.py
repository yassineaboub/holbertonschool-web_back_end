#!/usr/bin/python3
"""
mru_cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.min = []

    def put(self, key, item):
        """Assign to the dict"""

        if key and item:
            if key in self.cache_data:
                self.min.remove(key)

            self.cache_data[key] = item
            self.min.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min = self.min.pop(-2)
            del self.cache_data[min]
            print("DISCARD:", min)

    def get(self, key):
        """Return the value linked"""

        if key in self.cache_data:
            self.min.remove(key)
            self.min.append(key)

        return self.cache_data.get(key)
