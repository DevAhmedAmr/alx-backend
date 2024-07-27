#!/usr/bin/env python3
'''Task 3: LRU Caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


def get_key_from_value(d: dict, target_value: any):
    """Get the first key from a dict that matches the given value .

    Args:
        d (dict): [description]
        target_value (any): [description]

    Returns:
        [type]: [description]
    """
    for key, value in d.items():
        if value == target_value:
            return key

    return None


class LRUCache(BaseCaching):
    """A class `LRUCache` that inherits from
       `BaseCaching` and is a caching system
    """

    def __init__(self):
        '''initialize the cache
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_order = OrderedDict()
        self.mini = self.MAX_ITEMS

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key (str): The key to add.
            item (any): The item to add.
        """
        if not (key and item):
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            # print("zz ", self.mini)
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = next(iter(self.access_order.values()))
                del self.cache_data[oldest_key]
                del self.access_order[self.mini]
                print("DISCARD:", oldest_key)
            self.cache_data[key] = item
            self.reorder_keys(key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key (str): The key to retrieve.

        Returns:
            any: The item associated with the key, or None if not found.
        """
        if key not in self.cache_data:
            return None

        self.reorder_keys(key)
        return self.cache_data[key]

    def reorder_keys(self, key: str) -> None:
        """Reorder keys to ensure LRU order.

        Args:
            key (str): The key to move to the end of the access order.
        """
        temp = {}
        key_point = get_key_from_value(self.access_order, key)
        # print("before ", self.access_order)
        if key_point is not None:
            for position, key_name in self.access_order.items():
                if position > key_point:
                    temp[position - 1] = key_name
                else:
                    temp[position] = key_name
                self.mini = min(self.mini, position)

            temp[self.MAX_ITEMS] = key
            self.access_order = temp
        else:
            self.access_order[self.MAX_ITEMS] = key
        # #print("after ", self.access_order, self.mini)
