'''
d = {'1' : ['a','b'], '2':['c','d'], '3':['e','f']}

    # now combine each character with each other.
for i in d['1']:
    for j in d['2']:
        for k in d['3']:
            print(i+j+k)


d1 = {'item': 'item1', 'amount': 400}
d2 = {'item': 'item2', 'amount': 300}
d3 = {'item': 'item1', 'amount': 750}
d4 = {}
d = [d1, d2, d3]

for i in d:
    item = i['item']
    if item in d4:
        d4[item] += i['amount']
    else:
        d4[item] = i['amount']

print(d4)  # Output: {'item1': 1150, 'item2': 300}


k = 1
for i in range(5):
    for j in range(i+1):
        print(k,end = " ")
        k += 1
    print()
    


l = [1,2,3,4,[5,6,7,[9,8.111,4,6],10,11],14,50,9,11]

print

'''


def find_index(data, value):
    path = []
    
    def search(data, value, current_path):
        if isinstance(data, list):
            for i, item in enumerate(data):
                new_path = current_path + [i]
                if item == value:
                    path.append(new_path)
                    return True
                if search(item, value, new_path):
                    return True
        return False
    
    search(data, value, [])
    return path

l = [1, 2, 3, 4, [5, 6, 7, [9, 8.111, 4, 6], 10, 11], 14, 50, 9, 11]
index_path = find_index(l, 8.111)
print(index_path)
