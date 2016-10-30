def load_data(variant):
    import requests
    import zipfile
    import os
    import json
    import sys
    import pprint

    if variant == 1:
        url = 'http://data.mos.ru/opendata/export/1854/json/1/2'
        tmp_file_name = 'tmp/tmp_file'
        tmp_path = 'tmp/'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            os.mkdir(tmp_path)
            with open(tmp_file_name, 'wb') as code:
                code.write(r.content)
                r.close()
            if zipfile.is_zipfile(tmp_file_name):
                z = zipfile.ZipFile(tmp_file_name, 'r')
                z.extractall(tmp_path)
                z.close()
            for x in os.listdir(tmp_path):
                if '.json' in x:
                    file_name = tmp_path + x
                    f = open(file_name, 'r', encoding='utf_8')
                    data = json.load(f)
                    print('JSON успешно загружен.')
                    print('-----------------------------------------------------------')
                    f.close()
            os.remove(tmp_file_name)
            os.remove(file_name)
            os.rmdir(tmp_path)
        else:
            print('Запрошенная информация не доступна. Программа завершает работу.')
            exit()
    elif variant == 2:
        print("Введите путь до JSON-файла.")
        path = input()
        try:
            f = open(path, 'r', encoding='utf_8')
        except Exception:
            print('Файл не найден')
            print(sys.exc_info()[1])
            exit()
        else:
            try:
                data = json.load(f)
            except Exception:
                pprint(sys.exc_info())
                print('JSON не найден. Программа завершает работу.')
                exit()
            else:
                print('JSON успешно загружен.')
                print('-----------------------------------------------------------')
    else:
        print('The request is invalid. The program shuts down.')
        exit()
    return data


def pretty_print_json(data):
    from pprint import pprint
    pprint(data)