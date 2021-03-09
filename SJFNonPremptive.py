class ShortestJobFirst():

    def processData(self, proc_count):
        process_data = []
        for i in range(proc_count):
            TEMP = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
            Execution_time = int(input(f"Enter Execution Time for Process {process_id}: "))
            TEMP.extend([process_id, arrival_time, Execution_time, 0])
            process_data.append(TEMP)

        ShortestJobFirst.schedulingProcess(self, process_data)
        

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])       
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)): 
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                    
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])                
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)                  

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

        t_time = ShortestJobFirst.calculateTurnaroundTime(self, process_data)
        w_time = ShortestJobFirst.calculateWaitingTime(self, process_data)
        ShortestJobFirst.printData(self, process_data, t_time, w_time)
    

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)        
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)        
        return average_waiting_time         

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])        
        print("Process_ID  Arrival_Time  Execution_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="             ")
            print()

        print(f'AVG TurnAround Time: {average_turnaround_time}')
        print(f'AVG Waiting Time: {average_waiting_time}')
    


##FCFS
##SJF NP
##SJF P
##Priority Scheduling NP and P
##Round Robin Scheduling

if __name__ == "__main__":
    proc_count = int(input("Process Count ??: (SJf Non-Preemptive) "))
    sjf = ShortestJobFirst()
    sjf.processData(proc_count)        

