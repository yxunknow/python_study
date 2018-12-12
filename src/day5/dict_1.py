# dict : key to value storage, map type data
# immutable type: tuple, bool, number, string => hashable
# mutable type: list, dict  => unhashable

# in dict, key must be immutable data type(be hashable)
# value has no limitation
# in other words: key must be tuple, bool, number or string type in dict

# advantage of dict type
# 1. random write and read
# 2. query use bin-tree algorithm
# 3. storage vary relationship data
# 4. data became ordered since python 3.6

# base operation

# declare a new dict
dic = {
    'name': 'java',
    'age': 23
}


# insert

# 1. insert or update a key
dic['location'] = '重庆市南岸区'

# 2. setDefault
# value is None or your specification
# if the key exist in dic, do nothing
# otherwise insert a new key
dic.setdefault('province', 'chongqing')

# delete

# 1. pop
# delete a key and return the value when key exist
# if key not exist will produce error
province = dic.pop('province')

# return default value
withDefault = dic.pop('key', 'default value')

# 2. popItem
# random delete a key-value and return a 2 elements tuple like tu = (key, value)
dic.popitem()

# 3. clear
# set dict to empty
dic.clear()

# 4. del
# delete the dic from memory
# del dic

# delete key, this method will produce error if the key is not in dict
# del dic['key']

# update
# 1. update a key(or insert a new key)
dic['key'] = 'value'

# 2. update
# add dict/iterable object to a dict
# D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
# If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
# If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
# In either case, this is followed by: for k in F:  D[k] = F[k]
dic.update(dic)

# query

# 1. get all keys
keys = dic.keys()  # return all keys as a list
values = dic.values()  # return all value as a list
items = dic.items()  # return all key-value as a (key, value) tuple list

# add some data
dic['name'] = 'java'
dic['country'] = 'us'

# 2. for loop
for key in dic:
    print(key)

for key, value in dic.items():
    print(key, value)

# 3. query key
# value = dict[key] if key not exit in dict will occur an error

# avoid key does'nt exist error
val = dic.get('names', 'default value')




