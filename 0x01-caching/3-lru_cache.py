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
        """
        if not (key and item):
            return None

        self.cache_data[key] = item
        self.rearrange_order_with_max_check(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            oldest_key = self.access_order[self.mini]
            del self.access_order[self.mini]
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        pass
        if key not in self.cache_data:
            return None

        if len(self.cache_data) < self.MAX_ITEMS:
            value = self.cache_data.get(key)
            self.rearrange_order_with_max_check(key)
            return value

        elif len(self.cache_data) == self.MAX_ITEMS and key in self.cache_data:
            self.rearrange_order(key)
            return self.cache_data.get(key)
        else:
            oldest_key = self.access_order[self.mini]

            del self.access_order[self.mini]
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]
            self.rearrange_order_with_max_check(key)

        return self.cache_data.get(key)

    def rearrange_order_with_max_check(self, key: str) -> None:
        """Decrement the value of key in the dictionary

        Args:
            points (dict): [description]
            key (str): [description]

        Returns:
            dict: [description]
        """
        updated_access_order = {}
        current_position = get_key_from_value(self.access_order, key)
        if current_position == self.MAX_ITEMS:
            return

        for position, key_name in self.access_order.items():
            if position <= self.MAX_ITEMS and position != current_position:
                updated_access_order[position - 1] = key_name
                position -= 1
                self.mini = min(self.mini, position)

        self.access_order = updated_access_order
        self.access_order[self.MAX_ITEMS] = key

    def rearrange_order(self, key: str, ) -> dict:
        """Decrement the value of key in the list of points to the smallest key .

        Args:
            points (dict): [description]
            key (str): [description]

        Returns:
            dict: [description]
        """
        updated_access_order = {}

        key_point = get_key_from_value(self.access_order, key)
        for point, key_name in self.access_order.items():
            if point > key_point:
                updated_access_order[point - 1] = key_name
            else:
                updated_access_order[point] = key_name

            if point < self.mini:
                self.mini = point

        updated_access_order[self.MAX_ITEMS] = key
        self.access_order = updated_access_order
