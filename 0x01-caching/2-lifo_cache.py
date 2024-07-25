#!/usr/bin/env python3
"""Task 2: LIFO Caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """

    def put(self, key, item):
        """
        This Python function adds a key-value pair to a cache,
        discarding the least recently used item if the cache is full.

        :param key: The `key` parameter in the `put` method
        represents  the key under which the `item` will be stored
        in the cache.  It is used to uniquely identify the item in
        the cache

        :param item: The `item` parameter in the `put` method represents
        the value that you want to store in the cache with the
        corresponding `key`. When you call the `put`method with a `key`
        and an `item`, the method will store the `item` in the cache under
        the specified
        """

        if key and item:

            if self.cache_data:
                last_key = next(reversed(self.cache_data))

            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item

            if LIFOCache.MAX_ITEMS < len(self.cache_data):
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
