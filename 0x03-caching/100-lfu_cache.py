#!/usr/bin/env python3
"""lfu_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache that inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dict
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(
                    self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Return the value linked
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(
                self.keys.index(key)))
            return self.cache_data.get(key)
        return None
