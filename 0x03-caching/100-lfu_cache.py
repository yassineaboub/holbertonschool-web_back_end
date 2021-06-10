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
        self.keyys = []

    def put(self, key, item):
        """
        Assign to the dict
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.keyys:
                self.keyys.append(key)
            else:
                self.keyys.append(self.keyys.pop(
                    self.keyys.index(key)))
            if len(self.keyys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.keyys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Return the value linked
        """
        if key is not None and key in self.cache_data:
            self.keyys.append(self.keyys.pop(
                self.keyys.index(key)))
            return self.cache_data.get(key)
        return None
