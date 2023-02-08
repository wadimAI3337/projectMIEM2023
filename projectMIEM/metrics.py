import json

def dicts_list(filenames, save_data, distance, fill_gaps, make_list, make_dictionary):
    dlists = []
    for f in filenames:
        ndict = {}
        file = open(f, encoding="utf-8")
        data = json.load(file)

        arr, names, values = save_data(data)
        distance_values, distances_names = distance(arr, names)
        fill_gaps(distance_values, distances_names, arr)
        listochek = make_list(distance_values, distances_names, arr)
        make_dictionary(ndict, listochek)
        dlists.append(ndict)
    return dlists


def dict_compare(dlists):
    different_keys = []
    for i in range(len(dlists) - 1):
        if len(dlists[i]) == len(dlists[i + 1]):
            d1 = dlists[i]
            d2 = dlists[i + 1]
            d1_keys = set(d1.keys())
            d2_keys = set(d2.keys())
            shared_keys = d1_keys.intersection(d2_keys)
            dict1_keys = d1_keys - d2_keys
            dict2_keys = d2_keys - d1_keys
            different_keys.append((dict1_keys, dict2_keys))
            modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
            same = set(o for o in shared_keys if d1[o] == d2[o])
            return different_keys, dict1_keys, dict2_keys, modified, same
        else:
            print("Two dictionaries don't have the same length")
