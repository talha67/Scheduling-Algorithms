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

def showtabluarForm( Process_array, Total_process ):
   Process_array.sort(key = lambda Process_array:Process_array[1])
   print 'Name\tArrivalTime\tBurstTime'
   for i in xrange(Total_process):
   	print Process_array[i][0],'\t\t',Process_array[i][1],'\t\t',Process_array[i][2]
   return

def PrintWaitingTime(Total_waiting_time,Total_process):
   print 'Waiting time: ',Total_waiting_time
   print 'Average waiting time: ',(Total_waiting_time/Total_process)
   return

Total_waiting_time, Total_process = inputProcess(Process_array,Total_process,Total_waiting_time)

showtabluarForm(Process_array,Total_process)

PrintWaitingTime(Total_waiting_time,Total_process)
    



