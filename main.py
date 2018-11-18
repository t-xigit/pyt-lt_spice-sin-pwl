
import matplotlib.pyplot as plot
import numpy as np
import math
import datetime
import time
from prettytable import PrettyTable

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#amount of points within one full cycle
sample_points = 12
Pi = math.pi
Sin_Frequenzy = 100

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

def plot_table(sample_points):

    print("Sample Points calculated: ", str(sample_points))
    #Rad per Step
    angle_rad = 2*Pi/sample_points
    print("Angle between Sample Points in Rad ", "{0:.4f}".format(angle_rad))
    #Degree per Step
    angle_deg = 360/sample_points
    print("Angle between Sample Points in Degree ", "{0:.2f}".format(angle_deg))

    degree = np.arange(0, int(math.degrees(2*Pi)), angle_deg)
    radian = np.arange(0, 2*Pi, angle_rad)
    sin_rad = np.sin(radian)

    if radian.size != degree.size:
        print('You fucked up stupid np.arrange failed')
        exit()

    normalized = 1 + sin_rad
    percent = normalized / 2

    #the time of one pulse equals to duty cycle 100%
    period = 1/Sin_Frequenzy
    pulse_time = period / sample_points

    on_time = pulse_time * percent
    off_time = pulse_time - on_time

    index = 0
    print ("Pulse time in ms: " + "{0:.2f}" .format(pulse_time*1000 ))

    index = 0
    y = PrettyTable()
    y.field_names = ["Degree", "Radian", "sine(Radian)", "Normalized", "Percent", "On Time", "Off Time"]

    for x in np.nditer(degree):
        y.add_row(["{0:.2f}".format(degree[index]),
        "{0:.2f}".format(radian[index]),
        "{0:.2f}".format(sin_rad[index]),
        "{0:.2f}".format(normalized[index]),
        "{0:.1f}".format(percent[index]),
        "{0:.2f}".format(on_time[index]),
        "{0:.2f}".format(off_time[index])])

        index += 1
    print(y)

def main():
    print ("Starting main()")
    #plot_sinus_tutorial()
    #plot_sinus(steps)
    plot_table(sample_points)

main()
