Arrival_time=[]
Burst_time=[]
Burst_copy=[]
sum_wait=0
sum_turnaround=0

def input_process(Arrival_time, Burst_time, Burst_copy):
	i=0
	Total_process=int(raw_input("Enter number of Process : "))
	while i<Total_process:
		print  "For process :",i+1
		Arrival_time.append(int(raw_input("Enter Arrival time of process :")))
		Burst_time.append(int(raw_input("Enter Burst time of process :")))
		Burst_copy.append(Burst_time[i])
		i+=1
	return Total_process, Arrival_time, Burst_time, Burst_copy


def Calculate_time(Total_process,Arrival_time,Burst_time,sum_wait,sum_turnaround):
	print "\n\nProcess\t|Turnaround Time| Waiting Time\n"
	Burst_copy.append(99999)
	time=0
	remain=0
	j=Total_process	
	while remain!=Total_process:
        	smallest=j
		i=0;        
		while i<Total_process:
	            if Arrival_time[i]<=time and Burst_copy[i]<Burst_copy[smallest] and Burst_copy[i]>0:
	                smallest=i
	            i+=1       
	        Burst_copy[smallest]-=1
	        if Burst_copy[smallest]==0:
	            remain+=1
	            endTime=time+1
	            print smallest+1,"\t","\t",endTime-Arrival_time[smallest],"\t","\t",endTime-Burst_time[smallest]-Arrival_time[smallest]
	            sum_wait+=endTime-Burst_time[smallest]-Arrival_time[smallest]
	            sum_turnaround+=endTime-Arrival_time[smallest]
	    	time+=1
	return Total_process,Arrival_time,Burst_time,sum_wait,sum_turnaround

def Print_Average_time(sum_wait,sum_turnaround):
	print "\nAverage waiting time = ",sum_wait*1.0/Total_process
	print "Average Turnaround time = ",sum_turnaround*1.0/5
	return




Total_process, Arrival_time, Burst_time, Burst_copy = input_process(Arrival_time, Burst_time, Burst_copy)

Total_process,Arrival_time,Burst_time,sum_wait,sum_turnaround=Calculate_time(Total_process,Arrival_time,Burst_time,sum_wait,sum_turnaround)

Print_Average_time(sum_wait,sum_turnaround)
