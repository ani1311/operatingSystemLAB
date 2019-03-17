
noOfResources = 3
process = [1,2,3,4]
aquired = [[1,3,2],[1,0,1],[0,3,2],[4,5,1]]
needed = [[2,1,1],[1,0,3],[5,6,3],[1,3,3]]
available = [4,2,4]



def Print():
    print("%-20s%-18s%-18s"%('Process no','Aquired','Needed'))
    print("%-20s"%(' '),end = "")
    
    for _ in range(2):
    	for i in range(noOfResources):
    		print("%-6s"%(str(chr(65 + i))),end = "")
    print()



    for i in range(len(process)):
    	print("%-20s"%(process[i]),end = "")
    	for j in range(noOfResources):
    		print("%-6s"%aquired[i][j],end = "")
    	for j in range(noOfResources):
    		print("%-6s"%needed[i][j],end = "")
    	print()

    print("\nAvailable resources ",end = "")
    
    for i in range(noOfResources):
    	print("%s = %d "%(str(chr(65 + i)),available[i]),end = "")

    print("\n\n")
    # print("\nAvailable resources A = %d b = %d c = %d"%(available[0],available[1],available[2]));


def delete(i):
    for p in range(len(available)):
        available[p] = available[p] + aquired[i][p]
    process.pop(i)
    aquired.pop(i)
    needed.pop(i)
    

def getProcess():
    for i in range(len(process)):
        if(needed[i][0] < available[0] and needed[i][1] < available[1] and needed[i][2] < available[2]):
            return i
    return -1

def bankers():
    solution = []
    while(len(process) != 0):
        p = getProcess()
        if(p == -1):
            return "NO POSSIBLE WAY OUT,SYSTEM UNSAFE"
        solution.append("P" + str(process[p]))
        delete(p)
        Print()
    return solution




Print()
print(bankers())

