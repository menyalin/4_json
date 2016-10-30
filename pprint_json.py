from func import *


if __name__ == '__main__':
    print("Загрузить JSON с портала открытых данных правительства Москвы: - 1")
    print("Самостоятельно выбрать файл на жестком диске: - 2")
    answer = int(input())
    data = load_data(answer)
    input('Нажмите "Enter" для вывода json в консоль')
    pretty_print_json(data)
