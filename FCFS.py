Process_array = []
Total_process=0
Total_waiting_time = 0
def inputProcess( Process_array, Total_process, Total_waiting_time ):
   Total_process = int(raw_input('Total no of processes: '))
   for i in xrange(Total_process):
       Process_array.append([])
       Process_array[i].append(raw_input('Process Name: '))
       Process_array[i].append(int(raw_input('Arrival time: ')))
       Total_waiting_time += Process_array[i][1]
       Process_array[i].append(int(raw_input('Burst Time: ')))
   return Total_waiting_time, Total_process


def Waiting_time(Process_array):
	time=0
	for proc in Process_array:
		time = time if time > proc[1] else proc[1]
		time = time + proc[2]
		proc.append(time)
		proc.append(proc[3] - proc[2] - proc[1] if time > proc[1] else 0)
		proc.append(proc[4] + proc[2])
	return Process_array


def showtabluarForm( Process_array, Total_process ):
   Process_array.sort(key = lambda Process_array:Process_array[1])
   print 'Name\tArrivalTime\tBurstTime\tFinishTime\tWaitingTime\tTurnAroundTime'
   for i in xrange(Total_process):
   	print Process_array[i][0],'\t\t',Process_array[i][1],'\t\t',Process_array[i][2],'\t\t',Process_array[i][3],'\t\t',Process_array[i][4],'\t\t',Process_array[i][5]
   return

Total_waiting_time, Total_process = inputProcess(Process_array,Total_process,Total_waiting_time)

Process_array = Waiting_time(Process_array)

showtabluarForm(Process_array,Total_process)
