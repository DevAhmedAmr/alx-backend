#!/usr/bin/env python3
""" 2: Hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        function that that takes two integer arguments page
        with default value 1 and page_size with default value 10.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary containing the following key-value pairs:

            >>>> page_size: the length of the returned dataset page
            >>>> page: the current page number
            >>>> data: the dataset page (equivalent to return from previous task)
            >>>> next_page: number of the next page, None if no next page
            >>>> prev_page: number of the previous page, None if no previous page
            >>>> total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        next_page_num = None
        prev_page = None
        if page + 1 <= total_pages:
            next_page_num = page + 1

        if page - 1 > 0 and page - 1 <= total_pages:
            prev_page = page - 1

        return {"page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page_num,
                "prev_page": prev_page,
                "total_pages": total_pages}
