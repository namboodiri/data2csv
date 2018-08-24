import json
import csv


def convert(ip_list, file_name):

    if type(ip_list) == dict:
        ip_list = [ip_list]
    elif type(ip_list) == str:
        ip_list = json.loads(ip_list)

    if type(ip_list[0]) == dict:
        keys = ip_list[0].keys()
        op_file = csv.writer(open(file_name, "w+"))
        op_file.writerow(list(keys))

        for item in ip_list:
            op_file.writerow([item[i] if i in item else "" for i in keys])
    elif type(ip_list[0]) == list:
        op_file = csv.writer(open(file_name, "w+"))
        for item in ip_list:
            op_file.writerow(item)
