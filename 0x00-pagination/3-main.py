#!/usr/bin/env python3
"""
Main file
"""
import datetime
x = datetime.datetime.now()
Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
res2 = server.get_hyper_index(res.get('next_index'), page_size)
print(res2)

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
# del server._Server__indexed_dataset[res2.get('index')]

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not
# the same as the first request
res3 = server.get_hyper_index(3, page_size)
print(res3)

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res3.get('next_index'), page_size))
