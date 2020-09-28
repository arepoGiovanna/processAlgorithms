def dataP(noProcesses):
    data_P = []
    for i in range(noProcesses):
        print("==============================================")
        processID = int(input("Enter the Process ID here: ")) #Ask user to enter the name of the Process
        print("==============================================")
        
        print("==============================================")
        burst_time = int(input("Enter the burst time for process {} :".format(processID)))
        print("==============================================")
        
        print("==============================================")
        arrival_time = int(input("Enter arrival time: "))
        print("==============================================")
        print()
        data_P.append([processID, burst_time, arrival_time, 0])
    
    schedulingProcess(data_P)


def schedulingProcess( data_P):
    start_time = []
    exit_time = []
    s_time = 0
    data_P.sort(key=lambda x: x[1])  #lamba expression is the same as anonymous function
    '''
    Sort processes according to the Arrival Time
    '''
    for i in range(len(data_P)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(data_P)):
            if (data_P[j][1] <= s_time) and (data_P[j][3] == 0):
                temp.extend([data_P[j][0], data_P[j][1], data_P[j][2]])
                ready_queue.append(temp)
                temp = []
            elif data_P[j][3] == 0:
                temp.extend([data_P[j][0], data_P[j][1], data_P[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            '''
            Sort the processes according to the Burst Time
            '''
            start_time.append(s_time)
            s_time += ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(data_P)):
                if data_P[k][0] == ready_queue[0][0]:
                    break
            data_P[k][3] = 1
            data_P[k].append(e_time)

        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time += normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(data_P)):
                if data_P[k][0] == normal_queue[0][0]:
                    break
            data_P[k][3] = 1
            data_P[k].append(e_time)

    t_time = calculateTurnaroundTime(data_P)
    w_time = calculateWaitingTime(data_P)
    printData(data_P, t_time, w_time)
    #makeGanttChart(processID)

def calculateTurnaroundTime(data_P):
    total_turnaround_time = 0
    for i in range(len(data_P)):
        turnaround_time = data_P[i][4] - data_P[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time += turnaround_time
        data_P[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(data_P) #average_turnaround_time = total_turnaround_time / no_of_processes
    return average_turnaround_time


def calculateWaitingTime( data_P):
    total_waiting_time = 0
    for i in range(len(data_P)):
        waiting_time = data_P[i][5] - data_P[i][2]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time += waiting_time
        data_P[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(data_P)
    '''
    average_waiting_time = total_waiting_time / no_of_processes
    '''
    return average_waiting_time


def printData(data_P, average_turnaround_time, average_waiting_time):
    data_P.sort(key=lambda x: x[0])  #[0] refers to the 
    '''
    Sort processes according to the Process ID
    '''
    print("Process_ID  Arrival_Time    Burst_Time    Completed    Completion_Time    Turnaround_Time    Waiting_Time")

    for i in range(len(data_P)):
        for j in range(len(data_P[i])):

            print(data_P[i][j], end="		")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time:2.2f}')

    print(f'Average Waiting Time: {average_waiting_time:.2f}')
 