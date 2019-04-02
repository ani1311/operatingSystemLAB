
memory = [[300,True],[300,False],[300,True],[300,False],[300,True]]
programs = [123,100,125,100]

def insertProgram(i,j):
    mem = memory[j][0]
    memory.pop(j)
    memory.insert(j,[programs[i],"p" + str(i)])
    memory.insert(j + 1,[mem - programs[i],False])
    

def printMemory():
    print("%-20s%-5s"%("Memory Status","Size"))
    for i in range(len(memory)):
        if(memory[i][1] == False):
            print("%-20s"%"empty",end="")
        elif(memory[i][1] == True):
            print("%-20s"%"Already Filled",end="")
        else:
            print("%-20s"%memory[i][1],end="")
            
        print("%-5d"%memory[i][0])
            
    print("\n")       

def bestFit():
    print("Best Fit ::")
    for i in range(len(programs)):
        mini = 0
        minVal = 99999
        
        for j in range(len(memory)):
            if(memory[j][1] == False and memory[j][0] >= programs[i] and memory[j][0] < minVal):
                mini = j
                minVal = memory[j][0]

        if(mini == 0 and memory[mini][0] < programs[i]):
            print("No space available")
            break
        else:
            insertProgram(i,mini)
            
def worstFit():
    print("Worst Fit ::")
    for i in range(len(programs)):
        maxi = 0
        maxVal = 0
        
        for j in range(len(memory)):
            if(memory[j][1] == False and memory[j][0] >= programs[i] and memory[j][0] > maxVal):
                maxi = j
                maxVal = memory[j][0]

        insertProgram(i,maxi)
            
        
def firstFit():
    print("First Fit ::")
    alloc = False
    for i in range(len(programs)):
        for j in range(len(memory)):
            if(memory[j][1] == False and memory[j][0] >= programs[i]):
                insertProgram(i,j)
                alloc = True
                break;
                
        if(alloc == False):
            print("No space available")
            break
def reset():
    global memory,programs
    memory = [[300,True],[300,False],[300,True],[300,False],[300,True]]
    programs = [123,100,125,100]
    
printMemory()
bestFit()
printMemory()
reset()
firstFit()
printMemory()
reset()
worstFit()
printMemory()

