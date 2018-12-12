## dict
key-value pair data storage type, index-based read and write  

## insert or update
dict[key] = value  
if key in the dict, do update  
otherwise insert new key

## query
value = dict[key]  
get value of key, error occurs when key does'nt exist in dict  

value = dict.get(key, default_value)  
this method can avoid key does'nt exist error  

dict.keys()  
return all keys in a list  

dict.values()  
return all values in a list  

dict.items()  
return all key-value pairs in a list, which item is key and value tuple  
like [(key, value)...]  

for k, v in dict.items:
    print(k, v)  
this method use unpack value assigned

in one word: dict like json in some case.