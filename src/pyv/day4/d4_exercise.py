li = [1, 2, 3, 4, 'java', [2, 4, 5, 'json'], '23']

for e in li:
    if type(e) == list:
        for ie in e:
            print(ie)
    else:
        print(e)