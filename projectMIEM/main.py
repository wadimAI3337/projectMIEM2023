from data_processing import dictionary

# for i in range(len(dictionary)):
#     print(dictionary.keys())
#     break

d1 = {'apple': [1, 2, 3],
      'orange': [2, 4, 5]}

d2 = {'pineapple': [1, 2, 3],
      'apple': [1, 2, 3]}


def dict_compare(d1, d2):
    different_keys = []
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    dict1_keys = d1_keys - d2_keys
    dict2_keys = d2_keys - d1_keys
    different_keys.append((dict1_keys, dict2_keys))
    modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return different_keys, dict1_keys, dict2_keys, modified, same


# x = dict(a=1, b=2)
# y = dict(a=2, b=2)
different_keys, dict1_keys, dict2_keys, modified, same = dict_compare(d1, d2)

# print('different_keys', different_keys)
# print('dict1_keys', dict1_keys)
# print('dict2_keys', dict2_keys)
# print('modified', modified)
# print('same', same)
print(set(d1.keys()) - set(d2.keys()))
