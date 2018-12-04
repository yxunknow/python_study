# list nested
# 3 layers nested list
li = ['java', 'js', ['json', 'bean', [1, 2, False]], 702]
# print first 'a' in java
print(li[0][1])
# string.capitalize(): convert first letter to upper case of string
li[0] = li[0].capitalize() #['Java', ...]
# set js to javascript
li[1] = li[1].replace('s', 'avascript')
# set json to JSON
li[2][1] = li[2][1].upper()
