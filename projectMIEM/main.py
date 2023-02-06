from to_json import data, make_list, distance, save_data, fill_gaps, make_dictionary

dictionary = {}

arr, names, values = save_data(data)
distance_values, distances_names = distance(arr, names)
fill_gaps(distance_values, distances_names, arr)
listochek = make_list(distance_values, distances_names)
make_dictionary(dictionary, listochek)

print(dictionary)

def executer(values):
    array = []
    k = 0
    for s in values:
        if re.findall(r'[^;]\d{1}\s-\s\d{1}', string=s) and ';' not in s:
            array.append((s, '1 = d|r:1'))
            print('Строка:', s, 'Обработана:', '1 = d|r:1')
            k += 1
        elif re.findall(r'[^;]\d{1}\s-\s\d{1}', string=s) and ';' in s:
            array.append((s, '1; = d|r:1'))
            print('Строка:', s, 'Обработана:', '1; = d|r:1')
            k += 1
        elif re.findall(r'[а-я]', string=s):
            array.append((s, '1 = s:1'))
            print('Строка:', s, 'Обработана:', '1 = s:1')
            k += 1
        elif re.findall(r'-', string=s):
            array.append((s, '- = s:1'))
            print('Строка:', s, 'Обработана:', '- = s:1')
            k += 1
        elif re.findall(r'\d\s±\s\d', string=s):
            array.append((s, '1 = dtv:1'))
            print('Строка:', s, 'Обработана:', '1 = dtv:1')
            k += 1
        elif re.findall(r'\d/\d', string=s) and '(' in s:
            array.append((s, '1/2 = {1(2) = d:2 } = d:1'))
            print('Строка:', s, 'Обработана:', '1/2 = {1(2) = d:2 } = d:1')
            k += 1
        elif re.findall(r'\d/\d', string=s):
            array.append((s, '1/2/ = d:1 = d:2'))
            print('Строка:', s, 'Обработана:', '1/2/ = d:1 = d:2')
            k += 1
        elif re.findall(r'\d', string=s) and '(' in s and ';' in s:
            array.append((s, 'Неверно задана строка для обработки'))
            print('Строка:', s, 'Обработана:', 'Неверно задана строка для обработки')
            k += 1
        elif re.findall(r'\d', string=s) and '(' in s:
            array.append((s, '1(2) = d:1'))
            print('Строка:', s, 'Обработана:', '1(2) = d:1')
            k += 1
        elif re.findall(r'/[0-9]', string=s):
            array.append((s, '/1/ = d:2'))
            print('Строка:', s, 'Обработана:', '/1/ = d:2')
            k += 1
        elif re.findall(r'[0-9]', string=s):
            array.append((s, '1 = d:1'))
            print('Строка:', s, 'Обработана:', '1 = d:1')
            k += 1
        elif ' ' in s:
            array.append((s, '_'))
            print('Строка:', '_', 'Обработана:', '_')
            k += 1
    print('K:', k)
    return array


def to_do():
    data = []
    cnt = 0
    arr_stop = distances_names[cnt]
    start = distances_names[cnt]
    arr_st = 0
    for value in distance_values:
        print(arr[arr_st:arr_stop])
        for i in range(start, value):
            print('DATA:', i)
        print('distances_names[cnt]', distances_names[cnt])
        arr_st += distances_names[cnt]
        cnt += 1
        print('----------')
        if cnt < len(distances_names):
            start = value + distances_names[cnt]
            arr_stop += distances_names[cnt]
            data.append((start, arr_stop))
    return data
