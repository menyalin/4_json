import json
from pprint import pprint


def load_data(filepath):
    my_file = open(filepath, mode="r", encoding='utf-8')
    data = json.load(my_file)
    my_file.close()
    return data


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':

    data = load_data('Магазины «Алкогольные напитки».json')
    pretty_print_json(data)
