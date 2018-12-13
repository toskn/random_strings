import random


filename = input('What is the name of the file? ')
strings = int(input('How many random strings do you want? '))


def get_file():
    with open(filename, encoding='utf-8') as file:
        file = file.read()
        file = file.split("\n")
        file.remove(file[0])
    return file


def rnd_str(file):
    i = 0
    list_num = random.sample(range(len(file)), strings)
    with open('random.csv', 'w+', encoding='utf-8') as file_s:
        while i < strings:
            a = list_num[i]
            file_s.write(file[a] + '\n')
            if i >= 1:
                for string in file_s:
                    if string == file[a]:
                        string.replace(file[a] + '\n', '')
                        i = i - 1
            i += 1
    return 0


rnd_str(get_file())
