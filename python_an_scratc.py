from time import sleep
import scratch

scr = scratch.Scratch()
x = 1

while True:
    
    
    try:
        x = x+1
        y = 2
        z = 3
        a = 4
        b = 5
        scr.sensorupdate({'x' : x})
        scr.sensorupdate({'y' : y})
        scr.sensorupdate({'z' : z})
        scr.sensorupdate({'a' : a})
        scr.sensorupdate({'b' : b})
        sleep(0.2)

    except:
        pass

