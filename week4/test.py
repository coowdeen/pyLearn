import copy

a = [1, 2, 3, 4]

def nonDestructiveRemoveAll(a, value):

    result = []
    for element in a:
        if(element != value):
            result.append(element)
    return result

nonDestructiveRemoveAll(a, 3)

print(a)
print(nonDestructiveRemoveAll(a, 3))