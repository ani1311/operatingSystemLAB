import queue

program = [1,2,3,4]
arrival_time = [4,2,5,0]
burst_time = [4,6,7,5]
priority = [3,1,4,2]

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

def sortByArrivalTime():
    for i in range(len(program)):
        for j in range(len(program) - 1 - i):
            if(arrival_time[j] > arrival_time[j + 1]):
                swap(j,j+1)
       
def getProcessesArrived(t):
    ans = []
    for i in range(len(arrival_time)):
        if(arrival_time[i] == t):
            ans.append(i)
    return ans
     
def checkDone():
    for i in burst_time:
        if(i != 0):
            return False
    return True
    
    
def roundRobin(qt):
    q = queue.Queue(100)
    t = 0
    ans = []
    t1 = getProcessesArrived(t)
    for i in t1:
        q.put(i)
    t = t + 1
    changeTime = 0
    p = q.get()
    while(not checkDone()):
        t1 = getProcessesArrived(t)
        for i in t1:
            q.put(i)
            
        if(changeTime == qt):
            q.put(p)
            p = q.get()
            changeTime = 0
        else:
            if(p == -1):
                t = t + 1
                continue
            ans.append([program[p],1])
            burst_time[p] = burst_time[p] - 1
            if(burst_time[p] == 0):
                if(q.empty()):
                    t = t + 1 
                    p = -1
                    continue
                p = q.get()
                changeTime = 0
                continue
            changeTime = changeTime + 1
        t = t + 1
    
    return [ans,t]
    


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
sortByArrivalTime()
printProcesses()
ans = roundRobin(2)
ans[0] = formatAns(ans[0])

printAns(ans[0],ans[1])
