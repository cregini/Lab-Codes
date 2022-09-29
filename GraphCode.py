import explorerhat
import matplotlib.pyplot as plt
import numpy as np

voltages=[ ]
volumes=[ ]
volume=0 

def read_pads(channel, event):
    global voltages
    global volumes
    global volume
    if channel == 3:
        voltage = explorerhat.analog.one.read()
        voltages.insert(0,voltage)
        volumes.insert(0,volume)
        print("Current Volume: ", volume, "Volumes: ", volumes)
        print("Current Reading: ", voltage, "Voltages: ", voltages)
        volume+=5
    if channel == 4:
        x=np.array(voltages)
        y=np.array(volumes)
        m, b = np.polyfit(x,y,1)
        plt.scatter(x, y, color='purple')
        plt.plot(x, m*x+b, color='red')
        plt.xlabel('Sensor Voltage')
        plt.ylabel('Water Volume (mL)')
        plt.title('y = ' + '{:.2f}'.format(m) + 'x' + ' + {:.2f}'.format(b))
        plt.show()

while True:   
    explorerhat.touch.pressed(read_pads)
