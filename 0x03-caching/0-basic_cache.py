#!/usr/bin/python3
"""basic_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Create a class BasicCache that inherits
    from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """Assign to dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
