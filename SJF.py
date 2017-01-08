Total_process, process_Array, time, process_queue = 0, [], 0, []

def input_Function(Total_process, process_Array):
	print 'Enter number of processes'
	Total_process = int(raw_input())
	for i in xrange(Total_process):
	    process = []
	    print 'Enter PID'
	    process.append(raw_input())
	    print 'Enter arrival time'
	    process.append(int(raw_input()))
	    print 'Enter execution time'
	    process.append(int(raw_input()))
	    process_Array.append(process)
	return Total_process, process_Array

def Print_output(process_queue):  
	print '\n'
	print 'PID\tArrival Time\tBurst Time\tWaiting Time\tFinish Time'
	for process in process_queue:
		print process[0],'\t\t',process[1],'\t\t',process[2],'\t\t',process[4],'\t\t',process[3]
	return

def Sort(process_Array, process_queue):
	process_Array.sort(key = lambda process_Array:process_Array[1])
	dumy_array = []
	index = 0
	while index < Total_process:
	    at = process_Array[index][1]
	    while index < Total_process and process_Array[index][1] == at:
	        dumy_array.append(process_Array[index])
	        index = index+1
	    dumy_array.sort(key = lambda dumy_array:dumy_array[2])
	    for process in dumy_array:
	        process_queue.append(process)
	    dumy_array = []
	return process_Array, process_queue

def Waiting_time(process_queue):
	time=0
	for proc in process_queue:
		time = time if time > proc[1] else proc[1]
		time = time + proc[2]
		proc.append(time)
		proc.append(proc[3] - proc[2] - proc[1] if time > proc[1] else 0)
	return process_queue

Total_process , process_Array = input_Function(Total_process, process_Array)
process_Array, process_queue = Sort(process_Array, process_queue)
process_queue = Waiting_time(process_queue)
Print_output(process_queue)
