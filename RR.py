Process_array = []
wait_time = 0
time_slice=0
burst_time_sum = 0
wait = []
finish = []
burst_time = []
Total_process=0
def Process_input(Total_process, Process_array, time_slice):
	Total_process = int(raw_input('Enter the No. of Process : '))

	for i in xrange(Total_process):
		Process_array.append([])
		Process_array[i].append(raw_input('Enter Process Name : ' ))
		Process_array[i].append(int(raw_input('Enter Arrival Time :')))
		Process_array[i].append(int(raw_input('Enter Burst Time :')))

	time_slice = int(raw_input('Enter the time slice for Process : '))

	Process_array.sort(key = lambda Process_array:(Process_array[1],Process_array[2]))
	return Total_process, Process_array, time_slice

def Print_output(Total_process,Process_array,wait_time,wait):
	print 'Process Name \tArrival Time \t Burst Time \t  Waiting Time'
	for i in xrange(Total_process):
		print Process_array[i][0] ,'\t\t' ,Process_array[i][1] ,'\t\t', Process_array[i][2], '\t\t',wait[i]
		wait_time += wait[i]
	print 'Total Waiting Time : ',wait_time
	print 'Average Waiting Time : ',(wait_time/Total_process)
	return

def Calculate_waiting_time(Total_process,finish,burst_time_sum,Process_array,wait,time_slice):
	for i in xrange(Total_process):
		finish.append(0)
		burst_time_sum += Process_array[i][2]
		burst_time.append(Process_array[i][2])
		wait.append(0)
	index1 = 0
	index2 = 0
	while (index2<burst_time_sum):
		index1 = index1 % Total_process
		for k in xrange(time_slice):
			if(burst_time[index1] != 0):
				burst_time[index1] -= 1
				index2 += 1
				if (burst_time[index1] == 0):
					finish[index1] = index2 + Process_array[index1][1] 
					break
		index1 += 1
	for i in xrange(Total_process):
		wait[i]  = finish[i] - Process_array[i][1] - Process_array[i][2]
	return Total_process,finish,burst_time_sum,Process_array,wait,time_slice





Total_process, Process_array, time_slice = Process_input(Total_process, Process_array, time_slice)

Total_process,finish,burst_time_sum,Process_array,wait,time_slice = Calculate_waiting_time(Total_process,finish,burst_time_sum,Process_array,wait,time_slice)

Print_output(Total_process,Process_array,wait_time,wait)
