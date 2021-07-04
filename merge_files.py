file_dict = {}
sorted_files = []
file_txt_1 = []
file_txt_2 = []
file_txt_3 = []
with open("1.txt", "r", encoding="utf-8") as file_1:
    line_count_1 = 0
    for line in file_1:
        file_txt_1.append(line.strip())
        line_count_1 += 1
    file_dict[len(file_txt_1)] = ("1.txt", file_txt_1)


with open("2.txt", "r", encoding="utf-8") as file_2:
    line_count_2 = 0
    for line in file_2:
        file_txt_2.append(line.strip())
        line_count_2 += 1
    file_dict[len(file_txt_2)] = ("2.txt", file_txt_2)



with open("3.txt", "r", encoding="utf-8") as file_3:
    line_count_3 = 0
    for line in file_3:
        file_txt_3.append(line.strip())
        line_count_3 += 1
    file_dict[len(file_txt_3)] = ("3.txt", file_txt_3)


sortDic = sorted(file_dict.items())

# write sorted bands to file
filename = 'bands_sorted.txt'
line_count = 0
with open(filename, 'w', encoding="utf-8") as fout:
    for k in sortDic:
        for line in k[1][1]:
            print(line)
            band = f'Строка номер {line_count}: файла номер {k[1][0]} - {line}'
            fout.write(band + '\n')
            line_count += 1
        fout.write('\n')

