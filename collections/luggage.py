"""Packing keyword arguments into a dict"""


def packer(**kwargs):
    print(kwargs)


packer(name="Kenneth", num=42, spanish_inquisition=None)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


unpacker(**{'first_name': "Kenneth", 'last_name': "Love"})


# def word_count(string):
#     string = string.lower()
#     string = string.split()
#     count = {}
#     for word in string:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     print(count)
#     return count
#
#
# word_count("Apple apple apple FLOPP aPPlE pear apple cat cat fish elephant human cat dog monkey")
