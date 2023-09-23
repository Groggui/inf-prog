list = open('C:/train.csv')
count_men, count_women = 0, 0
for line in list:
    line = line.split(',')
    if line[1] == '1' and line[5] == 'male':
        count_men += 1
    if line[1] == '1' and line[5] == 'female':
        count_women += 1
print('выжило мужчин:', count_men)
print('выжило женщин:', count_women)