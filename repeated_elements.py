#program which gives a dictionary with as a keys the elements form a list and values the number of times of each element is in the list.

#list
A = [1,4,6,3,3,4]

repeated = {}
for a in A:
    if a not in repeated.keys():
        repeated[a] = 1
    else:
        repeated[a] += 1

print(repeated)
        