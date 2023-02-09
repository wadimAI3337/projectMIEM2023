import json
import re
import numpy as np
from itertools import cycle

dict_values = {}
start_pos = 5
end_pos = 12


def data(data):
    for d in data:
        if len(d['data']) >= 3:
            cnt = 1
            for i in range(len(d['data'])):
                if re.match(r'\s{1,7}\d\.', string=d['data'][i]):
                    name = d['data'][i]
                    name = str(cnt) + ' |' + d['data'][i]
                    if name in dict:
                        name = str(cnt) + name
                        dict[name] = []
                    else:
                        dict[name] = []
                    cnt += 1

    key = list(dict.keys())
    j = 0
    k = 0
    arr_data = []
    for d in data:
        if k < 30:
            if len(d['data'][start_pos:end_pos]):
                for i in range(len(d['data'][start_pos:end_pos])):
                    arr_data.append((key[j], ['data'][start_pos:end_pos][i]))
                    dict[key[j]].append(d['data'][start_pos:end_pos][i])
                    j += 1
                k += 1
        else:
            break


def save_data(data):
    names = []
    arr = []
    values = []
    for d in data:
        if len(d['data']) >= 3:
            cnt = 1
            for i in range(len(d['data'])):
                if (re.match(r'\s{1,7}\d\.', string=d['data'][i])):
                    name = str(cnt) + ' |' + d['data'][i]
                    if name in arr:
                        name = str(cnt) + name
                        arr.append(name)
                        names.append(name)
                    else:
                        arr.append(name)
                        names.append(name)
                    cnt += 1
        if len(d['data'][start_pos:end_pos]):
            for i in range(len(d['data'][start_pos:end_pos])):
                arr.append(d['data'][start_pos:end_pos][i])
                values.append(d['data'][start_pos:end_pos][i])
    return arr, names, values


def distance(arr, names):
    sum = 0
    sort_names = []
    distances_names = []
    distance_values = []
    for name in names:
        if re.findall('[1]\.', string=name):
            sort_names.append(name)
    sort_names.append(names[-1])
    for j in range(len(sort_names) - 1):
        a = sort_names[j]
        b = sort_names[j + 1]
        distance_name = abs(names.index(a) - names.index(b))
        distances_names.append(distance_name)
    distances_names[-1] += 1

    for i in range(len(sort_names) - 2):
        a = sort_names[i]
        b = sort_names[i + 1]

        distance_value = abs(arr.index(a) - arr.index(b))
        sum = sum + distance_value
        distance_values.append(sum)
    distance_values.append(len(arr))
    return distance_values, distances_names


def fill_gaps(distance_values, distances_names, arr):
    start = 0
    arr_index = []
    for gap in range(len(distance_values)):
        for i in arr[start:distance_values[gap]]:
            if distances_names[gap] == 1:
                arr_index.append(i)
            elif distances_names[gap] == 2:
                if arr.index(i) % distances_names[gap] == 0:
                    arr_index.append(arr.index(i))
                elif arr.index(i) % distances_names[gap] != 0:
                    arr_index.append(arr.index(i))
            elif distances_names[gap] == 3:
                arr_index.append(arr.index(i) + 3)
        start = 0
        start += distance_values[gap]


def make_list(distance_values, distances_names, arr):
    listochek = []
    start_names = 0
    start_distance = 5
    for i in range(len(distance_values)):
        if i == 3:
            start_names += 1
        elif i == 6:
            start_names += 1
        stop_names = distances_names[i] + start_names
        names = (arr[start_names:stop_names])
        stop_names = stop_names - distances_names[i]
        values = (arr[start_distance:distance_values[i]])
        listochek.append((list(zip(cycle(names), values))))
        start_distance += len(values) + distances_names[i]
        start_names += distances_names[i] + len(values)
    return listochek


def make_dictionary(listochek):
    dictionary = {}
    for lst in listochek:
        for item in lst:
            if item[0] not in dictionary:
                dictionary[item[0]] = []
            dictionary[item[0]].append(item[1])
    return dictionary
