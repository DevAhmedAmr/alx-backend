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
        self.points = OrderedDict()
        self.mini = self.MAX_ITEMS

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if not (key and item):
            return None
        # {1,0,2,3}
        if len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item

            self.points = self.decrement(self.points, key)

            self.points[self.MAX_ITEMS] = key

        elif len(self.cache_data) == self.MAX_ITEMS and key in self.cache_data:
            self.points = self.decrement2(self.points, key)

        else:
            oldest_key = self.points[self.mini]
            del self.points[self.mini]
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]

            self.points = self.decrement(self.points, key)
            self.points[self.MAX_ITEMS] = key
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key not in self.cache_data:
            return None

        if len(self.cache_data) < self.MAX_ITEMS:
            value = self.cache_data.get(key)
            self.points = self.decrement(self.points, key)
            self.points[self.MAX_ITEMS] = key
            return value

        elif len(self.cache_data) == self.MAX_ITEMS and key in self.cache_data:
            self.points = self.decrement2(self.points, key)

            return self.cache_data.get(key)
        else:

            oldest_key = self.points[self.mini]

            del self.points[self.mini]
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]
            self.points = self.decrement(self.points, key)
            self.points[self.MAX_ITEMS] = key

        return self.cache_data.get(key)

    def decrement(self,  # The `points` dictionary in the LRUCache class is used to keep track of the
                  # order in which keys were accessed in the cache. It is used to implement the
                  # Least Recently Used (LRU) caching policy.
                  points: dict, key: str) -> dict:
        """Decrement the value of key in the dictionary

        Args:
            points (dict): [description]
            key (str): [description]

        Returns:
            dict: [description]
        """
        temp = {}
        key_pts = get_key_from_value(points, key)
        if key_pts == self.MAX_ITEMS:
            return points
        for point, key_name in points.items():
            if point <= self.MAX_ITEMS and point != key_pts:
                temp[point - 1] = key_name
                point -= 1
            if point < self.mini:
                self.mini = point

        return temp

    def decrement2(self, points: dict, key: str, ) -> dict:
        """Decrement the value of key in the list of points to the smallest key .

        Args:
            points (dict): [description]
            key (str): [description]

        Returns:
            dict: [description]
        """
        temp = {}
        key_point = get_key_from_value(points, key)
        for point, key_name in points.items():

            if point > key_point:
                temp[point - 1] = key_name
            else:
                temp[point] = key_name

            if point < self.mini:
                self.mini = point

        # del temp[key_point]
        temp[self.MAX_ITEMS] = key

        return temp
