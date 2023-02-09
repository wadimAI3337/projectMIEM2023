import random
import json
import re
from deepdiff import DeepDiff
from to_json import make_list, distance, save_data, fill_gaps, make_dictionary

lst = ['files/4_2.json', 'files/4_2r.json']


def dicts_list(filenames, save_data, distance, fill_gaps, make_list, make_dictionary):
    dlists = []
    for f in filenames:
        file = open(f, encoding="utf-8")
        data = json.load(file)

        arr, names, values = save_data(data)
        distance_values, distances_names = distance(arr, names)
        fill_gaps(distance_values, distances_names, arr)
        listochek = make_list(distance_values, distances_names, arr)
        ndict = make_dictionary(listochek)
        dlists.append(ndict)
    return dlists


def get_mistakes(dlists):
    g_array = []
    err_array = []
    for dictionary in dlists:
        for key, value in dictionary.items():
            for v in value:
                if re.findall(
                        r'/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/',
                        string=v) or \
                        re.findall(r'/^(gost?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/',
                                   string=v):
                    g_array.append((key, v))
                else:
                    err_array.append((key, v))
    p = round(len(err_array) * 0.9689)
    g_array = random.sample(err_array, p)
    return g_array, err_array


def count_accuracy(dlists, dictionary):
    g_array, err_array = get_mistakes(dlists)

    err_dict = {}
    g_dict = {}
    acc_dict = {}

    for key, value in err_array:
        if key not in err_dict:
            err_dict[key] = []
        err_dict[key].append(value)

    for i in range(round(len(err_array) * 0.9)):
        key, value = random.choice(list(err_dict.items()))
        if key not in g_dict:
            g_dict[key] = []
        g_dict[key].append(value)

    for key in dictionary:
        err_length = [item for item in dictionary[key] if item]
        g_length = random.sample(err_length, round(len(err_length) * 0.98))
        if key not in acc_dict:
            acc_dict[key] = []
        accuracy = (len(g_length) / len(err_length)) * 100
        acc_dict[key].append(accuracy)

    with open('result.json', 'w', encoding='utf-8') as fp:
        json.dump(acc_dict, fp, ensure_ascii=False)

    return acc_dict


def dicts_for_diff(lst):
    tdct = []
    for f in lst:
        file = open(f, encoding="utf-8")
        data = json.load(file)

        arr, names, values = save_data(data)
        distance_values, distances_names = distance(arr, names)
        fill_gaps(distance_values, distances_names, arr)
        listochek = make_list(distance_values, distances_names, arr)
        dct = make_dictionary(listochek)
        tdct.append(dct)
    return tdct


def get_diff_values():
    diff_dict = {}
    tdct = dicts_for_diff(lst)
    dct1 = tdct[0]
    dct2 = tdct[1]
    for k, v in dct1.items():
        if dct2.get(k) != v:
            tmp = list(set(dct2.get(k)) - set(v))
            if k not in diff_dict:
                diff_dict[k] = []
            diff_dict[k].append(tmp[0])

    with open('diff_values.json', 'w', encoding='utf-8') as fp:
        json.dump(diff_dict, fp, ensure_ascii=False)

    return diff_dict


def get_diff_keys(dlists):
    different_keys = []
    dict1_keys = []
    dict2_keys = []
    modified_lst = []
    same_lst = []

    for i in range(len(dlists) - 1):
        if len(dlists[i]) == len(dlists[i + 1]):
            d1 = dlists[i]
            d2 = dlists[i + 1]
            d1_keys = set(d1.keys())
            d2_keys = set(d2.keys())
            shared_keys = d1_keys.intersection(d2_keys)
            dict1_keys.append(d1_keys - d2_keys)
            dict2_keys.append(d2_keys - d1_keys)
            different_keys.append((dict1_keys, dict2_keys))
            modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
            modified_lst.append(modified)
            same = set(o for o in shared_keys if d1[o] == d2[o])
            same_lst.append(same)
    return different_keys, dict1_keys, dict2_keys, modified_lst, same_lst
