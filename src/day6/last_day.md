# dict operation

## insert
1. dict[key] = value  
insert or update
2. dict.setDefault(key, value)  
insert new key or do nothing

## delete
1. deletedValue = dict.pop(key)
2. dict.clear()  
set dict to empty
3. del dict[key]
4. (key, value) = dict.popItem()
random delete key in dict

## update
dict[key] = value

## query
1. keys = dict.keys()
2. values = dict.values()
3. items = dict.items()  
return tuple of (key, value)
3. value = dict.get(key, default_value) 
