__author__ = 'AIZOH'

'''accepts a list and an item,
and returns true if the item belongs to the list,
otherwise false.'''
def include(arr, item):
    pass
    if item in arr:
        return True
    else:
        return False

# method 2

def include(arr, item):
    return item in arr

print(include([1,2,3,4], 3))