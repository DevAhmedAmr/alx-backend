#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple

# 9          #10


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    return ((page_size * page) - page_size, (page_size * page))


if "__main__" == __name__:
    res = index_range(page=1, page_size=10)
    print(type(res))
    print(res)
# 1
# >>> 0 10
