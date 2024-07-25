#!/usr/bin/python3
"""
Test
"""
import sys

try:
    LIFOCache = __import__('2-lifo_cache').LIFOCache

    my_cache = LIFOCache()
    my_cache.print_cache()
    my_cache.put("test1", "myValue")
    my_cache.print_cache()
    test1_value = my_cache.get("test1")
    if test1_value != "myValue":
        print("get must return 'myValue', as we put it in the cache")
    else:
        print("OK")
except BaseException:
    print(sys.exc_info()[1])
