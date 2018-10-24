__author__ = 'AIZOH'
'''this program returns number of times
a character appears in a string it doesnt use any function'''
name = input("Enter string \n")
s = input("Enter the character to search\n")
arr1 = list(name)
print('{0} appears {1} times in {2}'.format(s, arr1.count(s), name))
