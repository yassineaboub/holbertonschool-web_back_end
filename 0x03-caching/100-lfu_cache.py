#!/usr/bin/env python3
""" LFU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching"""

    def __init__(self):
        """initialization"""
        super().__init__()
        self.lfu = []
        self.f = {}

    def put(self, key, item):
        """assign to the dict """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.f[key] += 1
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    minvalue = min(self.f.values())
                    minkeys = [k for k in self.f
                               if self.frequency[k] == min_value]
                    for i in range(len(self.lfu)):
                        if self.lfu[i] in minkeys:
                            break
                    del self.cache_data[self.lfu[i]]
                    del self.f[self.lfu[i]]
                    print("DISCARD:", self.lfu[i])
                    self.lfu.pop(i)
                self.cache_data[key] = item
                self.f[key] = 1
            self.lfu.append(key)

    def get(self, key):
        """ return the value linked"""
        if key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            self.f[key] += 1
            return self.cache_data[key]
        return None
