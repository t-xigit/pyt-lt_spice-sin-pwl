
import matplotlib.pyplot as plot
import numpy as np
import math

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#amount of points within one full cycle
sample_points = 12
Pi = math.pi

def angle_steps(sample_rate):    
    angle = 2*Pi/sample_rate
    print(angle)
    return angle

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
    plot.title('About as simple as it gets, folks')
    plot.grid(True)
    plot.savefig("test.png")
    plot.show()

def plot_sinus(steps):

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
    plot.title('About as simple as it gets, folks')
    plot.grid(True)
    plot.savefig("test.png")
    plot.show()

def plot_table(steps):
#todo Degree, Radian, sine(Radian), Normalize to Zero, %

    degree = np.arange(0, math.degrees(2*Pi), math.degrees(steps))
    radian = np.arange(0, 2*Pi, steps)
    sin_rad = np.sin(radian)
    normalized = 1 + sin_rad
    percent = normalized / 2

    index = 0
    print ("Degree" + " -- " + "Radian" + " -- " + "sine(Radian)" + " -- " + " Normalized to 0")
        
    for x in np.nditer(degree):
        print(round(degree[index]) , end =" --- ")
        print("{0:.4f}".format(radian[index]) , end =" --- ")
        print("{0:.4f}".format(sin_rad[index]) , end =" --- ")
        print("{0:.4f}".format(normalized[index]) , end =" --- ")

        print ("{0:.2f}".format(percent[index]) , end ='\n')

        index = index + 1

def main():
    print ("Starting main()")
    
    steps = angle_steps(sample_points)
    #plot_sinus(steps)
    plot_table(steps)
    #plot_sinus_tutorial()
    
main()
