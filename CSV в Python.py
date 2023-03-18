import csv

processes = [] # структура под хранение всех процессов
with open("22.csv", encoding = 'Windows-1251') as data:
    reader_csv = csv.reader(data, delimiter = ";")
    count_row = 0
    for row in reader_csv:
        if count_row == 0: # выводим заголовки (один раз)
            print(f'Файл содержит столбцы: {"| ".join(row)}')
        else: # выводим строки, которые удалось распознать из файла
            print(f' {row[0]}  {row[1]}  {row[2]}')
            process = dict(ID = int(row[0]),
                           time = int(row[1]),
                           depend = str(row[2]),
                           exectime = 0)
            processes.append(process)          
        count_row += 1        
    print(f'Всего в файле {count_row} строк')

# Расчет времен полного завершения процессов
for p in processes:
    if p['depend'] == '0':
        p['exectime'] = p['time']
    else:
        list_depends = p['depend'].split(';')
        times_depends = [ processes[int(ID)-1]['exectime']
                          for ID in list_depends ] 
        p['exectime'] = p['time'] + max(times_depends)

# Вывод информации                                                          
for row in range(0, len(processes)):
    print(processes[row])

max_exec_time = 0
for p in processes:
    if p['exectime'] > max_exec_time:
        max_exec_time = p['exectime']

print(f'Время исполнение всех процессов {max_exec_time}')
