#NON_PREMPTIVE SJF WITH SAME ARRIVAL TIME = 0 
n=int(input("Process Count\n"))
processes=[]

for i in range(0,n):
 processes.append(i)
#Process list upgraded

exec_time = []
print("Exeution time correspondingly?? ")
for proc in range(n):
	exec_time.append(int(input()))
#Execution Time list upgraded 

exec_time = sorted(exec_time)
print(exec_time)
#Execution time list sorted and stored 

Waiting_time= []
Turnaround_time = []

avg_Waiting_time = 0
avg_Turnaround_time = 0

Waiting_time.append(0)
#For first process there will be no waiting time.
Turnaround_time.append(exec_time[0])

#Loop only for the rest of processes.
for i in range(1,len(exec_time)):  
 Waiting_time.insert(i,int(Waiting_time[i-1])+int(exec_time[i-1]))
 Turnaround_time.insert(i,int(Waiting_time[i])+int(exec_time[i]))
 avg_Waiting_time+=Waiting_time[i]
 avg_Turnaround_time+=Turnaround_time[i]

avg_Waiting=float(avg_Waiting_time)/n
avg_Turnaround=float(avg_Turnaround_time)/n

print("\nProcess\t  Execution Time\t  Waiting Time\t  Turn Around Time")	
for i in range(0,n):
 print(str(processes[i])+"\t\t"+str(exec_time[i])+"\t\t"+str(Waiting_time[i])+"\t\t"+str(Turnaround_time[i]))
 print("\n")
print("Waiting Time (AVG) "+str(avg_Waiting), "\t\t\tTurn Around Time (AVG) "+str(avg_Turnaround))
	