import xlrd
# Open the Workbook
workbook = xlrd.open_workbook("22.xls")
# Open the worksheet
worksheet = workbook.sheet_by_index(0)

#Внесение данных в cписок
processes = []
for row in range(1, 16):
    process = [0,0,0,0]
    for col in range(0,3):
        buf = str(worksheet.cell_value(row, col))
        if ';' in buf:
            process[col] = buf
        else:
            process[col] = str(int(float(buf)))
    processes.append(process)

# Заполнение времени до завершения процесса
for row in range(0, len(processes)):
    print("Текущий процесс ID = {}".format(processes[row][0]))
    if processes[row][2] == "0": # Если процесс не зависит от других
        processes[row][3] = int(processes[row][1])
        print("{} не зависит от процессов".format(processes[row][0]))
    else: # если процесс зависит от других процессов
        # время процесса = время_выполнения + max(задержек_зависимых)
        # Список процессов от которых зависит текущий рассматриваемый
        list_dependent = processes[row][2].split(';')
        print("{} зависит от процессов: {}".format(processes[row][0], list_dependent))
        
        # Список временных задержек зависимых процессов
        times_dependent = [ int(processes[int(ID)-1][3]) for ID in list_dependent ]
        
        # Расчет полного времени текущего процесса
        processes[row][3] = int(processes[row][1]) + max(times_dependent)
        
        print("Список временных задержек для {}: {}".format(processes[row][0], times_dependent))

    print("Полное время текущего процесса {}: {}\n".format(processes[row][0], processes[row][3]))

# Вывод информации                                                          
for row in range(0, len(processes)):
    print(processes[row])

# Время выполнения всех процессов
execution_time = max([p[3] for p in processes])
print("Время выполнения всех процессов: {}".format(execution_time))

