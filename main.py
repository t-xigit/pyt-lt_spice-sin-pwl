
import matplotlib.pyplot as plot
import numpy as np
import math
import datetime
import time

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#amount of points within one full cycle
sample_points = 12
Pi = math.pi
Sin_Frequenzy = 100

def angle_steps(sample_points):    
    angle_rad = 2*Pi/sample_points
    angle_deg = 360/sample_points
    print("Angle between Sample Points in Rad ", str(angle_rad))
    print("Angle between Sample Points in Degree ", str(angle_deg))
    return angle_rad

def plot_tutorial():
    plot.scatter(X,Y, s=60, c='red', marker='^')

    plot.title('Relationship Between Temperature and Iced Coffee Sales')
    plot.xlabel('Cups of Iced Coffee Sold')
    plot.ylabel('Temperature in Fahrenheit')

    plot.xlim(0,1000)
    plot.ylim(0,100)

    plot.show()

def plot_sinus_tutorial():

    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)
    plot.plot(t, s)

    plot.xlabel('time (s)')
    plot.ylabel('voltage (mV)')
    plot.title('Tutorial')
    plot.grid(True)
    plot.savefig("test.png")
    plot.show()

def plot_sinus(steps):

    now = datetime.datetime.now()
    t = np.arange(0.0, 2*Pi, steps)
    s = 1 + np.sin(t)
    print(s)
    t_ref = np.arange(0.0, 2*Pi, 0.1)
    s_ref = 1 + np.sin(t_ref)

    ratio = s/2
    print(ratio)

    plot.plot(t_ref, s_ref)
    plot.scatter(t,s, s=60, c='red', marker='^')

    plot.xlabel('time (s)')
    plot.ylabel('voltage (mV)')
    plot.title('About as simple as it gets -' + now.strftime("%d-%m-%Y  %H:%M"))
    plot.grid(True)
    plot.savefig("test.png")
    plot.show()

def plot_table(steps):

    # Cutting of the float is neccessary othersise np.arrange creates arrys with randon length
    steps=int(math.degrees(2*Pi) / math.degrees(steps))
    degree = np.arange(0, math.degrees(2*Pi), math.degrees(steps))
    radian = np.arange(0, 2*Pi, steps)
    sin_rad = np.sin(radian)
    normalized = 1 + sin_rad
    percent = normalized / 2

    #the time of one pulse equals to duty cycle 100%
    period = 1/Sin_Frequenzy
    pulse_time = period / steps 

    on_time = pulse_time * percent
    off_time = pulse_time - on_time

    index = 0
    print ("Pulse time in ms: " + "{0:.2f}" .format(pulse_time*1000 ))
    print ("Degree" + " -- " + "Radian" + " -- " + "sine(Radian)" + " -- " + " Normalized" + " -- " + "Percent"+ " -- " + " On Time" + " -- " + " Off Time")
        
    for x in np.nditer(degree):
        print(round(degree[index]) , end =" --- ")
        print("{0:.4f}".format(radian[index]) , end =" --- ")
        print("{0:.4f}".format(sin_rad[index]) , end =" --- ")
        print("{0:.4f}".format(normalized[index]) , end =" --- ")
        print ("{0:.2f}".format(percent[index]) , end =" --- ")
        print ("{0:.4f}".format(on_time[index]) , end =" --- ")
        print ("{0:.4f}".format(off_time[index]) , end ='\n')

        #print ("this the index --->" + str(x))
        index += 1

def main():
    print ("Starting main()")
    
    steps = angle_steps(sample_points)
    #plot_sinus(steps)
    plot_table(steps)
    #plot_sinus_tutorial()
    
main()
