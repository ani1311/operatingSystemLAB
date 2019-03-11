

program = [1,2,3,4]
arrival_time = [4,2,5,0]
burst_time = [4,6,7,5]
priority = [3,1,4,2]


def shortestJobFirstPremptive():
    t = 0
    ans = []
    while(len(program) != 0):
        p = getNextProgram(t)
        if(p == -1):
            t = t + 1
            continue
        t = t + 1
        burst_time[p] = burst_time[p] - 1
        ans.append([program[p],1])
        sortByBurstTime()
        if(burst_time[p] == 0):
            delProcess(p)
    return [ans,t]


def swap(i,j):
    tp,ta,tb,tpri = program[i],arrival_time[i],burst_time[i],priority[i]
    program[i],arrival_time[i],burst_time[i],priority[i] = program[j],arrival_time[j],burst_time[j],priority[j] 
    program[j],arrival_time[j],burst_time[j],priority[j] = tp,ta,tb,tpri

def printProcesses():
    n = len(program)
    print("LIST OF PROCESSES WITH INFO") 
    print("id          ",end="")
    for i in range(n):
        print("%5d"%program[i],end="")
    
    print("\narrival Time",end="")
    for i in range(n):
        print("%5d"%arrival_time[i],end="")

    print("\nburst time  ",end="")
    for i in range(n):
        print("%5d"%burst_time[i],end="")
    
    print("\npriority    ",end="")
    for i in range(n):
        print("%5d"%priority[i],end="")
    
    print("\nEND")

def sortByBurstTime():
    for i in range(len(program)):
        for j in range(len(program) - 1 - i):
            if(burst_time[j] > burst_time[j + 1]):
                swap(j,j+1)


def delProcess(i):
    program.pop(i)
    arrival_time.pop(i)
    burst_time.pop(i)
    priority.pop(i)

def getNextProgram(t):
    i = 0
    while(arrival_time[i] > t):
        i = i + 1
    if(i == len(program)):
        return -1
    return i

def formatAns(ans):
    finalAns = []
    tp = ans[0][0]
    te = 1
    for i in range(1,len(ans)):
        if(tp == ans[i][0]):
            te = te + 1
        else:
            finalAns.append([tp,te])
            tp = ans[i][0]
            te = 1
    
    finalAns.append([tp,te])
    return finalAns

def printAns(ans,t):
    print("Process id     :",end="")
    for i in range(len(ans)):
        print("%3d"%ans[i][0],end="")
    print("\nExecution Time :",end="")
    for i in range(len(ans)):
        print("%3d"%ans[i][1],end="")
    print("\nLast Process finished at",t)


printProcesses()    
sortByBurstTime()
printProcesses()
ans = shortestJobFirstPremptive()
ans[0] = formatAns(ans[0])
printAns(ans[0],ans[1])