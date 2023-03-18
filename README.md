Парсинг Excel-файлов на Python на примере задачи из ЕГЭ по информатике

Сегодня разберем с вами довольное сложное 22 задание. Здесь стоит оговориться. Горе-эксперты ЕГЭ каждый раз выдумывают что-то новое, поэтому никогда не знаешь, что ожидать в следующий раз. Недавно на занятиях с учениками попалась задача, которая не решается обычными формулами, встроенными в Excel (во всяком случае я не знаю, как её автоматизировать средствами ТОЛЬКО Excel). И тут повезло, что таблица была небольшой, поэтому можно было решить задачу руками. Но я сразу же задумался над тем, а что если записей в ней было бы гораздо больше? Что если руками решать было бы не целесообразно, потому что это заняло бы бесконечно большое время, которого нет на экзамене? Как же тогда автоматизировать решение? Об этом мы сегодня с вами и поговорим... Заваривайте чай, здесь нужно будет посидеть и подумать.

Задача

В файле 22.xlsx содержится информация о совокупности N вычислительных процессов, которые могут выполняться параллельно или последовательно. Будем говорить, что процесс B зависит от процесса A, если для выполнения процесса B необходимы результаты выполнения процесса A. В этом случае процессы могут выполняться только последовательно.
Информация о процессах представлена в файле в виде таблицы. В первой строке таблицы указан идентификатор процесса (ID), во второй строке таблицы  — время его выполнения в миллисекундах, в третьей строке перечислены с разделителем «;» ID процессов, от которых зависит данный процесс. Если процесс является независимым, то в таблице указано значение 0. Определите минимальное время, через которое завершится выполнение всей совокупности процессов, при условии, что все независимые друг от друга процессы могут выполняться параллельно.

Все подробности и решение на канале: Репетитор IT mentor https://dzen.ru/itmentor


Parsing Excel files in Python on the example of a task from the Unified State Exam in computer science

Today we will analyze with you a rather difficult 22 task. It's worth making a reservation here. Would-be EXAM experts invent something new every time, so you never know what to expect next time. Recently, in classes with students, I came across a problem that cannot be solved with the usual formulas embedded in Excel (in any case, I do not know how to automate it using Excel ALONE). And then it was lucky that the table was small, so it was possible to solve the problem with your hands. But I immediately thought about what if there would have been much more entries in it? What if it would be impractical to solve with your hands, because it would take an infinitely long time, which is not on the exam? How then to automate the solution? That's what we're going to talk about today... Brew tea, you will need to sit and think here.

Task

In the file 22.xlsx contains information about a set of N computational processes that can be performed in parallel or sequentially. We will say that process B depends on process A if the execution of process B requires the results of the execution of process A. In this case, the processes can only be executed sequentially.
Information about the processes is presented in a file in the form of a table. The first row of the table shows the process identifier (ID), the second row of the table shows the time of its execution in milliseconds, the third row lists with a separator ";" the IDs of the processes on which this process depends. If the process is independent, then the value 0 is indicated in the table.
Determine the minimum time after which the execution of the entire set of processes will be completed, provided that all processes independent of each other can be executed in parallel.
