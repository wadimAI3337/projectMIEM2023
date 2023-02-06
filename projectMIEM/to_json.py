import json
import re
import numpy as np
from itertools import cycle

dict_values = {}
file = open('4_1.json', encoding="utf-8")
data = json.load(file)
start_pos = 5
end_pos = 12

def data(data):
    for d in data:
        # print('DATA:', d['data'])
        # print('IIIIIIIIIIII: ', i)
        if len(d['data']) >= 3:
            cnt = 1
            for i in range(len(d['data'])):
                if re.match(r'\s{1,7}\d\.', string=d['data'][i]):
                    name = d['data'][i]
                    # print('Добавил эту строку: ', name)
                    name = str(cnt) + ' |' + d['data'][i]
                    if name in dict:
                        name = str(cnt) + name
                        dict[name] = []
                    else:
                        dict[name] = []
                    cnt += 1
                    # print('Я НЕ В ЦИКЛЕ: ', name)

    key = list(dict.keys())
    j = 0
    k = 0
    for d in data:
        print('REAL DATA: ', d['data'])
        if k < 30:
            if len(d['data'][start_pos:end_pos]):
                for i in range(len(d['data'][start_pos:end_pos])):
                    # print(d['data'][start_pos:end_pos][i])
                    # print(list(dict.keys()))
                    print('KEY: ', key[j])
                    # print('СЮДА: ', dict[key])
                    # print('YESSSS' if key in dict else 'NO')
                    print('ЭТО: ', d['data'][start_pos:end_pos][i])
                    dict[key[j]].append(d['data'][start_pos:end_pos][i])
                    j += 1
                k += 1
                print('----------')
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
                    # print('NAME: ', d['data'][i])
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
            # print('KEY:', key)
            for i in range(len(d['data'][start_pos:end_pos])):
                arr.append(d['data'][start_pos:end_pos][i])
                values.append(d['data'][start_pos:end_pos][i])
                # print('DATA:', d['data'][start_pos:end_pos][i])
                # dict[key].append(d['data'][start_pos:end_pos][i])
            # print('--------')
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

        distance_name = abs(names.index(a) - names.index(b))
        # print(distance_name)
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


# distance_values, distances_names = distance(arr, names)
#
# print('distances_names', distances_names)
# print('distance_values', distance_values)
# print(arr)
# print('')
# start = 0


def fill_gaps(distance_values, distances_names, arr):
    for gap in range(len(distance_values)):
        # print('distance_values[gap]:', distance_values[gap])
        print('arr[start:distance_values[gap]]:', arr[start:distance_values[gap]])
        for i in arr[start:distance_values[gap]]:
            # print(arr.index(i))
            if distances_names[gap] == 1:
                print(i)
            elif distances_names[gap] == 2:
                if arr.index(i) % distances_names[gap] == 0:
                    print('TRUE INDEX: ', arr.index(i), 'i:', i)
                elif arr.index(i) % distances_names[gap] != 0:
                    print('INDEX: ', arr.index(i), 'i:', i)
            elif distances_names[gap] == 3:
                print('INDEX: ', arr.index(i), 'i:', arr.index(i) + 3)
        start = 0
        start += distance_values[gap]
        print('-------------------')


# fill_gaps(distance_values, distances_names, arr)


def make_list(distance_values, distances_names):
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


# listochek = make_list(distance_values, distances_names)


def make_dictionary(dictionary, listochek):
    for lst in listochek:
        for item in lst:
            if item[0] not in dictionary:
                dictionary[item[0]] = []
            dictionary[item[0]].append(item[1])
