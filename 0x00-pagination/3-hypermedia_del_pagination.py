#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """_summary_

        Args:
            index (int, optional): _description_. Defaults to None.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
        a dictionary with the following key-value pairs:
            - index: the current start index of the return page.
                That is the index of the first item in the current page.
                For example if requesting page 3 with page_size 20, and no
                data was removed from the dataset, the current index should be 60.
            - next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
            - page_size: the current page size
            - data: the actual page of the dataset
        """
        total_pages = math.ceil(len(self.__dataset) / page_size)
        assert index < len(self.__dataset)

        data = []
        next_index = None
        page_size_cpy = page_size
        i = 0
        while i < page_size:
            if self.__indexed_dataset.get(index + i):
                data.append(self.__indexed_dataset[index + i])
            else:
                page_size += 1

            if i == page_size - 1:
                next_index = i + index + 1
            i += 1

        return {"index": index, "data": data,
                "page_size": page_size_cpy, "next_index": next_index}
