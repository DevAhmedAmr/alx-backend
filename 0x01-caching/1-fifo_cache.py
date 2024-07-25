#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def put(self, key, item):
        """
        The `put` function adds a key-value pair to a cache,
        discarding the oldest item if the cache is full.

        :param key: The `key` parameter in the `put` method represents
        the key under which the `item` willbe stored in the cache.
        It is used to uniquely identify the item in the cache so that
        it can be retrieved later using the same key

        :param item: The `item` parameter in the `put` method represents
        the value that you want to store in
        the cache with the corresponding `key`. When you call the `put`
        method with a `key` and an `item`,
        the method will store this key-value pair in the cache. If the
        """
        if key and item:
            self.cache_data[key] = item
            if self.MAX_ITEMS < len(self.cache_data):
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)
