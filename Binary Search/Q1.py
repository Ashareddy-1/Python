#  When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
#  numbers = [1,4,6,9,10,5,7]
#  Answer: It is because the list is not sorted! Binary search requires that list has to be sorted

################### PROBLEM 2 #######################
# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective
