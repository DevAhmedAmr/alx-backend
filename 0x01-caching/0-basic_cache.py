#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        return self.cache_data.get(key)
