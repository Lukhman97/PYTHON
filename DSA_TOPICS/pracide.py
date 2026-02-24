# nums1 = [1,2,2,1]
# nums2 = [2,2]
# # nums1 = [4,9,5]
# # nums2 = [9,4,9,8,4]
# n=[]
# # nums=set(nums1)
# # num=set(nums2)
# for i in set(nums1):
#     if i in nums2:
#         n.append(i)
# print(n)

# s = "abcd"
# t = "abcde"
# a=""
# for i in t:
#     if i not in s:
#         a+=i
# print(a)

        
# s1="listen"
# count1 = [0] * 26  # for a-z
# for i in range(len(s1)):
#     count1[ord(s1[i]) - ord('a')] += 1
# print(count1)


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = []     # will store lists of anagram groups
keys = []       # will store sorted-letter-keys

for w in words:
    # Manually sort letters in word
    letters = list(w)
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            if letters[j] < letters[i]:
                letters[i], letters[j] = letters[j], letters[i]

    key = "".join(letters)  # our "sorted" version of word

    # Check if key exists in keys list
    found = False
    for i in range(len(keys)):
        if keys[i] == key:
            groups[i] += [w]  # add word to existing group
            found = True
            break

    # If key not found, create a new group
    if not found:
        keys += [key]
        groups += [[w]]

print(groups)
