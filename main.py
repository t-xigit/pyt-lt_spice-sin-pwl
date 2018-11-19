
import matplotlib.pyplot as plot
import numpy as np
import math
import datetime
import time
from prettytable import PrettyTable

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#amount of points within one full cycle
sample_points = 6
Pi = math.pi
Sin_Frequenzy = 50

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

    #Don't want to have negative values therefore lift the sinwave by 1
    normalized = 1 + sin_rad
    percent = normalized / 2

    #the time of one pulse equals to duty cycle 100%
    period = 1/Sin_Frequenzy
    pulse_time = period / sample_points

    #Doing some logic here to have prettier prints
    time_unit_multiplier = 1
    period_unit_multiplier = 1
    TimeUnitPeriod = "s"
    TimeUnitPulse  = "s"

    if Sin_Frequenzy <= 1000:
            #Frequenzy Below 1KHz
            time_unit_multiplier = 1000
            period_unit_multiplier = 1000
            TimeUnitPeriod = "ms"
            TimeUnitPulse  = "us"

    on_time  = pulse_time * percent 
    off_time = pulse_time - on_time 

    index = 0

    x = PrettyTable()
    x.field_names = ["Sample Points", str(sample_points)]
    x.add_row(["Period in "+ TimeUnitPeriod, " {0:.2f}" .format(period*period_unit_multiplier )])
    x.add_row(["Pulse time in "+ TimeUnitPeriod, " {0:.2f}" .format(pulse_time*time_unit_multiplier )])
    print(x)

    OnTimeHeader = "On Time in " + TimeUnitPulse
    OffTimeHeader = "Off Time in " + TimeUnitPulse
    index = 0
    y = PrettyTable()
    y.field_names = ["Degree", "Radian", "sine(Radian)", "Normalized", "Percent", OnTimeHeader, OffTimeHeader]

    for x in np.nditer(degree):
        y.add_row(["{0:.2f}".format(degree[index]),
        "{0:.2f}".format(radian[index]),
        "{0:.2f}".format(sin_rad[index]),
        "{0:.2f}".format(normalized[index]),
        "{0:.1f}".format((percent[index])*100),
        "{0:.8f}".format(on_time[index]* time_unit_multiplier),
        "{0:.8f}".format(off_time[index]* time_unit_multiplier)])

        index += 1

    print('Calculated at - ' + datetime.datetime.now().strftime("%d-%m-%Y  %H:%M"))
    print(y)

def plot_OnTime(sample_points):

    print("Plot OnTime")
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

    #Don't want to have negative values therefore lift the sinwave by 1
    normalized = 1 + sin_rad
    percent = normalized / 2

    #the time of one pulse equals to duty cycle 100%
    period = 1/Sin_Frequenzy
    pulse_time = period / sample_points

    sample_time = (radian/2*Pi)*period

    #Doing some logic here to have prettier prints
    time_unit_multiplier = 1
    period_unit_multiplier = 1
    TimeUnitPeriod = "s"
    TimeUnitPulse  = "s"

    if Sin_Frequenzy <= 1000:
            #Frequenzy Below 1KHz
            time_unit_multiplier = 1000
            period_unit_multiplier = 1000
            TimeUnitPeriod = "ms"
            TimeUnitPulse  = "us"

    on_time  = pulse_time * percent 
    off_time = pulse_time - on_time 
    high_on  = sample_time -(on_time/2)
    high_off = sample_time +(on_time/2)

    index = 0

    x = PrettyTable()
    x.field_names = ["Sample Points", str(sample_points)]
    x.add_row(["Period in "+ TimeUnitPeriod, " {0:.2f}" .format(period*period_unit_multiplier )])
    x.add_row(["Pulse time in "+ TimeUnitPeriod, " {0:.2f}" .format(pulse_time*time_unit_multiplier )])
    x.add_row(["Frequenzy ", str(Sin_Frequenzy)])

    print(x)

    OnTimeHeader = "On Time in " + TimeUnitPulse
    OffTimeHeader = "Off Time in " + TimeUnitPulse
    index = 0
    y = PrettyTable()
    y.field_names = ["Degree", "Radian", "sine(Radian)", "Normalized", "Percent", 'Sample Time', 'High Time On', 'High Time Off', OnTimeHeader, OffTimeHeader]

    for x in np.nditer(degree):
        y.add_row(["{0:.2f}".format(degree[index]),
        "{0:.2f}".format(radian[index]),
        "{0:.2f}".format(sin_rad[index]),
        "{0:.2f}".format(normalized[index]),
        "{0:.1f}".format((percent[index])*100),
        "{0:.2f}".format((sample_time[index])*1000),
        "{0:.2f}".format((high_on[index])*1000),
        "{0:.2f}".format((high_off[index])*1000),
        "{0:.8f}".format(on_time[index]* time_unit_multiplier),
        "{0:.8f}".format(off_time[index]* time_unit_multiplier)])

        index += 1

    print('Calculated at - ' + datetime.datetime.now().strftime("%d-%m-%Y  %H:%M"))
    print(y)

    FileName = 'Frequenzy_'+ str(Sin_Frequenzy) + 'Hz'+'.pwl'
    print(FileName)
    with open(FileName,'w') as pwl:
        pwl.write(str(y))

    t = (on_time*1000)
    s = degree
    plot.bar(s, t)

    plot.xlabel('Degree')
    plot.ylabel('OnTime')
    plot.title('OnTime')
    plot.grid(True)
    plot.show()

def main():
    print ("Starting main()")
    #plot_sinus_tutorial()
    #plot_sinus(steps)
    plot_table(sample_points)
    plot_OnTime(sample_points)

main()
