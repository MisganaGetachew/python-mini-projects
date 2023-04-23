names = ["Alice", "Bob", "Charlie", "David"]


def reverseOne(item):
    return item[::-1]


print(list(map(reverseOne, names)))
# OR
print(list(map(lambda x: x[::-1], names)))
