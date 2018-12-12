# read-only list
# child of read-only list can't be modified
# child of child can be modified
tu = (1, 2, 3, 'java', [2, 3, 5, 'json'], 'lemon')
# read: index-based read
tu[3]
for e in tu:
    print(e)

# tu[3] = tu[3].upper()
# will produce error
tu[4][3] = tu[4][3].upper()  # fine
tu[4].append('kotlin')
