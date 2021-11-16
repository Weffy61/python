# Это уже делал не сморел разбор ваш
import json

total_dict = {}
average_profit = {}

with open('hw_7(ls_5).txt', 'r', encoding="utf-8") as f:
    my_list = f.readlines()
    company = 0
    av_prof = 0
    for i in my_list:
        line = i.split()
        total_profit = float(line[2]) - float(line[3])
        total_dict.update({line[0]: total_profit})
        company += 1
        av_prof += total_profit
        if total_profit > 0:
            average_profit.update({'average_profit': round(av_prof / company, 2)})

total_list = [total_dict, average_profit]

print(total_list)

with open('hw_7(ls_5).json', 'w') as f:
    json.dump(total_list, f)
