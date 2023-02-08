from to_json import make_list, distance, save_data, fill_gaps, make_dictionary
from metrics import dicts_list, dict_compare
import os
import json

folder = "C:/Users//wadim/PycharmProjects/projectMIEM/files"
filenames = []

for filename in os.listdir(folder):
    filenames.append("files/" + filename)

dlists = dicts_list(filenames, save_data, distance, fill_gaps, make_list, make_dictionary)
different_keys, dict1_keys, dict2_keys, modified, same = dict_compare(dlists)
