import json
import os


def load_json_data(filepath):
    if os.path.exists(file_path):
        with open(filepath, 'r', encoding='utf-8') as file_handler:
            return json.load(file_handler)


if __name__ == '__main__':
    file_path = input("Select data file:")
    json_data = load_json_data(file_path)
    if not json_data:
        print('File not exists!')
        exit()
    print(json.dumps(json_data, indent=4, ensure_ascii=False, sort_keys=True))
