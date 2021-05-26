# -*- coding: utf-8 -*-
import re

def prep_file(fileName):
	file = (open(fileName))
	f = file.read()
	f = re.sub(r"\'", '\\\'', f)
	f = re.sub(r"\"", '\\\"', f)
	f = re.sub(r"\n", '\\n', f)
	f = re.sub(r"\d\d\/\d\d\/\d\d, \d\d:\d\d - ",'', f)
	return f

def phrase_count_lower(str):
    counts = dict()
    words = str.split('\n')

    for word in words:
        if word.lower() in counts:
            counts[word.lower()] += 1
        else:
            counts[word.lower()] = 1

    print_dic({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

def phrase_count(str):
    counts = dict()
    words = str.split('\n')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print_dic({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

def word_count_lower(str):

    counts = dict()
    words = str.split()

    for word in words:
        if word.lower() in counts:
            counts[word.lower()] += 1
        else:
            counts[word.lower()] = 1

    print_dic({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

def word_count(str):

    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print_dic({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

def print_dic(dic):
    for key, value in dic.items():
        print(key)
        print(value)


file_name = input('Insert the file name of the wpp convo: ')

file_read = prep_file(file_name)

print('file load successful \\o/')
print('What do you want to count:')
print('1. Words(case sensitive)')
print('2. Words(not case sensitive)')
print('3. Phrases(case sensitive)')
print('4. Phrases(case insensitive)')

i = int(input())
if(i == 1):
    word_count(file_read)
elif(i == 2):
    word_count_lower(file_read)
elif(i == 3):
    phrase_count(file_read)
elif(i == 4):
    phrase_count_lower(file_read)
else:
    print('Option not valid')