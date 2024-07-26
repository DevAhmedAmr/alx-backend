#!/usr/bin/python3

LRUCache = __import__('3-lru_cache').LRUCache
from base_caching import BaseCaching

BaseCaching.MAX_ITEMS = 5
LRUCache.MAX_ITEMS = 5
my_cache = LRUCache()
my_cache.MAX_ITEMS = 5
prev_key = None

for i in range(10):
    key = "key-{}".format(i)
    value = "value-{}".format(i)
    if prev_key is not None:
        my_cache.get(prev_key)
    prev_key = key
    my_cache.put(key, value)
    my_cache.print_cache()

my_cache.get("key-0")
my_cache.get("key-4")
my_cache.get("key-6")
my_cache.get("key-7")
my_cache.print_cache()
my_cache.put("key-20", "value-20")
my_cache.put("key-21", "value-21")
my_cache.put("key-22", "value-22")
my_cache.print_cache()
"""Current cache:
key-0: value-0
Current cache:
key-0: value-0
key-1: value-1
Current cache:
key-0: value-0
key-1: value-1
key-2: value-2
Current cache:
key-0: value-0
key-1: value-1
key-2: value-2
key-3: value-3
Current cache:
key-0: value-0
key-1: value-1
key-2: value-2
key-3: value-3
key-4: value-4
DISCARD: key-0
Current cache:
key-1: value-1
key-2: value-2
key-3: value-3
key-4: value-4
key-5: value-5
DISCARD: key-1
Current cache:
key-2: value-2
key-3: value-3
key-4: value-4
key-5: value-5
key-6: value-6
DISCARD: key-2
Current cache:
key-3: value-3
key-4: value-4
key-5: value-5
key-6: value-6
key-7: value-7
DISCARD: key-3
Current cache:
key-4: value-4
key-5: value-5
key-6: value-6
key-7: value-7
key-8: value-8
DISCARD: key-4
Current cache:
key-5: value-5
key-6: value-6
key-7: value-7
key-8: value-8
key-9: value-9
Current cache:
key-5: value-5
key-6: value-6
key-7: value-7
key-8: value-8
key-9: value-9
DISCARD: key-5
DISCARD: key-8
DISCARD: key-9
Current cache:
key-20: value-20
key-21: value-21
key-22: value-22
key-6: value-6
key-7: value-7"""

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
