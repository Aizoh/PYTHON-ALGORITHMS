__author__ = 'AIZOH'
# method 1 for beginners

sent = input("Enter sentence  to find shortest \n")
def find_small(sent2):
    smallest_len = 150
    sent2list = sent.split()
    print("WORD LIST:", sent2list)
    for word in sent2list:
        curr_len = 0
        for letter in word:
            curr_len += 1
        if curr_len < smallest_len:
            smallest_len = curr_len
    return smallest_len


print("LENGTH OF SMALLEST :", find_small(sent))

# shortest for intermediate
def find_smallest(sent):
    return min(len(word) for word in sent.split())
print("LENGTH OF SMALLEST:", find_smallest(sent))