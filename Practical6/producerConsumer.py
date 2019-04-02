import time

mutex = True
produced = 0

def produce():
    global mutex
    global produced
    while(mutex == False):
        continue
    
    mutex = False
    print("Aquiring mutex")
    time.sleep(3)
    print("Mutex Aquired")
    print("Producing")
    produced = produced + 1
    mutex = True
    print("Mutex realesed")
    print("produced = %d \n"%produced)

def consume():
    global mutex
    global produced
    
    while(mutex == False):
        continue
    
    mutex = False
    print("Aquiring mutex")
    time.sleep(3)
    print("Mutex Aquired")
    if(produced == 0):
        print("Nothing to consume")
        return
    else:
        produced = produced - 1
    print("Consuming")
    mutex = True
    print("Mutex realesed")
    print("produced = %d \n"%produced)



produce()
consume()
produce()
produce()
consume()
consume()
consume()

    
