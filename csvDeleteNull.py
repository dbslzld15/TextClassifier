import csv

f = open('텍스트_형용사_shuffled.csv', 'r', encoding='euc-kr')
f2 = open('텍스트_형용사_notnull.csv', 'w', encoding='euc-kr', newline='')

rdr = csv.reader(f)
wr = csv.writer(f2)

num = 0
for line in rdr:
    if len(line[1].lstrip()) == 0:
        print("공백 입니다")
    elif line[1] == '':
        print("공백 입니다")
    else:
        wr.writerow([line[0], line[1]])

f.close()
f2.close()
