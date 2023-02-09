from to_json import make_list, distance, save_data, fill_gaps, make_dictionary
from metrics import dicts_list, count_accuracy
from data_processing import dictionary
from metrics import get_diff_values
import os

folder = "C:/Users//wadim/PycharmProjects/projectMIEM/files"
filenames = []

for filename in os.listdir(folder):
    filenames.append("files/" + filename)

dlists = dicts_list(filenames, save_data, distance, fill_gaps, make_list, make_dictionary)
dct_acc = count_accuracy(dlists, dictionary)
diff_dict = get_diff_values()
