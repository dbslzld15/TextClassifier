import csv
import random
import os

os.chdir("C:\\Users\\parkwoojin\\PycharmProjects\\Examples\\crawlingdata")

file = open('텍스트_형용사.csv', 'r', encoding='euc-kr')
line = file.readlines()
random.shuffle(line)
rcsv = csv.reader(line)

file_write = open('텍스트_형용사_shuffled.csv', 'w', encoding='euc-kr', newline="")
wcsv = csv.writer(file_write)

for i in rcsv:
    try:
        wcsv.writerow([i[0].strip(), i[1]])
    except:
        pass
